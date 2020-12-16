# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:51:00 2020

@author: Dani
"""
import sqlite3


usuarios = open("usuarios.txt","rt",encoding='utf8')
datos_usuarios = usuarios.read()
  

claves = open("claves.txt","rt",encoding='utf8')
datos_claves = claves.read()

codigo = open("codigo.txt","rt",encoding='utf8')
datos_codigo = codigo.read()

precio = open("precio.txt","rt",encoding='utf8')
datos_precio = precio.read()

nombre = open("nombre.txt","rt",encoding='utf8')
datos_nombre = nombre.read()

conexion = sqlite3.connect("ventas.db")


print( f" {datos_usuarios}")

# cursor1 = conexion.cursor()
# cursor1.execute(""" CREATE TABLE USUARIO(
#                     idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
#                     usuario TEXT, 
#                     clave INTEGER)
#                 """)
                
# cursor2 = conexion.cursor()
# cursor2.execute(""" CREATE TABLE PRODUCTO(
#                     idproducto INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     nombre TEXT, 
#                     codigo INTEGER,
#                     precio INTEGER)
#                 """)

lista_usuarios = datos_usuarios.split() 
lista_claves = datos_claves.split()
lista_nombre = datos_nombre.split() 
lista_codigo = datos_codigo.split()
lista_precio = datos_precio.split() 


lista_final = []
for usuario,clave in zip(lista_usuarios, lista_claves):
    lista_final.append((usuario,clave))
    print(usuario)
    print(clave)
    
print(lista_final)


lista_final2 = []
for nombre,codigo,precio in zip(lista_nombre, lista_codigo, lista_precio):
    lista_final2.append((nombre,codigo,precio))

    
print(lista_final2)
cursor = conexion.cursor()
# consulta_usuario = """ INSERT INTO USUARIO(USUARIO, CLAVE)
#                     VALUES(?,?)
#                 """
# cursor.executemany(consulta_usuario, lista_final)
consulta_producto = """ INSERT INTO PRODUCTO(NOMBRE,CODIGO,PRECIO)
                    VALUES(?,?,?)
                """
cursor.executemany(consulta_producto, lista_final2)
conexion.commit()
conexion.close()