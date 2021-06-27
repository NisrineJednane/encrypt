alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
user_choice = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
user_text = input("Type your text:\n")
user_shift = int(input("Type your shift:\n"))

def caesar(text, shift):
  result = ""
  for i in text:
    position = alphabet.index(i)
    if user_choice == "encode":
      i = alphabet[position+shift]
      result+=i
    if user_choice == "decode":
      i = alphabet[position-shift]
      result += i
  print(result)


caesar(text=user_text, shift=user_shift)
