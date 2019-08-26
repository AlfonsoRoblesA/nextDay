# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:31:20 2019

@author: Alfonso
"""

def readMonth():
    """ Solicita un valor entero para determinar el mes"""
    while True:
        valor = input("Ingrese el mes: ")
        try:
            valor = int(valor)
            if valor >= 1 and valor <= 12:
                return valor
            else:
                print("Error: Debe ingresar un numero entre 1 y 12")
        except ValueError:
            print("Error: Debe ingresar un número entero.")


def readDay():
    """ Solicita un valor entero para determinar el dia"""
    while True:
        valor = input("Ingrese el dia: ")
        try:
            valor = int(valor)
            if valor >= 1 and valor <= 31:
                return valor
            else:
                print("Error: Debe ingresar un numero entre 1 y 31")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            

            
def readYear():
    """ Solicita un valor entero para determinar el año"""
    while True:
        valor = input("Ingrese el año: ")
        try:
            valor = int(valor)
            if valor >= 1812 and valor <= 2020:
                return valor
            else:
                print("Error: Debe ingresar un año entre 1812 y 2020")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            

def validate(day,month,year):
    """ Valida si la fecha dada es correcta o no existe """
    if month == 4 or month == 6 or month == 9 or month == 10:
        if day <= 30:
            return True
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day <= 29:
                return True
        if day <= 28:
            return True
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31:
            return True
    return False

def nextDay(day, month, year):
    newDay = day + 1
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        if newDay > 31:
            month = month + 1
            newDay = 1
            print ("La nueva fecha es: " , newDay , "/" , month , "/" , year)
            return 0
    if month == 4 or month == 6 or month == 9 or month == 10:
        if newDay > 30:
            month = month + 1
            newDay = 1
            print ("La nueva fecha es: " , newDay , "/" , month , "/" , year)
            return 0
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if newDay > 29:
                month = month + 1
                newDay = 1
                print ("La nueva fecha es: " , newDay , "/" , month , "/" , year)
            else:
                print ("La nueva fecha es: " , newDay , "/" , month , "/" , year)
            return 0
        if newDay > 28:
            month = month + 1
            newDay = 1
            print ("La nueva fecha es: " , newDay , "/" , month , "/" , year)
            return 0
    if month == 12:
        if day > 31:
            newDay = 1
            month = 1
            year = year + 1
            print ("La nueva fecha es: " , newDay , "/" , month , "/" , year)
            return 0
    print ("La nueva fecha es: " , newDay , "/" , month , "/" , year)
    
def mainFun(dia, mes, anio):
    if validate(dia,mes,anio):
         nextDay(dia,mes,anio)
    else:
        print("No es una fecha valida")
        
        
dia = readDay()
mes = readMonth()
anio = readYear()

mainFun(dia,mes,anio)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            