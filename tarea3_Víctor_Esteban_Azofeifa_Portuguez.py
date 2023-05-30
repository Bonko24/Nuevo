#Ejercicio 1
#El próposito de la función es pasar una nota número a una alfabética, en el proceso determinando si un estudiante aprobo o reprobó..
#ENTRADA: La nota
#SALIDA: La calificación alfabética (A, B, C, D o F) del estudiante y si aprobo o reprobó el curso. 
def calificacion(nota):
#La nota debe ser un número natural y debe estar entre 0 y 100.
    if nota < 0 or nota > 100:
        return "ERROR: NOTA DEBE ESTAR ENTRE 0 Y 100." #La nota debe estar entre 0 y 100.
    if nota >= 90 or nota == 100:
        return "A - Excelente (Aprobado)"
    if nota >= 80 or nota == 89:
        return "B - Bien (Aprobado)"
    if nota >= 70 or nota == 79:
        return "C - Suficiente (Aprobado)"
    if nota >= 50 or nota == 69:
        return "D - Deficiente (Reprobado)"
    if nota >= 0 or nota == 49:
        return "F - Muy deficiente (Reprobado)"
    

#Ejercicio 2
#El propósito de esta función es clasificar los dígitos de un número natural de cuatro dígitos en pares e impares.
#ENTRADA: Número natural de cuatro dígitos.
#SALIDAS: Dos números, un compuesto por los números pares y el otro por los impares, en este orden respectivamente, de no haber pares o impares la función digitará un -1.
def pares_impares(num):
    unidades = num%10
    cociente1 = num//10
    decenas = cociente1%10
    cociente2 = cociente1//10
    centenas = cociente2%10
    millares = cociente2//10
    if num > 9999 or num < 1000:
        return "ERROR: DEBE SER UN NÚMERO NATURAL DE CUATRO DÍGITOS."
# Casos de -1 y un número de cuatro dígitos. 
    if (unidades%2) == 0 and (decenas%2) == 0 and (centenas%2) == 0 and  (millares%2) == 0:
        return (num, -1)
    if (unidades%2) != 0 and (decenas%2) != 0 and (centenas%2) != 0 and  (millares%2) != 0:
        return (-1, num)
# Casos de un número de tres dígitos y uno de un dígito.
    #Millares:
    if (millares%2) == 0 and (centenas%2) != 0 and (decenas%2) != 0 and  (unidades%2) != 0:
        return (millares, centenas*100 + decenas*10 + unidades)
    if (millares%2) != 0 and (centenas%2) == 0 and (decenas%2) == 0 and  (unidades%2) == 0:
        return (centenas*100 + decenas*10 + unidades, millares)
    #Centenas
    if (centenas%2) == 0 and (millares%2) != 0 and (decenas%2) != 0 and  (unidades%2) != 0:
        return (centenas, millares*100 + decenas*10 + unidades)
    if (centenas%2) != 0 and (millares%2) == 0 and (decenas%2) == 0 and  (unidades%2) == 0:
        return (millares*100 + decenas*10 + unidades, centenas)
    #Decenas
    if (decenas%2) == 0 and (millares%2) != 0 and (centenas%2) != 0 and  (unidades%2) != 0:
        return (decenas, millares*100 + centenas*10 + unidades)
    if (decenas%2) != 0 and (millares%2) == 0 and (centenas%2) == 0 and  (unidades%2) == 0:
        return (millares*100 + centenas*10 + unidades, decenas)
    #Unidades
    if (unidades%2) == 0 and (millares%2) != 0 and (centenas%2) != 0 and  (decenas%2) != 0:
        return (unidades, millares*100 + centenas*10 + decenas)
    if (unidades%2) != 0 and (millares%2) == 0 and (centenas%2) == 0 and  (decenas%2) == 0:
        return (millares*100 + centenas*10 + decenas, unidades)
# Casos de números de dos dígitos
    #Casos millares y otro número par:
    if (millares%2) == 0 and (centenas%2) == 0 and (decenas%2) != 0 and  (unidades%2) != 0:
        return (millares*10 + centenas, decenas*10 + unidades)
    if (millares%2) == 0 and (centenas%2) != 0 and (decenas%2) == 0 and  (unidades%2) != 0:
        return (millares*10 + decenas, centenas*10 + unidades)
    if (millares%2) == 0 and (centenas%2) != 0 and (decenas%2) != 0 and  (unidades%2) == 0:
        return (millares*10 + unidades, centenas*10 + decenas)
    #Casos centenas y otro número par:
    if (millares%2) != 0 and (centenas%2) == 0 and (decenas%2) == 0 and  (unidades%2) != 0:
        return (centenas*10 + decenas, millares*10 + unidades)
    if (millares%2) != 0 and (centenas%2) == 0 and (decenas%2) != 0 and  (unidades%2) == 0:
        return (centenas*10 + unidades, millares*10 + decenas)
    #Caso decenas y unidades número par:
    if (millares%2) != 0 and (centenas%2) != 0 and (decenas%2) == 0 and  (unidades%2) == 0:
        return (decenas*10 + unidades, millares*10 + centenas)
    

#Ejercicio 3 
#Esta función establece si un año determinado es bisiesto o no.
#ENTRADAS: Un año desde 1800 en adelante.
#SALIDAS: True si es bisiesto, False si no lo es.
def bisiesto(año):
    #Solo se trabaja con números naturales de cuatro dígitos.
    if año < 1800 or año > 9999:
        return False
    #La condiciones para ser bisiesto son: divisible entre 4 y 400, por este último es que no todos los divisbles entre 100 entran en la categoría de bisiestos.
    if (año%4) == 0 and ((año%100) != 0 or (año%400) == 0):
        return True
    else:
        return False

#Ejercicio 4 
#Esta función determina si una fecha es válida o no, tomando en cuenta su mes, cantidad de días, que el año sea bisisesto o no y que sea un año después de 1800.
#ENTRADA: El año
#SALIDA: True si la fecha es válida, si no False.
def valida_fecha (fecha):
#Se divide la fecha en año, mes y día.
    dia = fecha//1000000
    fecha = fecha%1000000
    mes = fecha//10000
    año = fecha%10000
#El año debe ser desde 1800 en adelante y para que la fecha se mantenga de la forma ddmmaaaa, debe ser de cuatro dígitos. 
    if año < 1800 or año > 9999:
        return False
#Meses de 31 días: Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre.
    if dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return True
#Meses con 30 días: Abril, Junio, Setiembre y Noviembre.
    if dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return True
#Caso de Febrero: Se reutiliza la función bisiesto(año) para determinar si el año es bisiesto o no y así saber si este mes tendrá 28 ó 29 días.
    if bisiesto(año) == True and mes == 2 and dia <= 29:
        return True
    if bisiesto(año) == False and mes ==2 and dia <=28:
        return True
    else:
        return False

#Ejercicio 5:
#Esta función debe clasificar la paridad de dos número para saber si su paridad mutua es par, impar o diferente una de la otra.
#ENTRADA: Dos número enteros.
#SALIDA: Si sus paridades coinciden (si es imparidad par o impar) o si difieren.
def paridad(num1, num2):
#Los números se dividen entre 2, si es par se define como True y si es impar False.
    if (num1%2) == 0:
        par1 = True
    else:
        par1 = False   
    if (num2%2) == 0:
        par2 = True   
    else:
        par2 = False
    if par1 == True and par2 == True:
        return "Paridad par"
    if par1 == False and par2 == False:
        return "Paridad impar"
    if par1 != par2:
        return "DIFERENTE PARIDAD"

#Ejercicio 6:
#La función identifica si el número natrual que se digite es el doble de un número impar.
#ENTRADA: Un número natural.
#SALIDA: True si es doble de un impar o False en caso de lo contrario.
def doble_de_impar(num):
    mitad = num//2
    if (mitad%2) != 0:
        return True
    else:
        return False

#Ejercicio 7:
#Esta función determina la cantidad de dinero que queda en una cuenta bancaria después de hacer un retiro o un depósito.
#ENTRADAS: El saldo que tiene la cuenta, la operación que se realizará (1: depósito ó 2: retiro) y la cantidad de dinero que se retira o se deposita.
#SALIDA: El nuevo saldo de la cuenta.
def cuenta_bancaria(saldo, operacion, cantidad):  
#Condición 1: Cantidad múltiplo de 1000.
    if (cantidad%1000) != 0:
        return False
#Condición 2: La operación no puede ser un número distinto de 1 o 2. La primer condición cubre los número menores que 1 y mayores que 2 y la segunda cubre a los número decimales entre 1 y 2.
    if operacion < 1 or operacion > 2:
        return False
    if operacion > 1 and operacion < 2:
        return False
#Condición 3: El saldo ni la cantidad puede ser menores a cero. 
    if saldo < 0 or cantidad <= 0:
        return False
    if operacion == 1:
        return saldo + cantidad
    if operacion == 2:
#Como se está realizando un retiro la cantidad no puede ser mayor al saldo.
        if cantidad > saldo:
            return False
        else:
            return saldo - cantidad

#Ejercicio 8:
#Esta función tiene como proósito determinar cuánto tiene que pagar una persona por su celular, considerando los mensajes que envía, los minutos que consume y su plan de internet.
#ENTRADAS: Cantidad de minutos consumindos, cantidad de mensajes enviados y el plan aquirido.
#SALIDAS: La cantidad de dinero que debe paragar la persona.
def pago_celular(minutos, mensajes, plan):
    if minutos < 0 or mensajes < 0:
        return "ERROR: CANTIDAD DE MENSAJES Y MINUTOS DEBE SER MAYOR O IGUAL A CERO."
#Estas condiciones hacen que no se pueda poner ningún que no sea 0, 1, 2 ó 3.
    if plan < 0 or plan > 3:
        return "ERROR: PLAN ELIJA PLAN ENTRE 0 Y 3"
    if plan > 0 and plan < 1:
        return "ERROR: PLAN ELIJA PLAN ENTRE 0 Y 3"
    if plan > 1 and plan < 2:
        return "ERROR: PLAN ELIJA PLAN ENTRE 0 Y 3"
    if plan > 2 and plan < 3:
        return "ERROR: PLAN ELIJA PLAN ENTRE 0 Y 3"
#Tarifa básica.
    if minutos <= 60:
        tarifa = 2750
#Tarifa +60 minutos a 120 minutos.
    if minutos > 60 and minutos < 121:
        minutos -= 60
        tarifa = 2750 + minutos*50
#Tarifa +120 minutos.
    if minutos >= 121:
        minutos -= 60
        tarifa = 2750 + minutos*50
        minutos -= 60
        tarifa = tarifa + minutos*35
#Se le suma el costo de los mensajes a la tarifa.
    tarifa += mensajes*3
    if plan == 0:
        tarifa += 0
    if plan == 1:
        tarifa += 12000
    if plan == 2:
        tarifa += 15000
    if plan == 3:
        tarifa += 25000
#Se añade el impesto de venta (13% de la tarifa calculada) más 200 colones para la Cruz Roja.
    tarifa += tarifa*0.13 + 200
    return tarifa

#Ejercicio 9:
#Esta función se encarga de determinar el día de la semana que una determinada fecha representa.
#ENTRADA: Una fecha en la fomra ddmmaaaa, d = día, m = mes y a = año
#SALIDA: El día de la semana que representa la fecha.
def nombre_dia(fecha):
    dia = fecha//1000000
    fecha = fecha%1000000
    mes = fecha//10000
    año = fecha%10000
#Se reusa la programación del ejercicio 4, para determinar si es una fecha válida con la que se ouede trabajar y se hacen unos cambios para que en vez de retornar el resultado, solo cambie el valor de fecha.
#El año debe ser de cuatro dígitos para que la fecha se mantenga de la forma ddmmaaaa, debe ser de cuatro dígitos. 
    if año > 9999:
        return False
#Meses de 31 días: Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre.
    if dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        fecha = True
#Meses con 30 días: Abril, Junio, Setiembre y Noviembre.
    if dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        fecha = True
#Caso de Febrero: Se reutiliza la función bisiesto(año) para determinar si el año es bisiesto o no y así saber si este mes tendrá 28 ó 29 días.
    if bisiesto(año) == True and mes == 2 and dia <= 29:
        fecha = True
    if bisiesto(año) == False and mes == 2 and dia <= 28:
        fecha = True
#Se hace uso del algoritmo de Zeller.
    if fecha == True:
        if mes == 1 or mes == 2:
#Se hace este cambio ya que para Enero y Febrero se usan los números 13 y 14 respectivamente y se toma el año pasado para hacer la operación.
            año -= 1
            mes += 12
        dia_semana = (dia + (mes+1)*26//10 + año%100 + año%100//4 + año//100//4 -2*(año//100))%7
        if dia_semana == 0:
            return "Sábado"
        if dia_semana == 1:
            return "Domingo"
        if dia_semana == 2:
            return "Lunes"
        if dia_semana == 3:
            return "Martes"
        if dia_semana == 4:
            return "Miércoles"
        if dia_semana == 5:
            return "Jueves"
        if dia_semana == 6:
            return "Viernes"
    else:
        return False

#Ejercicio 10
#Esta función determina si un número es palíndromo o no, es decir, que se pueda leer igual al derecho y al revés.
#ENTRADA: Un número natrual de 4 dígitos.
#SALIDA: True si es un número palíndromo o False si no lo es.

#Se va a reutlizar la función al_reves(numero), desarrollada en otro trabajo.
def al_reves(numero):
    unidades = numero%10
    decenas = numero//10%10
    centenas = numero//10//10%10
    millares = numero//10//10//10
    reverso = unidades*1000+decenas*100+centenas*10+millares
    return(reverso)

def es_palindromo(numero):
    reves = al_reves(numero)
    if reves == numero:
        return True
    else:
        return False


                



