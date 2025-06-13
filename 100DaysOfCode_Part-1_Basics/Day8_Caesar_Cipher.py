alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  text = list(text)
  for n in range(len(text)):
    letter = text[n]
    position = alphabet.index(letter)
    text[n] = alphabet[position+shift]
    string = "".join(text)
  print(f"The encoded text is {string}")

def decrypt(text, shift):
  text = list(text)
  for n in range(len(text)):
    letter = text[n]
    position = alphabet.index(letter)
    text[n] = alphabet[position-shift]
    string = "".join(text)
  print(f"The decoded text is {string}")

######## Option 2 ############
# def encrypt(text, shift):
#   string = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     newposition = position + shift
#     string += alphabet[newposition]
#   print(f"The encoded text is {string}")


# def decrypt(text, shift):
#   string = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     newposition = position - shift
#     string += alphabet[newposition]
#   print(f"The decoded text is {string}")

    
if direction == "encode":
  encrypt(text,shift)
elif direction == "decode":
  decrypt(text, shift)
