alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo) # ----> displays a caesar cipher logo

def caesar(text, shift, direction):
  string = ""
  for char in text:
    if char not in alphabet:
      string += char
    else:
      position = alphabet.index(char)
      if direction == "encode":
        new_position = position + shift
        string += alphabet[new_position]
      elif direction == "decode":
        new_position = position - shift
        string += alphabet[new_position]
  print(f"The {direction}d text is {string}")


should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26 # usecase: What if the user enters a shift that is greater than the number of letters in the alphabet? eg shift number = 45 when divided by 26 the reminder is 19 (45%26=19). so shift will be 19.
  caesar(text, shift, direction)
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    should_continue = False
    print("Goodbye")


# -----------------------------------------------------

# Alternative code for Caesar function is: 

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     if char not in alphabet:
#       end_text += char
#     else:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
    
#   print(f"Here's the {cipher_direction}d result: {end_text}")