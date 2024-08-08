#Se declara la variable valorcompra,Se declara la variable valordescuen, Se declara la variable descuento restando la variable valorcompra menos la variable valordescuen y finalmente se muestra el resultado mediante print concatenando la variable valorcompra , valordescuen y descuento

# Se declara la variable valorcompra
valor_compra = int(input(" ingrese el valor de la compra"))
# Se declara la variable valordescuen
valor_descuen = int(input(" ingrese el valor del descuento"))
# Se declara la variable descuento restando la variable valorcompra menos la variable valordescuen
descuento =  valor_compra - valor_descuen
# se muestra el resultado mediante print concatenando la variable valorcompra , valordescuen y descuento
print (" La compra fue de : ", valor_compra, " con un descuento de:", valor_descuen, " y el valor final al pagar es de:", descuento)