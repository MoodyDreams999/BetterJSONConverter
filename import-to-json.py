import os
from datetime import date
import csv
import json

# date object of today's date
today = date.today()
data = []
folder_to_create = r"PID-%s" % today


if not os.path.exists(folder_to_create):
        os.makedirs(folder_to_create)




def make_json(csvFilePath, jsonFilePath, folder_to_create):
    # Get list of files in the folder
  files_in_folder = os.listdir(folder_to_create)
    
  with open(csvFilePath, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
          data.append(row)


    # Find the highest numbered file
  file_extension = '.json'
  highest_number = 0
  for file_name in files_in_folder:
      if file_name.startswith(jsonFilePath) and file_name.endswith(file_extension):
            file_number = int(file_name[len(jsonFilePath):-len(file_extension)])
            highest_number = max(highest_number, file_number)
    
    # Generate new file name with the next number
  new_file_name = f"{jsonFilePath}{highest_number + 1}{file_extension}"
    
    # Save file
  with open(os.path.join(folder_to_create, new_file_name), 'w') as jsonf:
          jsonf.write(json.dumps(data, indent=2))
        # Here you can write data to the file if needed
  pass

# Example usage
csvFilePath = r"output_reordered.csv"
jsonFilePath = r"Output_%s_" % today
make_json(csvFilePath, jsonFilePath, folder_to_create)




if os.path.exists(csvFilePath):
  os.remove(csvFilePath)
  print(f'{csvFilePath} Removed')
else:
  print("The file does not exist")