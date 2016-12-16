#jaime paredes mora
#programa5
segundos=input("introdusca segundos: ")
dias=(segundos/86400)
horas=((segundos-(dias*86400))/(60*60))
minutos=(segundos-(dias*86400)-(horas*(60*60)))/60
segundos=(segundos-(dias*86400)-(horas*(60*60))-(minutos*60))
print (dias,horas,minutos,segundos)
