from menu.calculateOption1Menu  import design as designOpcion1
from menu.calculateOption2Menu import design as designOpcion2
from menu.calculateOption3Menu import design as designOpcion3
import os
import keyboard
def design():
        while True:
                try:

                        print(f"""
        =====================================================
                        SIMULADOR DE PROPINA
        ======================================================   
        1. Calcular propina y total a pagar
        2. Calcular total a pagar divido entre varias personas
        3. Salir
        ======================================================
        """)
        
                        keyboard.is_pressed('ctrl+c')
                        opcion = int(input("Por favor, elige una opción (1-3): "))
                        if opcion == 1:
                                designOpcion1()  
                                break  
                        elif opcion == 2:
                                designOpcion2() 
                                break                
                        elif opcion == 3:
                                designOpcion3()
                                break  
                        else:
                                print("\nOpción no válida. Por favor, ingresa un número entre 1 y 3.\n")        
                except ValueError:
                        input("\n-Los datos utilizados no son validos,¡Presione Enter para continuar y seleccione una opción del menú!.")
                        os.system('cls')
                except KeyboardInterrupt:
                        input("\n-Señor usuario no presione 'Ctrl + C',¡Presione Enter para continuar y seleccione una opción del menú!.")
                        os.system('cls')
