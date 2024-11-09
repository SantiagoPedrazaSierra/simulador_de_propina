from menu.calculateOption1Menu  import design as designOpcion1
from menu.calculateOption2Menu import design as designOpcion2
from menu.calculateOption3Menu import design as designOpcion3
def design():
   
        print(f"""
        =====================================================
                      SIMULADOR DE PROPINA
        ======================================================   
        1. Calcular propina y total a pagar
        2. Calcular total a pagar divido entre varias personas
        3. Salir
        ======================================================
        """)
        while True:
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
        