import pandas as pd

# Input decimal number
decimal_num = int(input("Enter Decimal Number: "))

# Convert decimal to 8-bit binary
binary = format(decimal_num, '08b')

# Count number of 1s
ones = binary.count('1')

# Calculate parity bits
even_parity = 0 if ones % 2 == 0 else 1
odd_parity = 1 if ones % 2 == 0 else 0

# Append parity bits
even_parity_data = binary + str(even_parity)
odd_parity_data = binary + str(odd_parity)

# Display results
print("\nDecimal Number:", decimal_num)
print("Binary (8-bit):", binary)
print("Number of 1s:", ones)
print("Even Parity Bit:", even_parity)
print("Odd Parity Bit:", odd_parity)
print("Even Parity Data:", even_parity_data)
print("Odd Parity Data :", odd_parity_data)