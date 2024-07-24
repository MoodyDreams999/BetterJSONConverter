import csv
import os

input_csv_path = 'output_concatenated.csv'
output_csv_path = 'output_reordered.csv'

## Column to move to the first position
columns_to_move = ['display', 'value']   ## Replace with your actual column name


## Read the input CSV file and create a list with only the desired column
data = []
with open(input_csv_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        modified_row = {col: row[col] for col in columns_to_move}
        data.append(modified_row)

## Write the new CSV file with modified rows
with open(output_csv_path, 'w', newline='') as csv_file:
    ## Write header row
    fieldnames = columns_to_move
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    ## Write data rows
    csv_writer.writerows(data)

print(f'Modification complete. Result written to {output_csv_path}')

## Delete input file
if os.path.exists(input_csv_path):
  os.remove(input_csv_path)
  print(f'{input_csv_path} Removed')
else:
  print("The file does not exist")