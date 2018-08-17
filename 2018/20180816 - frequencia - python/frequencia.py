def calcula(d,f,r):
    faltas_maximo = d * 0.25
    faltas_atuais = d-r-f
    faltas_restantes= int(faltas_maximo-faltas_atuais)

    if (faltas_atuais > faltas_maximo):
        return "sem chance"
    if (faltas_atuais >=d*0.23):
        return "soh um milagre"
    return "tranquilo pode faltar "+str(faltas_restantes)+ " dias"
