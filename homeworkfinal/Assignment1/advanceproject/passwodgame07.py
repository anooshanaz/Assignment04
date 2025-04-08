
import random
import string

use_input = int(input("Enter your paswword length:"))

generate_password =''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=use_input))
print(f"Your generated password is: {generate_password}")