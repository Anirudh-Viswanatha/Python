# Prime Number Checker
list = []
def prime_checker(number):
  for i in range(1,number+1):
    if number % i == 0:
      list.append(i)
  if len(list) <= 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.") 
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)


# ----------------------------------------------------
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number): ---> here our range is from 2 to number meaning range starts from 2 and ends number-1 (does not include number). So since we dont have 1 and number itself which are the only numbers prime numbers can be divisible by, if number divisible by any number(i) cleanly, its not a prime number anymore.
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")   
# # Your code above this line 👆
# n = int(input()) # Check this number
# prime_checker(number=n)