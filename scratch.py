some_times = ["3:19.44", "3:33.20", "3:48.17", "4:04.73", "4:23.52"]

def convert_time_to_seconds(time):
    split_time = time.strip().split(":")
    print(split_time)
    seconds = round((float(split_time[0]) * 60 + float(split_time[1])), 2)
    return seconds

for time in some_times:
    print(convert_time_to_seconds(time))