### ejercico 17 tienda descuento

total = float(input("El total de la compra: "))

desc = (total*15) / 100

total_a_pagar = int(total - desc)

print(f"Debera pagar: ${total_a_pagar:.2f}")
