def menor_cantidad(n):
    # Verifica que el valor no sea negativo
    if n < 0:
        return None, None

    monedas = [50, 100, 200, 500, 1000]

    # dp[monto] guarda la menor cantidad de monedas necesarias para formar ese monto.
    dp = [float("inf")] * (n + 1)
    dp[0] = 1

    # Guarda cuál moneda se usó para cada monto.
    ultima_moneda = [-1] * (n + 1)

    # Programación dinámica
    for monto in range(1, n + 1):
        for moneda in monedas:
            if moneda <= monto and dp[monto - moneda] != float("inf"):
                cantidad_posible = dp[monto - moneda] + 1

                # Si esta opción usa menos monedas, se guarda
                if cantidad_posible < dp[monto]:
                    dp[monto] = cantidad_posible
                    ultima_moneda[monto] = moneda

    # Si no se puede completar exactamente el cambio
    if dp[n] == float("inf"):
        return None, None

    # Reconstruir las monedas que se deben entregar
    monedas_usadas = []
    monto = n

    while monto > 0:
        moneda = ultima_moneda[monto]
        monedas_usadas.append(moneda)
        monto -= moneda

    return dp[n], monedas_usadas


def main():
    n = int(input("Ingrese el valor del cambio: "))

    cantidad, monedas_usadas = menor_cantidad(n)

    if cantidad is None:
        print("No es posible entregar el cambio exacto.")
    else:
        print("Monedas que se deben entregar:", monedas_usadas)
        print("Cantidad mínima de monedas:", cantidad)


main()