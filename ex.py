with open('mydefaults.ini.txt', 'r') as ini_file:
    content = ini_file.read()

# Count the number of letters [a-z, A-Z]
letter_count = sum(c.isalpha() for c in content)

# Count the instances of numbers [0-9]
number_count = sum(c.isdigit() for c in content)

# Write the counts to an output file
with open('outputs.txt', 'w') as output_file:
    output_file.write(f"Letter count: {letter_count}\n")
    output_file.write(f"Number count: {number_count}\n")

print("Counts have been written to outputs.txt.")
