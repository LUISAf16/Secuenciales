""""
Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura.
La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El
algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área
del rectángulo es: yyyy
"""
#Declarar variables base y altura 
base = 10
altura = 15

#Calcular el perimetro del rectangulo Formula: Perímetro = 2 * (base + altura)
perimetro = 2 * (base + altura)
#Calcular el area del rectangulos Formula: Base * Altura 
area = base * altura

#Utilizamos una f-string para insertar el mensaje con los resultados 
print (f"el perimetro del rectangulo es: {perimetro} el area del rectangulo es: {area}")