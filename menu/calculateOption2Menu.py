from formula.logic import calcular_propina,calcular_total_con_propina,monto_por_persona
import os
import keyboard
def design():
    from menu.mainMenu  import design as designPrincipal1
    from menu.calculateOption3Menu import design as designOpcion3
    opcion = 2
    while opcion:
        print(f"""
        =============================================
            Dividir Cuenta entre Varias Personas
        =============================================""")
        try:
            keyboard.is_pressed('ctrl+c')
        
            total = float(input("\tIngrese el monto total de la cuenta: $"))
            if (total < 0):
                raise ValueError()
            porcentaje =float(input("\tIngrese el porcentaje de propina (por ejemplo: 10,15,20):"))
            if (porcentaje < 0):
                raise ValueError()
            personas=float(input("\tIngrese el número de personas: "))
            if (personas < 0):
                raise ValueError()
            propina = calcular_propina(total,porcentaje)
            totalMasPropina=calcular_total_con_propina(total,propina)
            totalPorpersona=monto_por_persona(total,propina,personas)
            print(f"""
        =============================================
        La propina calculada es: $ {propina}
        El total a pagar es: $ {totalMasPropina}
        Monto por persona: ${ totalPorpersona}
        =============================================    
            """)
            opcion = int(input("\t¿Deseas calcular nuevamente? (1-S/0-N) "))
            if opcion == 0:
                os.system('cls')
                designOpcion3()
            elif opcion ==1:
                os.system('cls')
                designPrincipal1()
        except ValueError:
            input("\n-Los datos utilizados no son validos,¡Presione Enter para continuar y seleccione una opción del menú!.")
            os.system('cls')      
        except KeyboardInterrupt:
            input("\n-Señor usuario no presione 'Ctrl + C',¡Presione Enter para continuar y seleccione una opción del menú!.")
            os.system('cls')