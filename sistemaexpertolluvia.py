def sistema_experto_clima():
    lluvia = input("¿Esta lloviendo quieres comer? (s/n): ").lower() == 's'
    frio = input("¿Esta haciendo frio, quieres una bebida caliente? (s/n): ").lower() == 's'

    if lluvia and frio:
        return "Llevo empanadas y cafe"
    elif lluvia and not frio:
        return "Llevo empanadas"
    elif not lluvia and frio:
        return "Llevo cafe"
    else:
        return "Hay un excelente dia."

print(sistema_experto_clima())
#imagen Sistema experto de comida en cambios de clima Jefer Cuetia Y el Camilo Castro