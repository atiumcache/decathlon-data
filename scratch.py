




data1 = "( 10.55/+0.3 - 7.80/+1.2 - 16.00 - 2.05 - 48.42 / 13.75/-1.1 - 50.54 - 5.45 - 71.90 - 4:36.11 )"

ten_records = []
record = ""

for char in list(data1):
    

    if char in ["(", "/", ")", " "]: 
        
        if record and "+" not in record and "-" not in record:
            ten_records.append(record)
            record = ""
        else:
            record = ""
            continue
        
    elif char.isnumeric() or char in [".", "+", "-", ":"]:
        record = "".join([record, char])

print(ten_records)