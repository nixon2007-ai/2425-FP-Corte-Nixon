#Definicion de una funcion vamos a calcular el descuento conjuntamente con el porcentaje de 10%
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función con solo el monto total
    monto1 = 2500  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1

    print(f"Monto total: {monto1}")
    print(f"Descuento: {descuento1}")
    print(f"Monto final a pagar: {monto_final1}")

    # Segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 2100  # Monto total de la compra
    porcentaje2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2

    print(f"\nMonto total: {monto2}")
    print(f"Descuento: {descuento2}")
    print(f"Monto final a pagar: {monto_final2}")
