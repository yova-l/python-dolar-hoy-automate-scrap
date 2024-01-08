from dolar_parser import scrap_dolar_hoy
import constants
from whatsapp_utils import send_dolar_notif, send_dolar_notif_vir

if __name__ == "__main__":
    money_exchange = scrap_dolar_hoy()

    for dollar in constants.DH_DOLLARS:
        dol_val_sell = money_exchange.get_value(dollar, constants.SELL_ARR_POS)
        send_dolar_notif(dollar, constants.DH_SELL, dol_val_sell)
        
        if dollar == constants.DH_TARJETA: 
            continue

        dol_val_buy = money_exchange.get_value(dollar, constants.BUY_ARR_POS)
        send_dolar_notif(dollar, constants.DH_BUY, dol_val_buy)

        if dollar == constants.DH_BLUE:
            send_dolar_notif_vir(dollar, constants.DH_SELL, dol_val_sell)
            send_dolar_notif_vir(dollar, constants.DH_BUY, dol_val_buy)

        
