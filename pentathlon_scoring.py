import csv
from sklearn.linear_model import LinearRegression
import numpy as np

# Initialize training data 
# Data gathered from IAAF Scoring Tables of Athletics
LJ_x = np.array([9.19, 8.96, 8.5, 8.0, 7.5, 7.0, 6.0]).reshape(-1, 1)
LJ_y = np.array([1399, 1348, 1247, 1138, 1029, 922, 710])
DT_x = np.array([78.39, 67.57, 56.69, 45.76, 34.78]).reshape(-1,1)
DT_y = np.array([1400, 1200, 1000, 800, 600])
JT_x = np.array([101.63, 87.53, 73.36, 59.13, 44.82]).reshape(-1,1)
JT_y = np.array([1400, 1200, 1000, 800, 600])
run1500_x = np.array([])
run1500_y = np.array([1400, 1200, 1000, 800, 600])
run200_x = np.array([19.8, 20.0, 20.5, 21.0, 22.0, 23.0, 24.0, 25.0]).reshape(-1, 1)
run200_y = np.array([1252, 1220, 1143, 1068, 925, 793, 671, 560])

# Creating the model
run200_reg = LinearRegression()

# Fitting the model
run200_reg.fit(run200_x, run200_y)

with open('pentathlon_results.csv', 'r+') as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(csvfile)

    for row in reader:
        try:
            x_value_200 = np.array([float(row[12])]).reshape(-1, 1)

            predicted_200 = run200_reg.predict(x_value)
            
        except:
            continue
    