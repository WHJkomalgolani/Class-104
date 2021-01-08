import csv
with open('height-weight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

    #This above code will just open the file in the backend. No output will be there.