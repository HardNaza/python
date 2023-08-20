#######################
## GERADOR DE SENHAS ##
#######################
import string as crct
from secrets import SystemRandom as Pswd

# a-z,A-z,0-9,!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
caracters = crct.ascii_letters + crct.digits + crct.punctuation

config = Pswd().choices

# "k=12" Tamanho da senhas gerada
print(''.join(config(caracters, k=12)))