# !/usr/bin/python
# -*-coding: utf-8-*-
##############################################
#          Llegim les taules         #
##############################################

import os
import sys
import string
import psycopg2    


##############################################
#          Ens connectem a la BBDD           #
##############################################
try:
	conn = psycopg2.connect(database="training", user="postgres", password="jupiter")
	print "DATABASE OPENED SUCCESSFULLY \n"
	
except:
	print "CONNECTION ERROR"
	exit(2)



##############################################
#            Declarem el cursor              #
##############################################
cur = conn.cursor()

os.system('clear')
sortir = False

##############################################
#              Menu principal                #
##############################################
while sortir == False:	
	
	os.system('clear')
	print "OPCIONS \n 1- leer tabla productos : \n 0- Sortir \n"

	opcio = raw_input('Escoge una opción [0-1]: ')
	
    # Comprovem si l'opció és correcta
	if not opcio.isdigit() or not ( int(opcio) >= 0 and int(opcio) <= 1 ):
		os.system('clear')
		print "Opción incorrecta, vuelve a probar \n"
		tecla = raw_input('Presiona una tecla para continuar :')

	else:
		opcio = int(opcio)

    # Sortim
	if opcio == 0:
		print "Adeu! \n"
		sortir = True

	# Leemos la tabla productos
	elif opcio == 1: 
		try:	
			nombre_tabla = raw_input("Indique el nombre de la tabla :")
			sql = "SELECT * FROM " + nombre_tabla + ""

			if nombre_tabla == "productos":
				cur.execute(sql);
				rows = cur.fetchall()
				
				os.system('clear')
				
				colnames = [desc[0] for desc in cur.description]
				print colnames
				
				for row in rows:
					print(" {:^10}   {}   {:^20}{:^1}   {:^15} ".format(row[0], row[1], row[2], row[3], row[4]))

				tecla = raw_input("presiona una tecla para contiuar :")
 			   		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()

##############################################
#        Ens desconnectem de la BBDD         #
##############################################
conn.close()
