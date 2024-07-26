from dolar_parser import scrap_dolar_hoy
import constants
from whatsapp_utils import send_full_msg_vir, send_full_msg_yova

if __name__ == "__main__":
    money_exchange = scrap_dolar_hoy()

    final_res = 'Dolar Compra/Venta\n'

    for dollar in constants.DH_DOLLARS:
        dol_val_sell = money_exchange.get_value(dollar, constants.SELL_ARR_POS)

        if dollar == constants.DH_TARJETA:
            final_res += f'{dollar} {dol_val_sell}\n'
            continue

        dol_val_buy = money_exchange.get_value(dollar, constants.BUY_ARR_POS)
        final_res += f'{dollar} {dol_val_buy}/{dol_val_sell}\n'

        if dollar == constants.DH_BLUE:
            send_full_msg_vir(f'El dolar Blue esta {dol_val_buy} para la compra y {dol_val_sell} para la venta')
    
    send_full_msg_yova(final_res)

#Revive the script 2