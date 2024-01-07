from bs4 import BeautifulSoup
import requests
from classes import MoneyExchange
import constants

# def scrap_blue(soup, operation):
#     dol_blue_box = soup.find('div', {'class': 'tile is-child'})
#     buy_blue_box = dol_blue_box.find('div', {'class': operation})
#     final_val = (buy_blue_box.find('div', {'class': 'val'})).get_text()
#     return final_val

def scrap_dolar(soup, dol_type, operation):
    dol_box_child = soup.find(lambda tag: tag.name == "a" and dol_type in tag.text)
    dol_box_parent = dol_box_child.parent
    dol_final_box = dol_box_parent.find('div', {'class': operation})
    final_val = (dol_final_box.find('div', {'class': 'val'})).get_text()
    return final_val


def scrap_dolar_hoy():
    result = requests.get(constants.WEBSITE)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    money_exchange = MoneyExchange()
    
    for dollar in constants.DH_DOLLARS:
        buy_val = scrap_dolar(soup, dollar, constants.DH_BUY)
        sell_val = scrap_dolar(soup, dollar,constants.DH_SELL)
        money_exchange.set_value(dollar, constants.BUY_ARR_POS, buy_val)
        money_exchange.set_value(dollar, constants.SELL_ARR_POS, sell_val)

    return money_exchange