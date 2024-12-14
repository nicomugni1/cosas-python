
porcentaje_dalto = 1.5
curso_minimo = 2.5
curso_maximo = 7
curso_promedio = 4

crudo_promedio = 3.5
crudo_maximo = 5

curso_10 = 10

#punto a 
#diferencia entre el "porcentaje_dalto" y el mas rapido
dif_time_min = round(float(100 - porcentaje_dalto / curso_minimo * 100), 2)
#diferencia entre el "porcentaje_dalto" y el mas lento
dif_time_max = round(float(100 - porcentaje_dalto / curso_maximo * 100), 2)
#diferencia entre el "porcentaje_dalto" y el mas promedio
dif_time_pro = round(float(100 - porcentaje_dalto / curso_promedio * 100), 2)

#punto b

dif_time_crudo = round(float(100 - curso_promedio * 1000 / crudo_maximo / 10), 2)
dif_time_crudo2 = round(float(100 - porcentaje_dalto * 1000 / crudo_promedio / 10), 2)

#punto c


print(f"Time min: {dif_time_min}, Time max: {dif_time_max}, Time pro: {dif_time_pro}")

print(f"Reduccion 1: {dif_time_crudo}, Reduccion 2: {dif_time_crudo2}")

print("Ver 10 horas: ", curso_promedio * 100 // porcentaje_dalto / 10)
print("Al reves: ", porcentaje_dalto * 100 // curso_promedio / 10)