from functions.write_file import write_file 

filepath = "lorem.txt"
print(f"Result for '{filepath}' file:")
print(write_file("calculator", filepath, "wait, this isn't lorem ipsum"))
print("-----------------------------------")

filepath = "pkg/morelorem.txt"
print(f"Result for '{filepath}' file:")
print(write_file("calculator", filepath, "lorem ipsum dolor sit amet"))
print("-----------------------------------")

filepath = "/tmp/temp.txt"
print(f"Result for '{filepath}' file:")
print(write_file("calculator", filepath, "this should not be allowed"))
print("-----------------------------------")


