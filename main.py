# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra,
# y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los
# productos de la cesta y devolver el precio final de la cesta.

# {50:20, 30:5, 45:10}

def discount(price, percentaje):
    return price-(price/100)*percentaje

def iva(precie, percentaje):
    return (precie/100)*16 #el 16 es el iba, el cual es un valor fijo

def ticket(basket, funcion): #basket es el diccionario donde van a estar almacenados los productos con su descuento respectivo
    total = 0
    for precie, percentaje in basket.items():
        total += funcion(precie, percentaje)

    return total

print("El iva es: "+ str(ticket({50:20, 30:5, 45:10}, iva)))
print("El total sin descuento es: "+ str(ticket({50:20, 30:5, 45:10}, discount)))
print("El total es: "+ str(ticket({50:20, 30:5, 45:10}, discount)+ticket({50:20, 30:5, 45:10}, iva) ))