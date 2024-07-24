import subprocess
###############################################################################################################################################################################################
#Notes The Format of the columns requires columns First, Last, value, case sensitive
###############################################################################################################################################################################################

## List of Python files to run
python_files = ['init_import.py', 'reorderimport.py', 'import-to-json.py']

## Iterate over the list and run each Python file
for file in python_files:
    print(f"Running {file}...")
    try:
        ## Run the Python file using subprocess
        subprocess.run(['python', file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file}: {e}")
    print(f"{file} executed successfully.\n")

print("All Python files executed.")