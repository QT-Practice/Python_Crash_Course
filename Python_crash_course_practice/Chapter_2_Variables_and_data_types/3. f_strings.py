# f strings aka format strings. 
# Python formats the string by replacing the name of any variable in braces with its value. 

first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}" 
print (f"Hello, {full_name}. \n Good to meet you.")
print (f"Hello, {full_name.title()}. \n Good to meet you.")