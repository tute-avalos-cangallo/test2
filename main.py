"""
    Este es mi programa
    Prof. Matías Ávalos (@tute-avalos-cangallo)
"""

def fibo(c : int) -> str:
    """Muestra una cantidad de dígitos de la serie de fibonacci

    Args:
        c (int): cantidad de elementos a mostrar
    """
    if c < 0:
        raise ValueError("No se admiten valores negativos")
    a, b = 1, 1
    sf = ""
    for _ in range(c):
        sf = sf + f"{b}, "
        a, b = a+b, a
    return sf


if __name__ == "__main__":
    pass