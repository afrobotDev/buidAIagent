from functions.get_file_content import get_file_content 

filepath = "lorem.txt"
print(f"Result for '{filepath}' file:")
print(get_file_content("calculator", filepath)) 
print("-----------------------------------")

filepath = "main.py"
print(f"Result for '{filepath}' file:")
print(get_file_content("calculator", filepath))
print("-----------------------------------")

filepath = "pkg/calculator.py"
print(f"Result for '{filepath}' file:")
print(get_file_content("calculator", filepath))
print("-----------------------------------")

filepath = "/bin/cat"
print(f"Result for '{filepath}' file:")
print(get_file_content("calculator", filepath))
print("-----------------------------------")

filepath = "pkg/does_not_exist.py"
print(f"Result for '{filepath}' file:")
print(get_file_content("calculator", filepath))

