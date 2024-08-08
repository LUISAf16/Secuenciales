""""
Desarrolle un algoritmo que permita calcular nota final de algoritmia de un estudiante dadas las
siguientes apreciaciones:
• Actividades en clase equivalen a un porcentaje de 30%
• Proyecto final 50%
• Evaluaciones parciales 20%
"""
# Declarar la variable para el nombre del estudiante
nombre_estudiante = "Carlos Ruiz" 

# Declarar la variable para la calificación promedio de las actividades en clase
calificacion_actividades = 85.0 

# Declarar la variable para la calificación del proyecto final
calificacion_proyecto = 90.0  

# Declarar la variable para la calificación promedio de las evaluaciones parciales
calificacion_evaluaciones = 80.0  

# Calcular la nota final
# Fórmula: nota_final = (calificacion_actividades * 0.30) + (calificacion_proyecto * 0.50) + (calificacion_evaluaciones * 0.20)
nota_final = (calificacion_actividades * 0.30) + (calificacion_proyecto * 0.50) + (calificacion_evaluaciones * 0.20)

# Imprimir el nombre del estudiante y la nota final
print(f"El estudiante {nombre_estudiante} tiene una nota final de: {nota_final}")
