def find_card(id_card):
    print(id_card)
    
    coordinates = "x, y"
    # logica para encontrar una carta
    
    numero_de_cartas = 4
    
    for numero in numero_de_cartas:
        
        if (find_card_color(numero) and find_pills(numero)):
            return coordinates
    
    # cargar png?
    
def find_card_color():
    pass

def find_pills():
    pass