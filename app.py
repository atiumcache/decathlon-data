from bs4 import BeautifulSoup
import csv
import requests


def main(page_num):
    url = "https://worldathletics.org/records/all-time-toplists/combined-events/decathlon/all/men/senior?regionType=world&windReading=regular&page=" + str(page_num) + "&bestResultsOnly=false&firstDay=1899-12-31&lastDay=2023-12-27&maxResultsByCountry=all&eventId=10229629&ageCategory=senior"

    html_data = scrape_website(url)

    if html_data:
        parse_html(html_data, page_num)
    else:
        print("Failed to fetch HTML data.")


def scrape_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assign the HTML content to the html_data variable
            html_data = response.text
            return html_data
        else:
            print(f"Failed to retrieve HTML. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def parse_html(html_data, iteration):
    soup = BeautifulSoup(html_data, 'html.parser')

    # Open a CSV file for writing
    with open('decathlon_results.csv', 'a', newline='') as csvfile:
        # Define the CSV writer
        csvwriter = csv.writer(csvfile)

        # Write the header row if this is the first page
        if iteration == int(1):
            header_row = ['Rank', 'Mark', 'Competitor', 'DOB', 'Nat', 'Pos', 'Venue', 'Date', 'ResultScore']
            events_header = [
                '100m', 'Long Jump', 'Shot Put', 'High Jump', '400m', '110m Hurdles',
                'Discus Throw', 'Pole Vault', 'Javelin Throw', '1500m'
            ]
            header_row.extend(events_header)
            csvwriter.writerow(header_row)

        # Find all rows in the table body
        rows = soup.select('.records-table tbody tr')

        # Iterate through each row
        for i in range(0, len(rows), 2):  # Skip every second row (the one with colspan)
            # Extract data from each cell
            rank = rows[i].select_one('td[data-th="Rank"]')
            mark = rows[i].select_one('td[data-th="Mark"]')
            competitor = rows[i].select_one('td[data-th="Competitor"] a')
            dob = rows[i].select_one('td[data-th="DOB"]')
            nat = rows[i].select_one('td[data-th="Nat"]')
            pos = rows[i].select_one('td[data-th="Pos"]')
            venue = rows[i].select_one('td[data-th="Venue"]')
            date = rows[i].select_one('td[data-th="Date"]')
            result_score = rows[i].select_one('td[data-th="ResultScore"]')

            # Check if elements are found before accessing the text attribute
            if all([rank, mark, competitor, dob, nat, pos, venue, date, result_score]):
                score_cell = rows[i + 1].select_one('td[colspan="100"]')
                if score_cell:
                    individual_scores_text = score_cell.text.strip()

                    # Adjust the format for the times/scores
                    formatted_scores = format_scores(individual_scores_text)
                    

                    csvwriter.writerow([
                        rank.text.strip(), mark.text.strip(), competitor.text.strip(),
                        dob.text.strip(), nat.text.strip(), pos.text.strip(),
                        venue.text.strip(), date.text.strip(), result_score.text.strip()] + formatted_scores)
                else:
                    print("Individual scores not found for this row.")
            else:
                print("Some data is missing in this row.")


def format_scores(data_list):
    ten_records = []
    record = ""

    for char in list(data_list):
        

        if char in ["(", "/", ")", " "]: 
            
            if record and "+" not in record and "-" not in record:
                ten_records.append(record)
                record = ""
            else:
                record = ""
                continue
            
        elif char.isnumeric() or char in [".", "+", "-", ":"]:
            record = "".join([record, char])
    
    for i, entry in enumerate(ten_records):
        if entry == "0.0" or entry == 0.0:
            ten_records.pop(i)

    if len(ten_records) == 10:
        return ten_records
    
    else:
        return []


if __name__ == "__main__":
    for i in range(1, 18):
        main(i)
