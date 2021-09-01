#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:25:01 2021

@author: jesus
"""
# TALLER #1 PYTHON Y GIT - IA

# 1.
y = (((5+2-5)**2)*((5+8)/(2-30)))/((2*5)-3)
print(f'El resultado es {y}')

# 2.
z = 5
n = 3
m = z-n
y = (((((z+2-n)**2)*((m+8)/(2-30)))/((2*5)-3))**5)+(15*3)-(9/3)
print(f'El resultado es {y}')

# 3.
z = 5
n = (((8+2-4)**2)*((5+8+7)/2)-(30*5))/(2*5-3)
m = (z**2)*(3+n)
y = (((((((z+2-n)**2)*(m+8)/(2-30))/(2*5-3))**5)+(15*3)-(9/3))**2)-5/4
print(f'El resultado es {y}')

# 4.
presión = float(input('Ingrese el valor de la presión: '))
volúmen = float(input('Ingrese el valor del volúmen: '))
temperatura = float(input('Ingrese el valor del temperatura: '))
masa = (presión*volúmen)/(0.37*(temperatura+460))
print(f'El valor de la masa es {masa}')

# 5.
edad = int(input('Ingrese su edad: '))
pulsaciones = (200-edad)/10
print(f'El numero de pulsaciones que debe tener cada 10s es {pulsaciones}')
