# EX4 
import string
import random






def custom_errors():
  val = input("Enter a value btween 1 and 9 ")
  while val !="quit":
      if val <'1' or val > '9':
        raise ValueError("Value should be btween 1 and 9")
      else: print(f"the number you enterd was {val}") 
  else : print("you quit")



# try :
#   l = [1,2,3,4,5]
#   i = int(input("Enter th index you need : "))
#   print(l[i])
# except:
#   print("Some error occured")

# finally :
#   print("I am always executed")





# def add_random_letters(string, num_letters):
#   """Adds a specified number of random letters to the beginning and end of a string.

#   Args:
#     string: The input string.
#     num_letters: The number of random letters to add.

#   Returns:
#     The modified string with random letters added.
#   """

#   # Generate random letters
#   random_letters = ''.join(random.choices(string.ascii_lowercase, k=num_letters))

#   # Add random letters to the beginning and end of the string
#   modified_string = random_letters + string + random_letters

#   return modified_string

def encoder():

  encoded_sen= ""
  fs =""
  bs= ""
  letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

  print("Welcome to the Encoder ...")
  sen = str(input ("Enter a sentence to encode : "))
  word = ""

  for i in sen:
    if i != " " :
      word = word + i
      
    else :
      
      
      for a in range(3):
        s = random.choice(letter)
        fs = fs + s

      
      for i in range(3):
        s = random.choice(letter)
        bs = bs + s
      
      word = fs + word + bs
      encoded_sen = encoded_sen  + " " + word 
      
      fs = ""
      bs = ""
      word = ""

  print(encoded_sen)
    
