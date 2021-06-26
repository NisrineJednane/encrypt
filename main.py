alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

user_choice = (input("Type 'encode' to encrypt text. Type 'decode' to decrypt text.\n")).lower()
user_text = input("Type your text:\n")
user_shift = int(input("Type your shift:\n"))


def encode(text, shift):
  result = ""
  for letter in text:
    letter_position = alphabet.index(letter)
    coded_position = letter_position + shift
    new_letter = alphabet[coded_position]
    result+=new_letter
  print(f"The encrypted text is {result}")


def decode(text, shift):
  result = ""
  for letter in text:
    letter_position = alphabet.index(letter)
    coded_position = letter_position - shift
    new_letter = alphabet[coded_position]
    result+=new_letter
  print(f"The decrypted text is {result}")


if user_choice == "encode":
  encode(text=user_text, shift=user_shift)
if user_choice == "decode":
  decode(text=user_text, shift=user_shift)
  
