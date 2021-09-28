def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    Altura =float(input("Altura en m: "))
    if peso == 0 or Altura == 0:
        print ("Revisa tus datos, alguno de ellos es erróneo.")
    else :
        imc=peso/ Altura**2
        if  imc < 20:
            print ("PESO BAJO")
        elif 20 <= imc < 25:
            print("NORMAL")
        elif 25 <= imc < 30:
            print("SOBREPESO")
        elif 30 <= imc < 40:
            print("OBESIDAD")
        else:
            print("OBESIDAD MORBIDA")

if __name__=='__main__':
    main()