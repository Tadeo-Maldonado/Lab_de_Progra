import requests
import re
from bs4 import BeautifulSoup as bs
a=0
b=0
c=0

cond=re.compile('Born')
cond1=re.compile('Lotte Giants #+')
cond2=re.compile('Acquired+')

page=requests.get("https://mykbostats.com/players/945-Brooks-Raley-Lotte-Giants")

soup=bs(page.content,"html.parser")

po=soup.find_all() #Busca los parrafos html p = paragraph

for z in range(len(po)):
    potext= po[z].getText()#Obtiene el texto del objeto encontrado
    mo=cond.search(potext)
    if mo == None:
        z=z+1
    else:
        a=a+1
        if a==10:
            w=potext
        else:
            z=z+1
        
for x in range(len(po)):
    potext= po[x].getText()#Obtiene el texto del objeto encontrado
    mo=cond1.search(potext)
    if mo == None:
        x=x+1
    else:
        b=b+1
        if b==7:
            q=potext
        else:
            x=x+1

for v in range(len(po)):
    potext= po[v].getText()#Obtiene el texto del objeto encontrado
    mo=cond2.search(potext)
    if mo == None:
        v=v+1
    else:
        c=c+1
        if c==10:
            e=potext
        else:
            v=v+1
        

print("Este codigo saca algunas estadisticas del jugador Brooks Raley de Lotte Giants")
print(q)
print(w)
print(e)
