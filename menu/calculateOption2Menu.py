from formula.logic import calcular_propina,calcular_total_con_propina,monto_por_persona
import os
def design():
    from menu.mainMenu  import design as designPrincipal1
    from menu.calculateOption3Menu import design as designOpcion3
    opcion = 2
    while opcion:
        print(f"""
        =============================================
            Dividir Cuenta entre Varias Personas
        =============================================""")
        total = float(input("\tIngrese el monto total de la cuenta: $"))
        porcentaje =float(input("\tIngrese el porcentaje de propina (por ejemplo: 10,15,20):"))
        propina = calcular_propina(total,porcentaje)
        personas=float(input("\tIngrese el número de personas: "))
        print(f"""
        =============================================
        La propina calculada es: $ {round(propina)}
        El total a pagar es: $ {calcular_total_con_propina(total,propina)}
        Monto por persona: ${monto_por_persona(total,propina,personas)}
        =============================================    
        """)
        opcion = int(input("\t¿Deseas calcular nuevamente? (1-S/0-N) "))
        if opcion == 0:
            os.system('cls')
            designOpcion3()
            break 
        elif opcion ==1:
            os.system('cls')
            designPrincipal1()
              
    