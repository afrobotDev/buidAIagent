from functions.get_files_info import get_files_info 

directory = "."
if directory == '.':
    print(f"Result for current directory:")
    print(get_files_info("calculator", directory)) 
    print("-----------------------------------")

directory = "pkg"
print(f"Result for '{directory}' directory:")
print(get_files_info("calculator", directory))

print("-----------------------------------")

directory = "/bin"
print(f"Result for '{directory}' directory:")
print(get_files_info("aiagent/calculator", directory))

print("-----------------------------------")

directory = "../"
print(f"Result for '{directory}' directory:")
print(get_files_info("aiagent/calculator", directory))


