from sys import exit
import random
import time

print("bem vindo a Dungeon\n")

def board():
    caracter = []
    counter = 0
    while counter < 100:
        if  counter >= 0 and counter < 5:
            caracter.append("*")
        elif counter >= 5 and counter < 15:
            caracter.append("@")
        elif counter >= 15 and counter < 35:
            caracter.append("#")
        elif counter >= 35 and counter < 65:
            caracter.append("^")
        elif counter >= 65 and counter < 100:
            caracter.append("_")
        counter += 1
        
    matrix = []
    for k in range(10):
        matrix.append(["0"]*10)
    for i in range(10):
        for j in range(10):
            matrix[i][j] = random.choice(caracter)
    matrix[0][0] = "T"
    matrix[9][9] = "P"

    return matrix
    

def movement(matrix,string, lista):
    for l in range(10):
        for c in range(10):
            if matrix[l][c] == "P":
                x,y = l,c

    if string=="l" or string=="L":
        return matrix, lista

    if string=="w" or string=="W":
        if (x) == (9) and y == 9:
            lista[0] = matrix[x-1][y]
            matrix[ 9 ][9] = " "
            matrix[x-1][y] = "P"
            return matrix, lista
        elif x == 0:
            print("\nVocê está na borda Norte\n")
            return matrix, lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x-1][y]
            matrix[x-1][y] = "P"
            if (x-1,y) == (0,0):
                victory()
                time.sleep(2)
                return exit()
            else:
                return matrix, lista
        
    elif string=="s" or string=="S":
        if x == 9:
            print("\nVocê está na borda Sul\n")
            return matrix,lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x+1][y]
            matrix[x+1][y] = "P"
            return matrix, lista
    
    elif string=="d" or string=="D":
        if y == 9:
            print("\nVocê está na borda Leste\n")
            return matrix,lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x][y+1]
            matrix[x][y+1] = "P"
            return matrix, lista
    
    elif string=="a" or string=="A":
        if (x) == (9) and (y) == (9):
            lista[0] = matrix[x][y-1]
            matrix[ 9 ][9] = " "
            matrix[x][y-1] = "P"
            return matrix, lista
        elif y == 0:
            print("\nVocê está na borda Oeste\n")
            return matrix,lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x][y-1]
            matrix[x][y-1] = "P"
            if (x,y-1) == (0,0):
                victory()
                time.sleep(2)
                return exit()
            else:
                return matrix, lista
    else:
        return matrix, lista


def life_implement(lista,string,life):

    if string == "l" or string == "L":
        life += 20
        if life > 100:
            life = 100
            return life
        else:
            return life
    
    if lista[0] == "^":
        life -= 15
        return life
    elif lista[0] == "#":
        life -= 25
        return life
    elif lista[0] == "@":
        life -= 40
        return life
    elif lista[0] == "*":
        life -= 60 
        return life
    else:
        return life
    
    
def victory():
    print("*"*21)
    print("*    você_venceu    *")
    print("*"*21)


def print_movement(matrix):
    for l in range(10):
        s = ''
        for c in range(10):
            cc = matrix[l][c]
            s += str(cc + "  ")
        print(s)


def chamamento():
    
    a = board()
    status  = str(input("\nDigite seu nome: "))
    l       = [""]
    v       = 100
    potion  = 3

    s4 = str("\n%s; life - %d; pocões - %d.  " %(status, v, potion))
    print(s4)
    print_movement(a)
    while True:
        m = str(input("\nMova-se: W, A, S, ou D  ou recupere vida:L ->>> "))
        print("\n")

        b,L     = movement(a,m,l)
        life    = life_implement(L,m,v)
        v       = life
        if m == "l" or m =="L":
            potion -= 1
        if potion   <= 0:
            potion = 0
        if life     <= 0:
            print("\nvocê perdeu! :( :( :( \n")
            time.sleep(1)
            break
        if m == "exit" or m == "EXIT":
            print("você desistiu")
            time.sleep(1)
            break

        s5 = str("\n%s; life - %d; pocões - %d.  " %(status, life, potion))
        print(s5)
        print_movement(b)
        a = b 
        l = L

chamamento()





