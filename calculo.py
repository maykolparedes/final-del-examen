def calcular(precio:int,cantidad:int):
    total = precio * cantidad
    igv = total * 0.18
    subtotal = total - igv
    return total, igv, subtotal
