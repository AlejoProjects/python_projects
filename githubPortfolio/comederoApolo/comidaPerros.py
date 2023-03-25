#pequeño script para obtener diferente información sobre la comida de mi perro
def pepasOcupanVolumen(volumen0,volumen):
            pepas = round(volumen0/volumen)
            print(f'para un volumen de {volumen0}cm³ se necesitan {pepas} pepas')
            return pepas
        
def pesoPorVolumen(volumen0,peso):
            pesoT = round(volumen0*peso)
            print(f'para un volumen de {volumen0}cm³ pesa {pesoT} gramos ')
            return pesoT
def run():
    print('hello')
    if __name__ == '__main__':
        run()
    
    