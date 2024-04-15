#Gerador de Senha
import secrets
import string

def create_pw(pw_length=12):
   all_characters = string.ascii_letters + string.digits + string.punctuation
   while True:
       pw = ''.join(secrets.choice(all_characters) for i in range(pw_length))
       if (any(c.islower()) and any(c.isupper()) and any(c.isdigit()) and any(c in string.punctuation)
               for c in pw):
           return pw

print(create_pw())