#Creador intelectual: Gaddiel Zamora Flores
"**********************************************************************************************************************************************************"
#librerias 
import msvcrt as ms
import time as ti
import os

import math as ma 

from colorama import Back, Fore, Style, init
init(autoreset=True)
"**********************************************************************************************************************************************************"
#inicio de sesion
def GZF_sesion(GZF_user,GZF_contra):
    GZF_error = 1
    GZF_ayuda = 0
    GZF_salida = 0
    for i in range(1,3):
        print(Style.BRIGHT + Fore.WHITE + Back.GREEN+ "Para poder acceder al programa primero debe iniciar sesion")
        ti.sleep(1/2)
        os.system('cls')
        print(Style.BRIGHT + Fore.BLUE + Back.WHITE + "Para poder acceder al programa primero debe iniciar sesion")
        ti.sleep(1/2)
        os.system('cls')
        print(Style.BRIGHT + Fore.CYAN + Back.RED + "Para poder acceder al programa primero debe iniciar sesion")
        ti.sleep(1/2)
        os.system('cls')
    print("Introduzca su usuario\n")
    GZF_usuario = str(input("Usuario: "))
    os.system('cls')
    while GZF_error == 1:
        print("Introduzca su contraseña\n")
        GZF_contraseña = str(input("Contraseña: "))
        os.system('cls')
        if GZF_usuario in GZF_user and GZF_contraseña in GZF_contra:
            GZF_perfil = GZF_user.index(GZF_usuario)
            GZF_error = 0
            GZF_ayuda = 0
            GZF_salida = 0
            for i in range(1,11):
                carga = i*"."
                print("Inicio de sesion exitoso.")
                print("Espere mientras carga el sistema"+carga)
                ti.sleep(1/5)
                os.system('cls')
        elif GZF_contraseña not in GZF_contra:
            print("La contraseña ingresada es incorrecta")
            ti.sleep(1)
            os.system('cls')
            GZF_error = 1
            GZF_ayuda += 1
            if GZF_ayuda == 1:
                GZF_help = GZF_contra[GZF_user.index(GZF_usuario)]
                GZF_longitud = len(GZF_help)
                GZF_inicio = GZF_help[0:1]
                GZF_fin = GZF_help[GZF_longitud-1:]
                print("La contraseña del usuario ingresado comienza con: ",GZF_inicio," y termina con",GZF_fin)
                print("y debe tener una longitud de ",GZF_longitud," caracteres")
                print("Intente de nuevo, le quedan 3 intentos")
                ti.sleep(1)
                print("\n presione enter para volver a intentar...")
                ms.getch()
                os.system('cls')
            elif GZF_ayuda == 2:
                GZF_help = GZF_contra[GZF_user.index(GZF_usuario)]            
                GZF_busqueda = GZF_help.find("$")
                if GZF_busqueda == -1:
                    GZF_busqueda = GZF_help.find("&")
                    if GZF_busqueda== -1:
                        GZF_busqueda = GZF_help.find("%")
                        if GZF_busqueda == -1:
                            GZF_busqueda = GZF_help.find("#")
                GZF_caracter = GZF_help[GZF_busqueda:GZF_busqueda+1]
                print("La contraseña debe llevar el carecter especial ",GZF_caracter)
                print("Intente de nuevo, le queda 2 intento")
                ti.sleep(1)
                print("\n presione enter para volver a intentar...")
                ms.getch()
                os.system('cls')
            elif GZF_ayuda == 3:
                GZF_caracter = GZF_help[GZF_busqueda-1:GZF_busqueda+2]
                print("El caracter se encuentra entre ",GZF_caracter)
                print("Intente de nuevo, le queda 1 intento")
                ti.sleep(1)
                print("\n presione enter para volver a intentar...")
                ms.getch()
                os.system('cls')
            elif GZF_ayuda > 3:
                print("Lo sentimos, ah sobrepasado el limite de intentos :( \n")
                print("\nPara recuperar su contraseña comuniquese con el administrador al siguiente numero: 7712648761")
                GZF_perfil = 0
                GZF_error = 0
                GZF_salida = 1
                print("\nPresione enter para salir...")
                ms.getch()
    return GZF_perfil,GZF_salida


"**********************************************************************************************************************************************************"    
#repetir calculos o programas
def GZF_repetir(r):
    print("¿Desea volver a repetir el ",r,"?")
    GZF_desicion = input("Y/N: ")
    if GZF_desicion.upper() == "Y":
        GZF_seguir = 1
        os.system('cls')
    else:
        GZF_seguir = 0
        os.system('cls')
    return(GZF_seguir)


"**********************************************************************************************************************************************************"
#Titulo de bienvenida

def GZF_bienvenida():
    os.system('cls')
    GZF_titulo =["#################################################################################################################################################",
"#                                                                                                                                               #",
"#▒█▀▀█ ▀█▀ ▒█▀▀▀ ▒█▄░▒█ ▒█░░▒█ ▒█▀▀▀ ▒█▄░▒█ ▀█▀ ▒█▀▀▄ ▒█▀▀▀█ 　 ░█▀▀█ ▒█░░░ 　 ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀ ▒█▀▀█ ▀▀█▀▀ ▒█▀▀▀█               #",
"#▒█▀▀▄ ▒█░ ▒█▀▀▀ ▒█▒█▒█ ░▒█▒█░ ▒█▀▀▀ ▒█▒█▒█ ▒█░ ▒█░▒█ ▒█░░▒█ 　 ▒█▄▄█ ▒█░░░ 　 ▒█▄▄█ ▒█▄▄▀ ▒█░░▒█ ▒█▄▄▄█ ▒█▀▀▀ ▒█░░░ ░▒█░░ ▒█░░▒█               #",
"#▒█▄▄█ ▄█▄ ▒█▄▄▄ ▒█░░▀█ ░░▀▄▀░ ▒█▄▄▄ ▒█░░▀█ ▄█▄ ▒█▄▄▀ ▒█▄▄▄█ 　 ▒█░▒█ ▒█▄▄█ 　 ▒█░░░ ▒█░▒█ ▒█▄▄▄█ ░░▒█░░ ▒█▄▄▄ ▒█▄▄█ ░▒█░░ ▒█▄▄▄█               #",
"#                                                                                                                                               #",
"#################################################################################################################################################",
"#                                                                                                                                               #",
"#▒█▀▀▄ ▒█▀▀▀ 　 ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ 　 ░█▀▀█ ▒█░░▒█ ░█▀▀█ ▒█▄░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▄ ░█▀▀█ #",
"#▒█░▒█ ▒█▀▀▀ 　 ▒█▄▄█ ▒█▄▄▀ ▒█░░▒█ ▒█░▄▄ ▒█▄▄▀ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ 　 ▒█▄▄█ ░▒█▒█░ ▒█▄▄█ ▒█▒█▒█ ░▄▄▄▀▀ ▒█▄▄█ ▒█░▒█ ▒█▄▄█ #",
"#▒█▄▄▀ ▒█▄▄▄ 　 ▒█░░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ▒█▄▄█ ▄█▄ ▒█▄▄▄█ ▒█░░▀█ 　 ▒█░▒█ ░░▀▄▀░ ▒█░▒█ ▒█░░▀█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█░▒█ #",
"#                                                                                                                                               #",
"#################################################################################################################################################",]

    for i in range(len(GZF_titulo)):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK +GZF_titulo[i])
        ti.sleep(0.2)
    ti.sleep(1/2)
    os.system('cls')
    for j in range(len(GZF_titulo)):
        print(Style.BRIGHT + Fore.MAGENTA + Back.BLACK +GZF_titulo[j])
        ti.sleep(0.2)
    ti.sleep(1/2)
    os.system('cls')

    for k in range(len(GZF_titulo)):
        print(Style.BRIGHT + Fore.GREEN + Back.BLACK +GZF_titulo[k])
        ti.sleep(0.2)
    ti.sleep(1/2)

    print("\n presione enter para regresar al menu...")
    ms.getch()
    os.system('cls')
    GZF_welcome = 1

    return GZF_welcome


"**********************************************************************************************************************************************************"
"inicio de calculos del proyecto"

#calculo de relacion de engranajes y poleas
def datos_proyecto_relacion():    
    transmisiones=[0,0,0]
    rpm_conducidos=[0,0]
    poleas = [6,20] 
    rpm_motriz = 1715 #RPM
    engranes = [15,46]
    os.system('cls')
    " conexion de poleas y engranes:   1.polea motriz - (2.polea conducida - 3.engrane conducido) - 4.engrane de salida"
    
    print("  Los datos del proyecto son los siguientes:")
    ti.sleep(1/3)
    print("  La polea de entrada (motriz) cuenta con una medida de ",poleas[0]," cm, y cuenta con una velocidad de ",rpm_motriz," RPM.\n")
    ti.sleep(1/3)
    print("  En el siguiente eje de movimiento: la polea conducida (2) cuenta con una medida  de ",poleas[1]," cm")
    print("  y el mismo eje de movimiento el engrane conducido (3) cuenta con una medida de ",engranes[0]," dientes\n")
    ti.sleep(1/3)
    print("  El engrane de salida es de ",engranes[1]," dientes\n")
    ti.sleep(1)
    print("\n  Se calculara la relacion de  transmision total y transmisiones parciales")
    ti.sleep(1/2)
    print("  asi como las RPM de cada rueda conducida ")
    ti.sleep(1.5)
    print("\npresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("  La formula de transmision es: i = Z² / Z¹ = W¹ / W² ")
    ti.sleep(1/2)
    print("""\n Nomenclatura:
        i = relacion de transmision
        Z = numero de dientes de un engranaje ó diametro de la polea
        W = velocidad angular en RPM
        """)
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    print("iniciamos calculando la transmision i₁₋₂")
    ti.sleep(1/4)
    print("\n como se conocen el diametro de ambas poleas la formula queda: ")
    ti.sleep(1/4)
    print("\n i₁₋₂ = ",poleas[1]," / ",poleas[0])
    ti.sleep(1/4)
    transmisiones[0] = round((poleas[1] / poleas[0]),2)
    print("\npresione enter para calcular...")
    ms.getch()
    os.system('cls')

    print("\n por lo tanto: i₁₋₂ = ",transmisiones[0])
    ti.sleep(1)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print(" se procede a calcular  la transmision  i₃₋₄")
    ti.sleep(1/4)
    print("\n como se conocen el numero de dientes de ambos engranes la formula queda: ")
    ti.sleep(1/4)
    print("\n i₃₋₄ = ",engranes[1]," / ",engranes[0])
    ti.sleep(1/4)
    transmisiones[1] = round((engranes[1] / engranes[0]),2)
    print("\npresione enter para calcular...")
    ms.getch()
    os.system('cls')
    
    print(" por lo tanto: i₃₋₄ = ",round(transmisiones[1],1))
    ti.sleep(1)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print(" Por ultimo procedemos a calcular la transmision total o  i₁₋₄")
    ti.sleep(1/4)
    print("\n para este caso se utilizara una formula diferente que es la multiplicacion de las transmisiones parciales, la cual queda: ")
    ti.sleep(1/4)
    print("\n i₁₋₄ =  i₁₋₂ * i₃₋₄")
    ti.sleep(1/4)
    print("\n por lo tanto: i₁₋₄ = ",round(transmisiones[0],1)," * ",round(transmisiones[1],1))
    ti.sleep(1/4)
    transmisiones[2]=round((transmisiones[0] * transmisiones[1]),2)
    print("\npresione enter para calcular...")
    ms.getch()
    os.system('cls')
    
    print(" La transmision total del sistema es: ",round(transmisiones[2],1))
    ti.sleep(1)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    
    print(" Continuando con los calculos, se procede a encontrar la velocidad angular de cada rueda del sistema.")
    ti.sleep(1/2)
    print(" se modificara la formula principal, quedando: W² = W¹ / i ")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print(" Iniciamos calculando W² = W¹ / i₁₋₂ ")
    ti.sleep(1/2)
    print("\n Como se conocen ambos datos, la formula queda: ")
    ti.sleep(1/4)
    print("\n polea conducida(W²) = ",round(rpm_motriz,1)," / ",round(transmisiones[0],1))
    ti.sleep(1/4)
    rpm_conducidos[0] = round((rpm_motriz / transmisiones[0]),2)
    print("\npresione enter para calcular...")
    ms.getch()
    os.system('cls')
    
    print(" Como la polea conducida(W²) y el engrane conducido(W³) se encuentran en el mismo eje")
    ti.sleep(1/4)
    print("\n ambas ruedas cuentan con la misma velocidad angular.")
    ti.sleep(1/2)
    print(" \nEntonces: la velocidad angular para W² y W³ es: ",round(rpm_conducidos[0],1)," RPM")
    ti.sleep(1)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print(" Procedemos con la velocidad angular en el engrane conducido ó engrande de salida (W⁴)")
    ti.sleep(1/4)
    print("\n como ahora conocemos la velocidad angular en W³, la formula queda: ")
    ti.sleep(1/4)
    print("\n engrande de salida (W⁴) = W³(",round(rpm_conducidos[0],1),") / i₃₋₄(",round(transmisiones[1],1),")")
    print("")
    ti.sleep(1/4)
    rpm_conducidos[1] = round((rpm_conducidos[0] / transmisiones[1]),2)             
    print("\npresione enter para calcular...")
    ms.getch()
    os.system('cls')
    
    print(" Entonces: la velocidad angular para W⁴ es: ",round(rpm_conducidos[1],1)," RPM")
    ti.sleep(1/4)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print(" Para Finalizar se enlistan los resultados obtenidos: \n")
    ti.sleep(1/4)
    print(" Relaciones de transmision:\n")
    ti.sleep(1/4)
    print("   i₁₋₂ = ",round(transmisiones[0],1))
    ti.sleep(1/4)
    print("   i₃₋₄ = ",round(transmisiones[1],1))
    ti.sleep(1/4)
    print("   i₁₋₄ = ",round(transmisiones[2],1))
    ti.sleep(1/4)
    print("\n Velocidades angulares en todas las ruedas:\n")
    ti.sleep(1/4)
    print("   polea motriz (W¹) = ",rpm_motriz," RPM")
    ti.sleep(1/4)
    print("   polea conducida (W²) = ",round(rpm_conducidos[0],1)," RPM")
    ti.sleep(1/4)
    print("   engrane conducido (W³)",round(rpm_conducidos[0],1)," RPM")
    ti.sleep(1/4)
    print("   engrande de salida (W⁴)",round(rpm_conducidos[1],1)," RPM")
    ti.sleep(1/4)
    print("\npresione enter para continuar...")
    ms.getch()
    os.system('cls')

    
def datos_nuevos(rueda,tipo):
    poleas_engranes = []
    print("Ingrese los datos solicitados")
    ti.sleep(1/4)
    print("Ingrese el ",rueda," motriz:")
    motriz = int(input("- - -> "))
    poleas_engranes.append(motriz)
    os.system('cls')
    print("ingrese el numero de RPM (revoluciones por minuto) ",tipo," motriz")
    rpm_motriz = int(input("- - -> "))
    os.system('cls')
    print("Ingrese ",rueda," conducido:")
    conducido = int(input("- - -> "))
    poleas_engranes.append(conducido)
    os.system('cls')

    return poleas_engranes,rpm_motriz

    
def calculo_relacion_engranes_poleas():
    seguir = 1
    while seguir == 1:
        for i in range(1,3):
            print("Bienvenido al calculo de relacion de engranajes y poleas")
            ti.sleep(1/5)
            os.system('cls')
        print("Bienvenido al calculo de relacion de engranajes y poleas")

        for i in range(1,11):
            print("cargando.")
            os.system('cls')
            print("cargando..")
            os.system('cls')
            print("cargando...")
            os.system('cls')
    
        print(""""¿desea hacer calculos con datos nuevos o utilizar los datos del proyecto?
1.- datos nuevos
2.- datos del proyecto
3.- regresar\n""")
        ti.sleep(1/3)
        datos = int(input("ingrese que datos desea utilizar: "))
        os.system('cls')
            
        if datos == 1:
            print("""¿desea calcular para poleas o engranes
            1.- poleas
            2.- engranes
            3.- regresar\n""")
            ti.sleep(1/4)
            calcular = int(input("ingrese el tipo de sistema a calcular: "))
            os.system('cls')
            if calcular == 1:
                bucle =1
                while bucle == 1:
                    poleas, rpm_motriz = datos_nuevos("diametro de la polea","de la polea")
                    rpm_conducido = rpm_motriz * (poleas[0]/poleas[1])
                    transmision = rpm_motriz / rpm_conducido
                    print("la velocidad de la polea conducida es: ",rpm_conducido," RPM\n")
                    print("la transmision del sistema de poleas es ",round(transmision,2)," : 1")
                    ti.sleep(1)
                    print("\n pesione enter para continuar...")
                    ms.getch()
                    os.system('cls')
                    bucle = repetir("calculo")        
            elif calcular == 2:
                bucle =1
                while bucle == 1:
                    engranes,rpm_motriz = datos_nuevos("numero de dientes del engrane","del engrane")
                    rpm_conducido = rpm_motriz * (engranes[0] / engranes[1])
                    transmision = rpm_motriz / rpm_conducido
                    print("la velocidad del engrane conducido es: ",rpm_conducido," RPM\n")
                    print("la transmision del sistema de engranaje es ",round(transmision,2)," : 1")
                    ti.sleep(1)
                    print("\n pesione enter para continuar...")
                    ms.getch()
                    os.system('cls')
                    bucle = repetir("calculo")
                seguir = 1            
            elif calcular == 3:
                seguir = 0

        elif datos ==2:
            bucle =1
            while bucle == 1:
                datos_proyecto_relacion()
                bucle = repetir("programa")
            seguir = 1
            
        elif datos == 3:
            seguir = 0
        

"**********************************************************************************************************************************************************"
#Razon de cambio de una variable con respecto al tiempo
def datos_proyecto_razon():
    print("Los datos del proyecto son los siguientes: \n")
    ti.sleep(1/4)
    
    T_Ci = 25.62
    t_ci = 0
    Tm = 100
    T_k = 90.31
    t_k = 962
    T_p = 94.94
    t_p = 0
    C = 0
    k = 0
    CI= " *CI *    "+str(T_Ci)+"    *     "+str(t_ci)+"     *    "+str(Tm)+"   *"
    K = " *K  *    "+str(T_k)+"    *     "+str(t_k)+"    *"
    P = " *P  *    "+str(T_p)+"    *     ?     *"
    datos = [" Tabla de datos"," ***************************************"," *   *  T = °C  *  t = seg  *  Tm = °C *"," ***************************************",CI," ***************************************",K," ****************************",P," ****************************"]
    nomenclatura =["Nomenclatura:","CI = condicion inicial","T = temperatura","Tm = temperatura del ambiente (es de valor constante)","t = tiempo","k= constante de proporcionalida"]

    for i in range(len(datos)):
        print(datos[i])
        ti.sleep(1/5)
    print("\n")

    for i in range(len(nomenclatura)):
        print(nomenclatura[i])
        ti.sleep(1/5)
        
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("La formula matematica para el calculo de la razon de cambio de la temperatura es: ")
    print("\ndT/dt = k(T-Tm)")
    ti.sleep(1/2)
    print("\nSe realizara el Procedimiento por pasos: \n")
    ti.sleep(1/3)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("Paso 1: Reacomodar expresion")
    ti.sleep(1/4)
    print("\ndT = k(T-Tm)dt")
    ti.sleep(1/2)
    print("se procede a juntar todas las (T) de temperatura en un lado y todas las (t) de tiempo en otro")
    ti.sleep(1/4)
    print("\ndT / T-Tm = k*dt")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print("\nPaso 2: Resolver integral")
    ti.sleep(1/4)
    print("\nuna vez separados los terminos con sus correspondientes variables.")
    ti.sleep(1/4)
    print("se procede aplicar un proceso de integracion en ambos lados, quedando:")
    ti.sleep(1/4)
    print("\n ∫ (dT / T-Tm) = k* ∫ dt")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("atendiendo la integracion del primer miembro:  ∫ (dT / T-Tm)")
    ti.sleep(1/4)
    print("\ncomo la variable (T) se encuentra en el denominador el resultado de integracion es: ")
    ti.sleep(1/4)
    print("\n ln|T-Tm|")
    ti.sleep(1/4)
    print("\ny atendiendo el segundo miembro: k* ∫ dt")
    ti.sleep(1/4)
    print("\nse puede esperar que la (∫) integral de  1 con respecto a dt, sea:")
    ti.sleep(1/4)
    print("(k * t) + C")
    ti.sleep(1/4)
    print("quedando: ")
    ti.sleep(1/4)
    print("ln|T-Tm| = (k * t) + C")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print("\nPaso 3: despejar T\n")
    ti.sleep(1/4)
    print("\ncomo el primer miembro esta afectado por un (ln) logaritmo natural, la funcion inversa es un (e) exponencial ")
    ti.sleep(1/4)
    print("\nquedando: T-Tm = e ⁽ᵏ * ᵗ⁾⁺ᶜ")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("como la propiedad de los exponentes nos dice que: eᵃ⁺ᵇ = eᵃ * eᵇ")
    ti.sleep(1/4)
    print("\npodemos reescribir que:  e ⁽ᵏ * ᵗ⁾⁺ᶜ = e⁽ᵏ * ᵗ⁾ *  eᶜ")
    ti.sleep(1/4)
    print("\ny como el exponencial de una constante (eᶜ) es igual a otra constante (C), entonces")
    ti.sleep(1/4)
    print("\n e ⁽ᵏ * ᵗ⁾⁺ᶜ = e⁽ᵏ * ᵗ⁾ * C")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("reescribiendo: T-Tm = e ⁽ᵏ * ᵗ⁾⁺ᶜ , nos queda:")
    ti.sleep(1/4)
    print("\n T-Tm = e⁽ᵏ * ᵗ⁾ * C")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("despejando la (T) temperatura nos queda la formula general:")
    ti.sleep(1/4)
    print("\n T = Tm + C*e⁽ᵏ * ᵗ⁾")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print("\nPaso 4: encontrar a C con los valores de la Condicion Inicial")
    ti.sleep(1/4)
    print("Una vez obtenida la formula general, se procede a encontrar los valores de las constantes")
    ti.sleep(1/4)
    print("\nse utilizan los valores de la condicion inicial para sustituirlos en la formula general")
    ti.sleep(1/4)
    print("\nsiendo")
    ti.sleep(1/4)
    print("\nCi:  T =",T_Ci,",  t =",t_ci ,",  Tm = ",Tm)
    ti.sleep(1/4)
    print("\nla formula general queda:")
    ti.sleep(1/4)
    print(T_Ci," = ",Tm, "+ C*e⁽ᵏ * ⁰⁾")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("en este caso: e⁽ᵏ * ⁰⁾, como k se multiplica por 0, el argumento nos queda como (e⁰) exponencial de 0.")
    ti.sleep(1/4)
    print("\ny matematicamente el  (e⁰) es 1 ")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("al sustituir el exponencial, queda solamente: ")
    ti.sleep(1/4)
    print("\n",T_Ci," = ",Tm, "+ C")
    ti.sleep(1/4)
    print("\npor lo que en este caso C = ",T_Ci,"-",Tm)
    C = float(T_Ci - Tm)
    ti.sleep(1/4)
    print("\n entonces C = ",C)
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print("\nPaso 5: Encontrar k con los valores de la proporcionalidad")
    ti.sleep(1/4)
    print("\nAhora se procede a obtener el valor de la constante de proporcionalida (k)")
    ti.sleep(1/4)
    print("\nse utilizan los valores de k para sustituirlos en la formula")
    ti.sleep(1/4)
    print("\nsiendo")
    ti.sleep(1/4)
    print("\nk: T =",T_k,",  t =",t_k ,",  Tm = ",Tm,",  C = ",C)
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("\nsustituyendo valores en la formula:")
    ti.sleep(1/4)
    print("\n",T_k," = ",Tm, "+ ",C,"*e^(k*",t_k,")")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("ahora se procede a despejar a k")
    ti.sleep(1/4)
    print("\nquedando")
    ti.sleep(1/4)
    print("\n(",T_k,"-",Tm,")","/",C," = e^(k*",t_k,")")
    T_km = T_k-Tm
    ti.sleep(1/4)
    print("\nsimplificando:")
    ti.sleep(1/4)
    print("\n",T_km,"/",C," = e^(k*",t_k,")")
    ti.sleep(1/4)
    print("\ncomo el exponencial afecta el valor de k, se aplica el ln")
    ti.sleep(1/4)
    print("\n ln|",T_km,"/",C,"|"," = k*",t_k)
    logaritmo_n_k = ma.log(T_km/C)
    ti.sleep(1/4)
    print("\n quedando:")
    ti.sleep(1/4)
    print("\n",round(logaritmo_n_k,6)," = ",t_k,"k")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("para finalizar el despeje se procede a dejar sola a k:")
    ti.sleep(1/4)
    print("\n",round(logaritmo_n_k,6),"/",t_k," = k")
    k = round(logaritmo_n_k,6) / t_k
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("\ndando como resultado que:")
    ti.sleep(1/4)
    print("\n k = ",round(k,6))
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("una vez encontrados los valores para las constantes: C y k, la formula general queda de la siguiente manera:")
    ti.sleep(1/4)
    print("\nT = ",Tm," +", C,"*e^(",round(k,6),"t)")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("posterior a encontrar las respectivas las constantes de la formula, se procede a despejar para la variable de (t) tiempo")
    ti.sleep(1/4)
    print("\nya que dentro de nuestra pregunta lo que se pide es encontrar el tiempo que tarde el sistema en llegar a ",T_p)
    T_pm = T_p - Tm
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print("\nPaso 6: dar respuesta a la pregunta")
    ti.sleep(1/4)
    print("Se procede a encontrar la formula para el (t) tiempo, realizando el mismo procedimiento que para la variable k")
    ti.sleep(1/4)
    print("\np: T =",T_p,", t = ?, Tm = ",Tm,", C = ",C,", k = ",round(k,6))
    ti.sleep(1/4)
    print("\n",T_p," = ",Tm, "+ ",C,"*e^(",round(k,6),"*t)")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("como el exponencial afecta el valor de k, se aplica el ln")
    ti.sleep(1/4)
    print("\n ln|",T_pm,"/",C,"|"," = ",round(k,6),"*t")
    logaritmo_n_t = ma.log(T_pm/C)
    ti.sleep(1/4)
    print("\nquedando:")
    ti.sleep(1/4)
    print("\n",round(logaritmo_n_t,6)," = ",round(k,6),"t")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("para finalizar el despeje se procede a dejar sola a t:")
    ti.sleep(1/4)
    print("\n",round(logaritmo_n_t,6),"/",round(k,6)," = t")
    t_p = round(logaritmo_n_t,6) / round(k,6)
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
    
    print("por lo tanto el tiempo que tarda el sistema en llegar a la Temperatura de ",T_p)
    ti.sleep(1/4)
    print("\nes de ",round(t_p,5)," segundos")
    ti.sleep(1/2)
    print("\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')

    print("paso 7: reescribir la tabla de datos")
    ti.sleep(1/4)
    
    P =" *P  *    "+str(T_p)+"    *  "+str(round(t_p,2))+"  *"
    print("\nSe volvera a escribir la tabla de datos con la respuesta a la pregunta\n")
    ti.sleep(1/4)
    
    datos_resultado = [" Tabla de datos"," ***************************************"," *   *  T = °C  *  t = seg  *  Tm = °C *"," ***************************************",CI," ***************************************",K," ****************************",P," ****************************"]

    for i in range(len(datos_resultado)):
          print(datos_resultado[i])
          ti.sleep(1/5)
    ti.sleep(1/4)
    print("\npresione enter para continuar...")
    ms.getch()
    os.system('cls')
          
          
def datos_otro(Tm,T_Ci,t_ci,T_k,t_k):
    C = 0 
    k = 0
    print("""¿Para su pregunta desea encontrar tiempo o Temperatura?
    1.- Temperatura
    2.- tiempo\n""")
    pregunta = int(input("ingrese el numero para su tipo de pregunta: "))
    os.system('cls')
    
    if pregunta == 1:
        T_p = "?"
        t_p = float(input("ingrese el tiempo en seg: "))
        os.system('cls')
        
    elif pregunta == 2:
        t_p = "?"
        T_p = float(input("ingrese la Temperatura en °C: "))
        os.system('cls')
        
    CI= " *CI *    "+str(T_Ci)+"    *     "+str(t_ci)+"     *    "+str(Tm)
    K = " *K  *    "+str(T_k)+"    *     "+str(t_k)+"    "
    P =" *P  *  "+str(T_p)+"  *  "+str(t_p)+"  "
    print("Los datos ingresados quedan de la siguiente manera: \n")
    ti.sleep(1/3)
    datos = [" Tabla de datos"," ***************************************"," *   *  T = °C  *  t = seg  *  Tm = °C *"," ***************************************",CI," ***************************************",K," ***************************************",P," ***************************************"]
    for i in range(len(datos)):
        print(datos[i])
        ti.sleep(1/5)
    print("presione enter para calcular...")
    ms.getch()
    os.system('cls')
    
    if pregunta == 1:
        for i in range(1,11):
            print("Calculando... /")
            os.system('cls')
            print("Calculando...-")
            os.system('cls')
            print("Calculando...\ ")
            os.system('cls')
            print("Calculando...I ")
            os.system('cls')
            
        C = float(T_Ci - Tm)
        T_km = T_k-Tm
        logaritmo_n_k = ma.log(T_km/C)
        k = round(logaritmo_n_k,6) / t_k
        exponencial = round(ma.exp(round(k,6) * t_p),5)
        T_p = Tm + (C*exponencial)

        print("Resultados finales: ")
        print("\nEl valor de C = ",C)
        print("\nEl valor de k = ",k)
        ti.sleep(0.8)
        print("\npor lo tanto la temperatura a la que llegara el sistema en un tiempo de ",t_p," seg")
        print("\nes de ",round(T_p,4)," °C")
        ti.sleep(1)
        print("\npresione enter para continuar...")
        ms.getch()
        os.system('cls')
        
        print("Para finalizar se reescribira la tabla de datos con los resultados\n")              
        P =" *P  *    "+str(round(T_p,5))+"    *  "+str(t_p)+"  "
        datos_resultados = [" Tabla de datos"," ***************************************"," *   *  T = °C  *  t = seg  *  Tm = °C *"," ***************************************",CI," ***************************************",K," ***************************************",P," ***************************************"]
        for i in range(len(datos_resultados)):
            print(datos_resultados[i])
            ti.sleep(1/5)

    elif pregunta == 2:
        for i in range(1,11):
            print("Calculando... /")
            os.system('cls')
            print("Calculando...-")
            os.system('cls')
            print("Calculando...\ ")
            os.system('cls')
            print("Calculando...I ")
            os.system('cls')
            
        C = float(T_Ci - Tm)
        T_km = T_k-Tm
        logaritmo_n_k = ma.log(T_km/C)
        k = round(logaritmo_n_k,6) / t_k
        T_pm = T_p - Tm
        logaritmo_n_t = ma.log(T_pm/C)
        t_p = round(logaritmo_n_t,6) / round(k,6)

        print("Resultados finales: ")
        print("\nEl valor de C = ",C)
        print("\nEl valor de k = ",k)
        ti.sleep(0.8)
        print("\npor lo tanto el tiempo que tarda el sistema en llegar a la Temperatura de ",T_p," °C")
        print("\nes de ",round(t_p,4)," segundos")
        ti.sleep(1)
        print("\npresione enter para continuar...")
        ms.getch()
        os.system('cls')
        
        print("Para finalizar se reescribira la tabla de datos con los resultados\n")
        P =" *P  *    "+str(T_p)+"    *  "+str(round(t_p,5))+"  "
        datos_resultados = [" Tabla de datos"," ***************************************"," *   *  T = °C  *  t = seg  *  Tm = °C *"," ***************************************",CI," ***************************************",K," ***************************************",P," ***************************************"]
        for i in range(len(datos_resultados)):
            print(datos_resultados[i])
            ti.sleep(1/5)
            
    print("\n\nPresione enter para continuar...")
    ms.getch()
    os.system('cls')
                    
        
def razon_de_cambio():
    seguir = 1
    while seguir == 1:
        for i in range(1,5):
            os.system('cls')
            print("Bienvenido al calculo de razon de cambio de temperatura")
            ti.sleep(1/5)
            os.system('cls')
        for i in range(1,11):
            print("Bienvenido al calculo de razon de cambio de temperatura")
            print("cargando.")
            os.system('cls')
            print("Bienvenido al calculo de razon de cambio de temperatura")
            print("cargando..")
            os.system('cls')
            print("Bienvenido al calculo de razon de cambio de temperatura")
            print("cargando...")
            os.system('cls')
            print("Bienvenido al calculo de razon de cambio de temperatura")
            print("cargando....")
            os.system('cls')
            
        print(""""¿desea hacer los calculos con datos nuevos o utilizar los datos del proyecto?
1.- datos nuevos
2.- datos del proyecto
3.- regresar\n""")
        ti.sleep(1/3)

        datos = int(input("ingrese el numero de los datos a utilizar: "))
        os.system('cls')
            
        if datos == 1:
            bucle =1
            while bucle == 1:
                print("Ingrese los datos solicitados\n")
                ti.sleep(1/4)
                Tm = float(input("Ingrese la temperatura ambiente en °C: "))
                os.system('cls')
    
                T_Ci = float(input("Ingrese la temperatura inicial de su sistema en °C: "))
                os.system('cls')
    
                print("Para el tiempo inicial, se recomienda utilizar un tiempo en 0 cero")
                print("\npresione enter para continuar...\n")
                t_ci = 0
                ms.getch()
                os.system('cls')
    
                T_k = float(input("Ingrese la temperatura de muestra (k) en °C: "))
                os.system('cls')
                t_k = float(input("Ingrese el tiempo de muestra (k) en seg: "))
                os.system('cls')
                
                datos_otro(Tm,T_Ci,t_ci,T_k,t_k)
                bucle = repetir("calculo")
            seguir = 1
            
        elif datos ==2:
            bucle =1
            while bucle == 1:
                datos_proyecto_razon()
                bucle = repetir("programa")
            seguir = 1
            
        elif datos == 3:
            seguir = 0


"**********************************************************************************************************************************************************"
#menu proyecto
def calculos_proyecto(GETH_opcion):
    if GETH_opcion == 1:
        calculo_relacion_engranes_poleas()
    elif GETH_opcion == 2:
        razon_de_cambio()


"**********************************************************************************************************************************************************"
"inicio programa 2 menu de resistencias"

#bandas de resistencias
def GZF_banda(GZF_numero):
    print("Seleccione la banda num. ",GZF_numero,"\n")
    ti.sleep(1/2)
    GZF_colores = ["Negro --> 0","Marron --> 1","Rojo --> 2","Naranja --> 3","Amarillo --> 4","Verde --> 5","Azul --> 6","Violeta --> 7","Gris --> 8","Blanco --> 9"]
    for i in range(len(GZF_colores)):
        print(GZF_colores[i])
        ti.sleep(1/4)      
    GZF_banda = str(input("Ingrese el numero del color de la banda:  "))
    os.system('cls')
    return GZF_banda

#banda multiplicadora
def GZF_multiplicador():
    GZF_multi = 0
    print("Seleccione la banda Multiplicador \n")
    ti.sleep(1/2)
    GZF_colores = ["Negro x1Ω - - -> 0","Marron x10Ω - - -> 1","Rojo x100Ω - - -> 2","Naranja x1kΩ - - -> 3","Amarillo x10kΩ - - -> 4","Verde x100kΩ - - -> 5","Azul x1MΩ - - -> 6","Violeta x10MΩ - - -> 7","Gris x100MΩ - - -> 8","Blanco x1GΩ - - -> 9","Oro x0.1Ω - - -> 10","Plata x0.01Ω - - -> 11"]
    for i in range(len(GZF_colores)):
        print(GZF_colores[i])
        ti.sleep(1/4)
    GZF_opcion = int(input("""Ingrese el numero de la banda multiplicador
- - -> """))
    os.system('cls') 
    if GZF_opcion ==0: #1Ω
        GZF_multi = 1
    elif GZF_opcion in range(1,10):
        GZF_opcion = GZF_opcion * "0"
        GZF_multi = "1"+GZF_opcion
        GZF_multi = float(GZF_multi)
    elif GZF_opcion ==10: #0.1Ω
        GZF_multi = 0.1        
    elif GZF_opcion ==11: #0.01Ω
        GZF_multi = 0.01
    return GZF_multi

#banda de tolerancia
def GZF_tolerancia():
    GZF_tol = " "
    print("Seleccione la banda de Tolerancia \n")
    ti.sleep(1/2)
    GZF_colores = ["Marron ±1% - - -> 0","Rojo ±2% - - -> 1","Verde ±0.5% - - -> 2","Azul ±0.25% - - -> 3","Violeta ±0.1% - - -> 4","Gris ±0.05% - - -> 5","Oro ±5% - - -> 6","Plata ±10% - - -> 7"]
    for i in range(len(GZF_colores)):
         print(GZF_colores[i])
         ti.sleep(1/4)
    GZF_opcion = int(input("Ingrese el numero de la banda de tolerancia"))
    os.system('cls')
    if GZF_opcion == 0:
        GZF_tol = "1"
    elif GZF_opcion == 1:
        GZF_tol = "2"
    elif GZF_opcion == 2:
        GZF_tol = "0.5"
    elif GZF_opcion == 3:
        GZF_tol = "0.25"
    elif GZF_opcion == 4:
        GZF_tol = "0.1"
    elif GZF_opcion == 5:
        GZF_tol = "0.05"
    elif GZF_opcion == 6:
        GZF_tol = "5"
    elif GZF_opcion == 7:
        GZF_tol = "10"       
    return GZF_tol

# calculo de valor resistivo
def GZF_calculo_resistencia(GZF_numero,GZF_multiplicador,GZF_tolerancia):
    for i in range(1,11):
            print("Calculando... /")
            os.system('cls')
            print("Calculando...-")
            os.system('cls')
            print("Calculando...\ ")
            os.system('cls')
            print("Calculando...I ")
            os.system('cls')       
    GZF_valor = float(GZF_multiplicador) * float(GZF_numero)
    if GZF_valor < 1000:
        print("El valor de la resistencia es: ", GZF_valor ," Ω con tolerancia ± ",GZF_tolerancia,"%")
    elif GZF_valor >= 1000 and GZF_valor < 100000:
        GZF_valor = GZF_valor / 1000
        print("El valor de la resistencia es: ", GZF_valor ," kΩ con tolerancia ± ",GZF_tolerancia,"%")
    elif GZF_valor >= 100000 and GZF_valor < 10000000:
        GZF_valor = GZF_valor / 100000
        print("El valor de la resistencia es: ", GZF_valor ," MΩ con tolerancia ± ",GZF_tolerancia,"%")
    elif GZF_valor >=10000000 and GZF_valor < 10000000000:
        GZF_valor = GZF_valor / 10000000
        print("El valor de la resistencia es: ", GZF_valor ," GΩ con tolerancia ± ",GZF_tolerancia,"%")
    ti.sleep(1)
    print("\npresione enter para continuar...")
    ms.getch()
    
    
# resistencias 4 y 5 bandas
def GZF_resistencias(GZF_tipo):
    if GZF_tipo ==1:
        GZF_ciclo = 1
        while GZF_ciclo == 1:
            print("RESISTENCIAS DE 4 BANDAS \n")
            for i in range(1,11):
                print("cargando.")
                os.system('cls')
                print("cargando..")
                os.system('cls')
                print("cargando...")
                os.system('cls')
            GZF_banda1 = GZF_banda(1)
            GZF_banda2 = GZF_banda(2)
            GZF_numero = GZF_banda1+GZF_banda2
            GZF_numero = int(GZF_numero)
            GZF_banda_multi = GZF_multiplicador()
            GZF_banda_tol = GZF_tolerancia()
            GZF_calculo_resistencia(GZF_numero,GZF_banda_multi,GZF_banda_tol)
            GZF_ciclo = GZF_repetir("programa")
    elif GZF_tipo == 2:
        GZF_ciclo = 1
        while GZF_ciclo == 1:
            print("RESISTENCIAS DE 5 BANDAS \n")
            for i in range(1,11):
                print("cargando.")
                os.system('cls')
                print("cargando..")
                os.system('cls')
                print("cargando...")
                os.system('cls')
                
            GZF_banda1 = GZF_banda(1)
            GZF_banda2 = GZF_banda(2)
            GZF_banda3 = GZF_banda(3)
            GZF_numero = GZF_banda1+GZF_banda2+GZF_banda3
            GZF_banda_multi = GZF_multiplicador()
            GZF_banda_tol = GZF_tolerancia()
            GZF_valor = GZF_calculo_resistencia(GZF_numero,GZF_banda_multi,GZF_banda_tol)
            GZF_ciclo = GZF_repetir("programa")
    print("Presione un enter para regresar al menu de resistencias")
    ms.getch()


"*******************************************************************************************************************************************************************"
#calculo de vida de un rodamiento
def GZF_datos(): 
    print("Para realizar el calculo de vida del rodamiento debe ingresar los siguientes datos\n")
    GZF_Fr = float(input("Fuerza Radial: "))
    os.system('cls')
    print("Para realizar el calculo de vida del rodamiento debe ingresar los siguientes datos\n")    
    GZF_Fa = float(input("Fuerza Axial: "))
    os.system('cls')
    print("Para realizar el calculo de vida del rodamiento debe ingresar los siguientes datos\n")
    GZF_C_basica = float(input("Carga Basica:"))
    os.system('cls')
    print("Para realizar el calculo de vida del rodamiento debe ingresar los siguientes datos\n")
    GZF_RPM = float(input("Revoluciones por minuto ó RPM: "))
    os.system('cls')
    print("Para realizar el calculo de vida del rodamiento debe ingresar los siguientes datos\n")    
    print("""Que anillo gira
1.- anillo interno
2.- anillo externo""")
    GZF_elegir = int(input("ingrese el numero de anillo: "))
    if GZF_elegir == 1:
        GZF_anillo = 1
    elif GZF_elegir == 2:
        GZF_anillo = 1.2
    else:
        GZF_anillo = 1
    return GZF_Fr, GZF_Fa, GZF_C_basica, GZF_RPM,GZF_anillo

    
def GZF_cojinete_bolas():
    os.system('cls')
    print("De la siguiente tabla de tipos de cojinetes selecione el tipo con el numero al costado \n")
    ti.sleep(1)
    GZF_tabla_cojinete = []
    GZF_tipo_cojinete = ["""****************************************************************
* TIPO DE COJINETE        *      *  x1   *   y1  *   x2 *   y2 *
*                         *      *       *       *      *      *""",
"""***********************************************************************
* Cojinetes de bolas de   *	 *   	 *       *      *      *      *
* contacto radial	  *	 *  1	 *   0	 *  0.5	*  1.4 *  "1" *""",
"""***********************************************************************
* Cojinetes de bolas de   *	 *       *       *      *      *      *
* contacto angular,       * <15  *  1    * 1.25  * 0.45 * 1.2  *  "2" *
* angulo pequeño          *      *       *       *      *      *      *""",
"""***********************************************************************
* Cojinetes de bolas de   *	 *       *       *      *      *      *
* contacto angular,       * >15  *  1    * 0.75  * 0.4  * 0.75 *  "3" *
* angulo grande           *      *       *       *      *      *      *""",
"""***********************************************************************
* Cojinetes de doble      *	 *       *       *      *      *      *
* hilera y duplex         *      *  1    * 0.75  * 0.63 * 3.7  *  "4" *
***********************************************************************"""]
    for i in range(len(GZF_tipo_cojinete)):
        print(GZF_tipo_cojinete[i])
        ti.sleep(1/5)

    GZF_cojinete = int(input("Ingrese el tipo de cojinete a utilizar: "))

    if GZF_cojinete == 1:
        GZF_tabla_cojinete = [1,0,0.5,1.4]
    elif GZF_cojinete == 2:
        GZF_tabla_cojinete = [1,1.25,0.45,1.2]
    elif GZF_cojinete == 3:
        GZF_tabla_cojinete = [1,0.75,0.4,0.75]
    elif GZF_cojinete == 4:
        GZF_tabla_cojinete = [1,0.75,0.63,3.7]
    
    return GZF_tabla_cojinete


def GZF_cojinete_rodillos():
    os.system('cls')
    print("De la siguiente tabla de tipos de cojinetes selecione el tipo con el numero al costado \n")
    ti.sleep(1)
    GZF_tabla_cojinete = []
    GZF_tipo_cojinete = ["""****************************************************************
* TIPO DE COJINETE        *      *  x1   *   y1  *   x2 *   y2 *
*                         *      *       *       *      *      *""",
"""***********************************************************************
* Cojinetes de doble      *      *       *       *      *      *      *
* hilera y duplex         *      *  1    * 0.75  * 0.63 * 3.7  *  "1" *""",
"""***********************************************************************
* Cojinetes de rodillos   *      *       *       *      *      *      *
* esfericos (series 22    *      *  1    * 2.5   * 0.67 * 3.7  *  "2" *
*  ó 30)                  *      *       *       *      *      *      *""",
"""***********************************************************************
* Cojinetes de rodillos   *      *       *       *      *      *      *
* esfericos (series 23,   *      *  1    * 2.0   * 0.67 * 3.0  *  "3" *
* 31 ó 32)                *      *       *       *      *      *      *""",
"""***********************************************************************
* Cojinetes de rodillos   *      *       *       *      *      *      *
* conicos, angulo pequeño *      *  1    *   0   * 0.4  * 1.8  *  "4" *""",
"""************************************************************************
* Cojinetes de rodillos   *      *       *       *      *      *      *
* conicos, angulo gande   *      *  1    *   0   * 0.4  * 1.0  *  "5" *""",
"""***********************************************************************
* Cojinetes de rodillos   *      *       *       *      *      *      *
* conicos, doble hilera   *      *  1    * 1.6   * 0.67 * 2.5  *  "6" *
***********************************************************************"""]
    
    for i in range(len(GZF_tipo_cojinete)):
        print(GZF_tipo_cojinete[i])
        ti.sleep(1/5)

    GZF_cojinete = int(input("Ingrese el tipo de cojinete a utilizar: "))

    if GZF_cojinete == 1:
        GZF_tabla_cojinete = [1,0.75,0.63,3.7]
    elif GZF_cojinete == 2:
        GZF_tabla_cojinete = [1,2.5,0.67,3.7]
    elif GZF_cojinete == 3:
        GZF_tabla_cojinete = [1,2.0,0.67,3.0]
    elif GZF_cojinete == 4:
        GZF_tabla_cojinete = [1,0,0.4,1.8]
    elif GZF_cojinete == 5:
        GZF_tabla_cojinete = [1,0,0.4,1]
    elif GZF_cojinete == 6:
        GZF_tabla_cojinete = [1,1.6,0.67,2.5]
        
    return GZF_tabla_cojinete


def GZF_servicio(GZF_cojinete):
    os.system('cls')
    GZF_fs = 0
    print("De la siguiente tabla de factores de servicio selecione el Fs con el numero al costado \n")
    ti.sleep(1)
    
    GZF_menu_servicio = ["""*******************************************************
* 		          * Factores de servicio Fs   *
*  		          *****************************
* TIPO DE COJINETE        * Rodamientos * Rodamientos *
*                         *   de bolas  * de rodillos *""",
"""**************************************************************
* Uniforme, carga estable *	1.0     *    1.0      *  "1" *""",
"""**************************************************************
* Con choques lijeros     * 	1.5	*    1.0      *  "2" *""",
"""**************************************************************
* Con choques moderados   *	2.0	*    1.3      *  "3" *""",
"""**************************************************************
* Con choques pesados     *	2.5	*    1.7      *  "4" *""",
"""**************************************************************
* Con choques extremos    *	3.0	*    2.0      *  "5" *
**************************************************************"""]

    for i in range(len(GZF_menu_servicio)):
        print(GZF_menu_servicio[i])
        ti.sleep(1/5)
        
    GZF_tipo_factor = int(input("Ingrese el tipo de factor de servicio a utilizar: "))
    if GZF_cojinete == 1:
        if GZF_tipo_factor == 1:
            GZF_fs = 1
        elif GZF_tipo_factor == 2:
            GZF_fs = 1.5
        elif GZF_tipo_factor == 3:
            GZF_fs = 2
        elif GZF_tipo_factor == 4:
            GZF_fs = 2.5
        elif GZF_tipo_factor == 5:
            GZF_fs = 3
            
    elif GZF_cojinete == 2:
        if GZF_tipo_factor == 1:
            GZF_fs = 1
        elif GZF_tipo_factor == 2:
            GZF_fs = 1
        elif GZF_tipo_factor == 3:
            GZF_fs = 1.3
        elif GZF_tipo_factor == 4:
            GZF_fs = 1.7
        elif GZF_tipo_factor == 5:
            GZF_fs = 2

    return GZF_fs
            
    
def GZF_vida_rodamiento(GZF_tabla, GZF_Fr, GZF_Fa, GZF_C_basica, GZF_RPM,GZF_anillo,GZF_b,GZF_Fs):
    if GZF_Fs == 0:
        x1 = GZF_tabla[0]
        y1 = GZF_tabla[1]
        x2 = GZF_tabla[2]
        y2 = GZF_tabla[3]
        "cargas equivalentes" #formula cargas equivalentes = (anillo que gira * valores de tabla X * fuerza radial) + (valores de tabla Y * fuerza axial)
        GZF_carga_equivalente_1 = (GZF_anillo * x1 *GZF_Fr) + (y1*GZF_Fa)
        GZF_carga_equivalente_2 = (GZF_anillo * x2 *GZF_Fr) + (y2*GZF_Fa)
        if GZF_carga_equivalente_1 > GZF_carga_equivalente_2:
            "vida en millones de revoluciones"
            GZF_vida_nominal = pow(GZF_C_basica / GZF_carga_equivalente_1, GZF_b)
            print("Vida nominal ",round(GZF_vida_nominal,2), " en millones de revoluciones")
            "vida en horas"
            GZF_vida_nominal_horas = (1000000/(60*GZF_RPM)) * GZF_vida_nominal
            print("Vida nominal ",round(GZF_vida_nominal_horas,2), " en horas")   
        elif GZF_carga_equivalente_2 > GZF_carga_equivalente_1:
            "vida en millones de revoluciones"
            GZF_vida_nominal = pow(GZF_C_basica / GZF_carga_equivalente_2, GZF_b)
            print("Vida nominal ",round(GZF_vida_nominal,2), " en millones de revoluciones")
            "vida en horas"
            GZF_vida_nominal_horas = (1000000/(60*GZF_RPM)) * GZF_vida_nominal
            print("Vida nominal ",round(GZF_vida_nominal_horas,2), " en horas")     
    elif GZF_Fs != 0:
        x1 = GZF_tabla[0]
        y1 = GZF_tabla[1]
        x2 = GZF_tabla[2]
        y2 = GZF_tabla[3]
        "cargas equivalentes"
        GZF_carga_equivalente_1 = (GZF_anillo * x1 *GZF_Fr) + (y1*GZF_Fa)
        GZF_carga_equivalente_2 = (GZF_anillo * x2 *GZF_Fr) + (y2*GZF_Fa)
        if GZF_carga_equivalente_1 > GZF_carga_equivalente_2:
            GZF_carga_equivalente_fs = GZF_carga_equivalente_1 * GZF_Fs
            "vida en millones de revoluciones"
            GZF_vida_nominal =  pow(GZF_C_basica / GZF_carga_equivalente_fs, GZF_b)
            print("Vida nominal ",round(GZF_vida_nominal,3), " en millones de revoluciones")
            "vida en horas"
            GZF_vida_nominal_horas = (1000000/(60*GZF_RPM)) * vida_nominal
            print("Vida nominal ", round(GZF_vida_nominal_horas,2), " en horas")  
        elif GZF_carga_equivalente_2 > GZF_carga_equivalente_1:
            GZF_carga_equivalente_fs = GZF_carga_equivalente_2 * GZF_Fs
            "vida en millones de revoluciones"
            GZF_vida_nominal =  pow(GZF_C_basica / GZF_carga_equivalente_fs, GZF_b)
            print(round(GZF_vida_nominal,2), " de vida en millones de revoluciones")
            "vida en horas"
            GZF_vida_nominal_horas = (1000000/(60*GZF_RPM)) * GZF_vida_nominal
            print(round(GZF_vida_nominal_horas,2), " de vida en horas")

        

def GZF_rodamiento(GZF_tipo):
    os.system('cls')
    if GZF_tipo == 1:
        GZF_bucle = 1
        while GZF_bucle ==1:
            print("RODAMIENTOS DE BOLAS\n")
            print("\nPrimero seleccionara el tipo de rodamiento que utilizara")
            print("\npresione enter para continuar..")
            ms.getch()
            GZF_b = 3
            GZF_tabla=GZF_cojinete_bolas()
            os.system('cls')
            print("En consiguiente ingrese lo datos que le sean solicitados")
            print("presione enter para continuar..")
            ms.getch()
            os.system('cls')
            GZF_Fr, GZF_Fa, GZF_C_basica, GZF_RPM,GZF_anillo = GZF_datos()
            os.system('cls')
            print("¿Desea utilizar un Factor de servicio?")
            GZF_usar_Fs =  input("Y/N: ")
            if GZF_usar_Fs.upper() == "Y":
                os.system('cls')
                GZF_Fs = GZF_servicio(1)
            else:
                GZF_Fs = 0
            GZF_vida_rodamiento(GZF_tabla, GZF_Fr, GZF_Fa, GZF_C_basica, GZF_RPM,GZF_anillo,GZF_b,GZF_Fs)
            GZF_bucle = GZF_repetir("programa")
    elif GZF_tipo == 2:
        GZF_bucle = 1
        while GZF_bucle == 1:
            print("RODAMIENTOS DE RODILLOS")
            print("\nPrimero seleccionara el tipo de rodamiento que utilizara")
            print("\npresione enter para continuar..")
            ms.getch()
            GZF_b = 10/3
            GZF_tabla=GZF_cojinete_rodillos()
            os.system('cls')
            print("En consiguiente ingrese lo datos que le sean solicitados")
            print("presione enter para continuar..")
            ms.getch()
            os.system('cls')
            GZF_Fr, GZF_Fa, GZF_C_basica, GZF_RPM,GZF_anillo = GZF_datos()
            os.system('cls')
            print("¿Desea utilizar un Factor de servicio?")
            GZF_usar_Fs = input("Y/N: ")
            if GZF_usar_Fs.upper() == "Y":
                os.system('cls')
                GZF_Fs = GZF_servicio(2)
            else:
                GZF_Fs = 0
            GZF_vida_rodamiento(GZF_tabla, GZF_Fr, GZF_Fa, GZF_C_basica, GZF_RPM,GZF_anillo,GZF_b,GZF_Fs)
            GZF_bucle = GZF_repetir("programa")
            


"******************************************************************************************************************************************************************"
#creditos
def GZF_creditos():
    os.system('cls')
    GZF_titulo_creditos =["########################################################",
"#    ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▄ ▀█▀ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀▀█   #",
"#    ▒█░░░ ▒█▄▄▀ ▒█▀▀▀ ▒█░▒█ ▒█░ ░▒█░░ ▒█░░▒█ ░▀▀▀▄▄   #",
"#    ▒█▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▀ ▄█▄ ░▒█░░ ▒█▄▄▄█ ▒█▄▄▄█   #",
"########################################################"]
    for i in range(len(GZF_titulo_creditos)):    
        print(Style.BRIGHT + Fore.GREEN + Back.BLACK +GZF_titulo_creditos[i])
        ti.sleep(1/5)
    os.system('cls')

    for j in range(len(GZF_titulo_creditos)):    
        print(Style.BRIGHT + Fore.WHITE + Back.BLACK + GZF_titulo_creditos[j])
        ti.sleep(1/5)
    os.system('cls')

    for k in range(len(GZF_titulo_creditos)):
        print(Style.BRIGHT + Fore.RED + Back.BLACK + GZF_titulo_creditos[k])
        ti.sleep(1/5)
    os.system('cls')
    
    for l in range(len(GZF_titulo_creditos)):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + GZF_titulo_creditos[l])
        ti.sleep(1/5)

    GZF_integrantes = [
"""********************************************************
*              █▓▒░ 9°B MECATRONICA ░▒▓█               *
********************************************************""",
"""*           █▓▒░ GADDIEL ZAMORA FLORES ░▒▓█            *
********************************************************"""]
    for i in range(len(GZF_integrantes)):
        print(Style.BRIGHT + Fore.WHITE + Back.BLACK + GZF_integrantes[i])
        ti.sleep(1/5)
    
    print("\n presione enter para regresar al menu...")
    ms.getch()
    os.system('cls')


"******************************************************************************************************************************************************************"
#cerrar
def GZF_cerrar():
    GZF_arreglo1 = [
          "██╗░██████╗░██████╗░░█████╗░░█████╗░██╗░█████╗░░██████╗  ██████╗░░█████╗░██████╗░",
          "██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗",
          "██║██║░░██╗░██████╔╝███████║██║░░╚═╝██║███████║╚█████╗░  ██████╔╝██║░░██║██████╔╝",
          "╚═╝██║░░╚██╗██╔══██╗██╔══██║██║░░██╗██║██╔══██║░╚═══██╗  ██╔═══╝░██║░░██║██╔══██╗",
          "██╗╚██████╔╝██║░░██║██║░░██║╚█████╔╝██║██║░░██║██████╔╝  ██║░░░░░╚█████╔╝██║░░██║",
          "╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝",
          " ",
          "██╗░░░██╗██╗░██████╗██╗████████╗░█████╗░██████╗░███╗░░██╗░█████╗░░██████╗██╗",
          "██║░░░██║██║██╔════╝██║╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔════╝██║",
          "╚██╗░██╔╝██║╚█████╗░██║░░░██║░░░███████║██████╔╝██╔██╗██║██║░░██║╚█████╗░██║",
          "░╚████╔╝░██║░╚═══██╗██║░░░██║░░░██╔══██║██╔══██╗██║╚████║██║░░██║░╚═══██╗╚═╝",
          "░░╚██╔╝░░██║██████╔╝██║░░░██║░░░██║░░██║██║░░██║██║░╚███║╚█████╔╝██████╔╝██╗",
          "░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═════╝░╚═╝"]

    for j in range(1,2):
        os.system('cls')
        for i in range(len(GZF_arreglo1)):
            print(Style.BRIGHT + Fore.BLUE + Back.BLACK +GZF_arreglo1[i])
            ti.sleep(0.3)
    ti.sleep(1/2)
    print(" ")
    GZF_arreglo2= ["""█░█ █░█ █▀▀ █░░ █░█ ▄▀█   █▀█ █▀█ █▀█ █▄░█ ▀█▀ █▀█   ▀ ▀▄""",
"""▀▄▀ █▄█ ██▄ █▄▄ ▀▄▀ █▀█   █▀▀ █▀▄ █▄█ █░▀█ ░█░ █▄█   ▄ ▄▀"""]
    for i in range(len(GZF_arreglo2)):
        print(Style.BRIGHT + Fore.GREEN + Back.BLACK +GZF_arreglo2[i])
        ti.sleep(0.3)
    
    print("\npresione enter para terminar el programa...")
    ms.getch()
    GZF_cerrar = 0
    return GZF_cerrar


"******************************************************************************************************************************************************************"
def main():
    GZF_sesion_activa = 1
    GZF_perfil_activo = " "
    GZF_menu = ["0.- Bienvenida","1.- Calculos del proyecto","2.- Calculador de resistencias","3.- Vida de un rodamiento","4.- Creditos","5.- Cerrar sesion y salir"]

    GZF_nombres = ["Administrador","Gaddiel Zamora Flores","Heydi Esmeralda Hernandez Flores","Erick de Jesus Lopez Sierra","Tlatzy Guadalupe Hernandez Hernandez","Jorge Reynaldo Rodriguez Flores"]
    GZF_usuarios = ["Admin","Gadi710","HEYDI_2002","ejls2002","Tlaltzy734","JorgeRey"]
    GZF_contraseñas = ["12345","GZF#0710","@ESEL300520","Chucho&2","Sere$1234","J0rgeRe&"]
    
    GZF_perfil,GZF_salida = GZF_sesion(GZF_usuarios,GZF_contraseñas)
    GZF_perfil_activo = GZF_nombres[GZF_perfil]

    if GZF_salida == 1:
        GZF_sesion_activa = 0
    else:
        GZF_sesion_activa = 1

    while GZF_sesion_activa == 1:
        print("\nMENU DE PROGRAMAS\n")
        for i in range(len(GZF_menu)):
            print(GZF_menu[i])
            ti.sleep(1/4)
        print()
        GZF_programa = int(input(GZF_perfil_activo+""" seleccione la opcion que desea utilizar
- - -> """))

        if GZF_programa  == 0:#seleccion 0: bienvenida al programa
            GZF_bienvenida()
            
        elif GZF_programa  == 1:#seleccion de programa 1: calculos de proyecto
            GZF_bucle = 1
            while GZF_bucle == 1:
                for i in range(1,6):
                    os.system('cls')
                    print("Bienvenido a los calculos del proyecto")
                    ti.sleep(1/5)
                    os.system('cls')
                print("Bienvenido a los calculos del proyecto")
                print("\nMENU\n")
                GZF_menu_proyecto=["1.- Relacion de engranajes y poleas","2.- razon de cambio de temperatura", "3.- regresar menu principal"]
                for i in range(len(GZF_menu_proyecto)):
                    print(GZF_menu_proyecto[i])
                    ti.sleep(1/5)
                print()
                GETH_opcion = int(input("Seleccione los calculos que desea utilizar: "))
                os.system('cls')

                if GETH_opcion == 3:
                    GZF_bucle = 0
                else:
                    calculos_proyecto(GETH_opcion)
                    GZF_bucle=1

            GZF_sesion_activa = 1
           
        elif GZF_programa  == 2:#seleccion de programa 2: resistencias
            GZF_bucle = 1
            while GZF_bucle == 1:
                for i in range(1,6):
                    os.system('cls')
                    print("Bienvenido al calculo de resistencias")
                    ti.sleep(1/5)
                    os.system('cls')
                print("Bienvenido al calculo de resistencias\n")
                print("\nMENU\n")
                GZF_menu_resistencias=["1.- Resistencias de 4 bandas", "2.- Resistencias de 5 bandas","3.- Regresar menu principal"]
                for i in range(len(GZF_menu_resistencias)):
                    print(GZF_menu_resistencias[i])
                    ti.sleep(1/5)
                print()
                GZF_tipo = int(input("Ingrese el numero de su seleccion: "))
                os.system('cls')
                if GZF_tipo == 3:
                    GZF_bucle = 0
                else:
                    GZF_resistencias(GZF_tipo)
                    GZF_bucle=1
            GZF_sesion_activa = 1
            
        elif GZF_programa  == 3:#seleccion de programa 3: rodamientos
            GZF_bucle = 1
            while GZF_bucle == 1:
                for i in range(1,6):
                    os.system('cls')
                    print("Bienvenido al calculo de vida de rodamientos")
                    ti.sleep(1/5)
                    os.system('cls')
                print("Bienvenido al calculo de vida de rodamientos")
                print("\nMENU\n")
                GZF_menu_rodamientos = ["1.- Rodamientos de bolas","2.- Rodamientos de cilindros","3.- Regresar al menu principal"]
                for i in range(len(GZF_menu_rodamientos)):
                    print(GZF_menu_rodamientos[i])
                    ti.sleep(1/5)
                print()
                GZF_tipo = int(input("Ingrese el numero de su seleccion: "))
                if GZF_tipo ==3:
                    GZF_bucle = 0
                else:
                    GZF_rodamiento(GZF_tipo)
                    GZF_bucle = 1
            os.system('cls')
            GZF_sesion_activa = 1

        elif GZF_programa  == 4:
            #credistos listos
            GZF_creditos()
            
        elif GZF_programa  == 5:
            #cierre de programa listo
            GZF_sesion_activa = GZF_cerrar()     

if __name__ == "__main__":
    main()
