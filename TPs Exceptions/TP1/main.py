from exercice1 import divEntier
# Main qui est associé à l'Exercice 1 des Exceptions (fonction divEntier)
if __name__ == '__main__':
    try:
        x = int(input("x : "))
        y = int(input("y: "))
        print(divEntier(x,y))
    # Exception relative à la recursion de y
    except RecursionError:
        if y < 0:
            print("Y doit être positif")
        elif y ==0:
            print("Y ne peut pas être égale à 0")
    # Exception relative à la valeur de y (ici doit être un entier et non un float)
    except ValueError:
        print("Le nombre doit être un nombre entier")
    else:
        divEntier(x,y)


