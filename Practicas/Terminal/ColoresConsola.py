print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo")

def construye_tabla_formato():
    for estilo in range(8):
        for colortexto in range(30,38):
            cad_cod =''
            for colorfondo in range(40,48):
                #fmtp 