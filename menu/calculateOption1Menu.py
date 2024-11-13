from formula.logic import calcular_propina,calcular_total_con_propina
import os
import keyboard
def design():
    from menu.mainMenu  import design as designPrincipal1
    from menu.calculateOption3Menu import design as designOpcion3
    opcion = 1
    while opcion:
        print(f"""
        =============================================
                    Cálculo de Propina
        =============================================""")
        try:
            keyboard.is_pressed('ctrl+c')
            total = float(input("\tIngrese el monto total de la cuenta: $"))
            if(total < 0):
                raise ValueError()
            porcentaje =float(input("\tIngrese el porcentaje de propina (por ejemplo: 10,15,20):"))
            if(porcentaje < 0):
                raise ValueError()
            propina = calcular_propina(total,porcentaje)
            total_a_pagar=calcular_total_con_propina(total,propina)
            print(f"""
        =============================================
        La propina calculada es: ${propina}
        El total a pagar es: ${total_a_pagar}
        =============================================     
            """)
            opcion = int(input("-¿Deseas calcular nuevamente? (1-S/0-N) "))
            if opcion == 0:
                os.system('cls')
                designOpcion3()
            elif opcion == 1:
                os.system('cls')
                designPrincipal1()
        except ValueError:
            input("\n-Los datos utilizados no son validos,¡Presione Enter para continuar y seleccione una opción del menú!.")
            os.system('cls')
        except KeyboardInterrupt:
            input("\n-Señor usuario no presione 'Ctrl + C',¡Presione Enter para continuar y seleccione una opción del menú!.")
            os.system('cls')
