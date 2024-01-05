from bs4 import BeautifulSoup
import requests

def scrap_dolar_hoy():
    website = 'https://dolarhoy.com/'
    result = requests.get(website)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    dolBluebox = soup.find('div', {'class': 'tile is-child'})
    compraBlueBox = dolBluebox.find('div', {'class': 'compra'})
    valorCompraBlue = (compraBlueBox.find('div', {'class': 'val'})).get_text()

    res = f'El valor de compra del dolar blue es: {valorCompraBlue}'
    print(res)
    
    return res