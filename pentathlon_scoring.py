import csv
from sklearn.linear_model import LinearRegression
import numpy as np
import datetime


def convert_time_to_seconds(time):
    split_time = time.strip().split(":")
    seconds = round((float(split_time[0]) * 60 + float(split_time[1])), 2)
    return seconds

# Initialize training data 
# Data gathered from IAAF Scoring Tables of Athletics
LJ_x = np.array([9.19, 8.96, 8.5, 8.0, 7.5, 7.0, 6.0]).reshape(-1, 1)
LJ_y = np.array([1399, 1348, 1247, 1138, 1029, 922, 710])
DT_x = np.array([78.39, 67.57, 56.69, 45.76, 34.78]).reshape(-1,1)
DT_y = np.array([1400, 1200, 1000, 800, 600])
JT_x = np.array([101.63, 87.53, 73.36, 59.13, 44.82]).reshape(-1,1)
JT_y = np.array([1400, 1200, 1000, 800, 600])

    # 1500m times are in seconds, using convert_time function above
run1500_x = np.array([199.44, 213.2, 228.17, 244.73, 263.52]).reshape(-1,1)
run1500_y = np.array([1400, 1200, 1000, 800, 600])
run200_x = np.array([19.8, 20.0, 20.5, 21.0, 22.0, 23.0, 24.0, 25.0]).reshape(-1, 1)
run200_y = np.array([1252, 1220, 1143, 1068, 925, 793, 671, 560])

# Creating the models
LJ_reg = LinearRegression().fit(LJ_x, LJ_y)

DT_reg = LinearRegression().fit(DT_x, DT_y)

JT_reg = LinearRegression().fit(JT_x, JT_y)

run1500_reg = LinearRegression().fit(run1500_x, run1500_y)

run200_reg = LinearRegression().fit(run200_x, run200_y)

fields = ["Rank","Mark","Competitor","DOB","Nat","Pos","Venue",'Date',"Long Jump","Discus Throw","Javelin Throw","1500m","200m","ResultScore"]
all_rows = []

# Predict the scores based on the sample data form CSV
# Then, add each of the 5 scores for a total
with open('pentathlon_results.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        try:
            x_value_LJ = np.array([float(row[8])]).reshape(-1, 1)
            predicted_LJ = LJ_reg.predict(x_value_LJ)

            x_value_DT = np.array([float(row[9])]).reshape(-1, 1)
            predicted_DT = DT_reg.predict(x_value_DT)

            x_value_JT = np.array([float(row[10])]).reshape(-1, 1)
            predicted_JT = JT_reg.predict(x_value_JT)

            seconds_1500 = convert_time_to_seconds(row[11])
            x_value_1500 = np.array([seconds_1500]).reshape(-1, 1)
            predicted_1500 = run1500_reg.predict(x_value_1500)

            x_value_200 = np.array([float(row[12])]).reshape(-1, 1)
            predicted_200 = run200_reg.predict(x_value_200)
            
            total_score = predicted_200 + predicted_1500 + predicted_JT + predicted_DT + predicted_LJ

            row[13] = round(total_score[0])

            all_rows.append(row)

        except:
            continue

with open('pentathlon_w_scores.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    writer.writerows(all_rows)
    
    


