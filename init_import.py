import csv
import os
import re

csv_file_path = 'input.csv'
output_csv_file_path = 'output_concatenated.csv'
selected_columns = ['display', 'value']

with open(csv_file_path, 'r') as input_csv, open(output_csv_file_path, 'w', newline='') as output_csv:
    csv_reader = csv.DictReader(input_csv)

    ## Assuming the first two columns are named 'column1' and 'column2'
    columns_to_concatenate = ['First', 'Last']

    fieldnames = csv_reader.fieldnames + ['display']

    csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    csv_writer.writeheader()

    data_to_sort = []

    for row in csv_reader:
        ## Use regex to clean up inputs values and remove whitespace
        first = re.sub(r'[^a-zA-Z]', '',row['First'])
        last = re.sub(r'[^a-zA-Z]', '',row['Last'])

        ##Concatenate the values of the first two fields
        concatenated_value = f"{first} {last}"
        #concatenated_value = f"{row['First']} {row['Last']}"
        
        ## Add the concatenated value to the row
        row['display'] = concatenated_value

        ## Create a dictionary with selected columns
        selected_row = {col: row[col] for col in selected_columns}

        ## Append the selected row to the list for sorting
        data_to_sort.append(selected_row)

    ## Sort the data based on the 'display' column
    sorted_data = sorted(data_to_sort, key=lambda x: x['display'])

    ## Write the sorted data to the output CSV file
    for sorted_row in sorted_data:
        csv_writer.writerow(sorted_row)

print(f'Concatenation and sorting complete. Concatenated and sorted data written to {output_csv_file_path}')

## Delete input file
if os.path.exists(csv_file_path):
  os.remove(csv_file_path)
  print(f'{csv_file_path} Removed')
else:
  print("The file does not exist")