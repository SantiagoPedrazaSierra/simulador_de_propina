def calcular_propina(total, porcentaje):
    decimal = porcentaje / 100
    propina= decimal * total
    
    return propina

def calcular_total_con_propina (total, propina):
    return round(total + propina)


def monto_por_persona(total,propina,personas):
    return round(total + propina) / personas 
