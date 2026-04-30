from functions.run_python_file import run_python_file, format_result     

filepath = "main.py"
print(f"Result for '{filepath}' file:")
print(run_python_file("calculator", {filepath}))
print("-----------------------------------")

filepath = "tests.py" 
print(f"Result for '{filepath} file:")
print(run_python_file("calculator", filepath))
print("-----------------------------------")

filepath = "main.py"
print(f"Result for '{filepath}' file:")
print(run_python_file("calculator", {filepath}, ["3 + 5"]))
print("-----------------------------------")

filepath = "../main.py"
print(f"Result for '{filepath}' file:")
print(run_python_file("calculator", filepath))
print("-----------------------------------")

filepath = "nonexistent.py"
print(f"Result for '{filepath}' file:")
print(run_python_file("calculator", filepath)))
print("-----------------------------------")

filepath = "lorem.txt"
print(f"Result for '{filepath}' file:")
print(run_python_file("calculator", filepath)))
print("-----------------------------------")



