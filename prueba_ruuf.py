def max_paneles(W: int|float, H: int|float, w: int|float, h: int|float) -> int:
    """
    W: Ancho del rectángulo grande
    H: Largo del rectángulo grande
    w: Ancho del rectángulo pequeño
    h: Largo del rectángulo pequeño
    W, H, h, w son ancho y largo de referencia. No hay restricción de que W > H o w > h.
    Devuelve el (casi) máximo número de rectángulos de tamaño (w,h)
    que se pueden teselar en un rectángulo de tamaño (W,H)
    Se permiten solo orientaciones con rotación en 90°.
    Los paneles son puestos de derecha a izquierda, de arriba a abajo.
    """

    paneles_puestos = 0
    
    # Probar sin rotar el rectángulo pequeño (w x h)
    if w <= W and h <= H:
        # Calculamos cuántos nos caben a lo ancho y a lo largo en esta orientación.
        cuantos_caben_ancho = W // w
        cuantos_caben_largo = H // h

        # Volvemos a calcular cuantos nos caben en el espacio sobrante de abajo y de la derecha
        # De caber más entraran en la orientación rotada en el siguiente llamado a la función
        sobrante_derecha = max_paneles(W - (w * cuantos_caben_ancho), H, w, h)
        sobrante_abajo = max_paneles(W, H - (h * cuantos_caben_largo), w, h)

        # Vemos cuántos paneles caben en total en esta orientación
        paneles_puestos = cuantos_caben_ancho * cuantos_caben_largo + sobrante_derecha + sobrante_abajo
    
    # 2) Probar con el rectángulo pequeño rotado (h x w)
    if h <= W and w <= H:
        # Igual que el paso 1), pero intercambiando w por h
        cuantos_caben_ancho = W // h
        cuantos_caben_largo = H // w

        # Volvemos a calcular cuantos nos caben en el espacio sobrante
        # De caber más entraran en la orientación rotada en el siguiente llamado a la función
        sobrante_derecha = max_paneles(W - (h * cuantos_caben_ancho), H, w, h)
        sobrante_abajo = max_paneles(W, H - (w * cuantos_caben_largo), w, h)

        # Vemos si nos caben más paneles en esta orientación o en la orientación original. 
        paneles_puestos = max(paneles_puestos, cuantos_caben_ancho * cuantos_caben_largo + sobrante_abajo + sobrante_derecha)
    return int(paneles_puestos)
    
if __name__ == "__main__":
    #probamos casos grandes
    print(max_paneles(500001, 500001, 2, 2))     # Debería dar 62500000000
    print(max_paneles(500, 2, 2, 2))      # Debería dar 250

    #caso borde de techo angosto con panel más ancho
    print(max_paneles(500, 1, 2, 2))      # Debería dar 0

    #caso borde de disminución de tamaño del area restante. 
    print(max_paneles(4, 4, 1, 3))     # Debería dar 5
    print(max_paneles(3.99, 4, 1, 3))  # Debería dar 4

    #casos de prueba permutando el orden en que se presenta el techo y panel.
    print(max_paneles(5, 3, 2, 1))     # Debería dar 7
    print(max_paneles(5, 3, 1, 2))     # Debería dar 7
    print(max_paneles(3, 5, 2, 1))     # Debería dar 7
    print(max_paneles(3, 5, 1, 2))     # Debería dar 7
    print(max_paneles(8, 5, 3, 2))     # Debería dar 6
    print(max_paneles(8, 5, 2, 3))     # Debería dar 6
    print(max_paneles(5, 8, 3, 2))     # Debería dar 6
    print(max_paneles(5, 8, 2, 3))     # Debería dar 6

    #casos de prueba del enunciado
    print(max_paneles(2, 4, 1, 2))    # Debería dar 4
    print(max_paneles(3, 5, 1, 2))    # Debería dar 7
    print(max_paneles(10, 1, 2, 2))     # Debería dar 0

    #caso de prueba adicionale
    print(max_paneles(7, 3, 2, 2))    # Debería dar 3
