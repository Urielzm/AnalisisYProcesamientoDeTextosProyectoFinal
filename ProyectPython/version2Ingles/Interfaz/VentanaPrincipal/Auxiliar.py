from bs4 import BeautifulSoup
import requests

#url = input("Introduce la URL: ")
respuesta = requests.get("https://es.qwe.wiki/wiki/Artificial_intelligence")
datos = respuesta.text
soup = BeautifulSoup(datos, "html.parser")
label = soup.find("label", text="Name:")
print(label.next_sibling.strip())

print(datos)