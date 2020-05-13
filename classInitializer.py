
variablesString = input("Enter the variable names you wish to initialize separated by a space: ")
variables = variablesString.split()
output = "\n\ndef __init__(self"

for var in variables:
    output += f", {var} = None"

#output = output[:-2]
output += "):\n"

for var in variables:
    output += f"\tself.{var} = {var} \n"

print(output)
