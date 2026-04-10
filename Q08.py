# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
num = int(input("Enter a number: "))
sum = 0
digit = num
while digit !=0:
    sum = sum + digit%10
    digit //= 10

print(f"Sum of digits of {num} = {sum}")