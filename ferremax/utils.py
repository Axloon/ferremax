import bcchapi
from decimal import Decimal
from datetime import datetime, timedelta

def get_clp_to_usd():
    siete = bcchapi.Siete("Maximofuentes2017@gmail.com", "Luiscruzmartines1617")

    hoy = datetime.now()

    if hoy.weekday() == 5:
        hoy -= timedelta(days=1)
    elif hoy.weekday() == 6:
        hoy -= timedelta(days=2)

    hoy = hoy.strftime('%Y-%m-%d')

    try:
        serie = siete.get("F073.TCO.PRE.Z.D", hoy, hoy)
        clp_to_usd = Decimal(serie.Series['Obs'][0]['value'])
        return clp_to_usd
    except Exception as e:
        print(f"Error al obtener el tipo de cambio: {e}")
        return None

def clp_to_usd_conversion(clp_amount):
    clp_to_usd = get_clp_to_usd()
    if clp_to_usd:
        usd_amount = clp_amount / clp_to_usd
        return usd_amount
    else:
        return None

def usd_to_clp_conversion(usd_amount):
    clp_to_usd = get_clp_to_usd()
    if clp_to_usd:
        clp_amount = usd_amount * clp_to_usd
        return int(clp_amount)
    else:
        return None
