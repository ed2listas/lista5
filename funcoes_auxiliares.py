import sys
import os

def lerString():
    new = ""
    str = sys.stdin.readline()
    for i in str:
        if i != '\n':
            new = new + i
    return new

def lerChar():
    str = sys.stdin.readline()
    return str[0]

def lerInteger():
    #print("%s" % msg)
    valor = sys.stdin.readline()
    # validar para ver se é inteiro
    return int(valor);

def menuComOpcao(opcoes=["inserir","retirar","finalizar"]):
    opcao = 0
    nro = 1
    print("==========================================");
    print("|         >>>>>>>>> Menu <<<<<<<<<       |");
    for txt in opcoes:
        if txt == opcoes[-1]:
            nro = 0
        print("| %d - %-35s|" % (nro, txt));
        nro += 1
    print("==========================================");
    print("Sua opcao: ");
    opcao = lerInteger()
    return opcao;

def isInteger(num):
    nums = "0123456789"
    size = len(num)
    if num[0] == '-':
        start = 1
    else:
        start = 0
    for i in range(start, size):
        if(not(num[i] in nums)):
            return False
    return True

def isAlpha(text, ex=""):
    letters = "abcdefghijklmnopqrstuvxyz"+ex
    text = text.lower()
    size = len(text)

    for i in range(0, size):
        if(not(text[i] in letters)):
            return False
    return True

def novaLinha(tam, x):
    linha = []
    for i in range(0, tam):
        linha.append(x)
    return linha

def novaMatriz(lins, cols, x):
    matriz = []
    if ((lins < 1) or (cols < 1)):
        return None
    for i in range(0, lins):
        matriz.append(novaLinha(cols, x))
    return matriz

def pausar(msg="Aperte enter para continuar"):
    print("%s" % msg)
    aux = sys.stdin.readline()

def limparTela():
    os.system('clear')

def gotoxy(x,y):
    print("\033[{};{}H".format(y, x), end="")
def moveUp(x):
    print("\033[{}A".format(x), end="")
def moveDown(x):
    print("\033[{}B".format(x), end="")
def moveRight(x):
    print("\033[{}C".format(x), end="")
def moveLeft(x):
    print("\033[{}D".format(x), end="")

class Cor:
    fore = {
        "BLACK":30,
        "RED":31,
        "GREEN":32,
        "YELLOW":33,
        "BLUE":34,
        "MARGENTA":35,
        "CYAN":36,
        "WHITE":37,
        "NORMAL":39,
    }
    back = {
        "BLACK":40,
        "RED":41,
        "GREEN":42,
        "YELLOW":43,
        "BLUE":44,
        "MAGENTA":45,
        "CYAN":46,
        "WHITE":47,
        "NORMAL":49
    }
    style = {
        "BRIGHT":1,
        "DIM":2,
        "NORMAL":22,
        "RESETALL":0,
        "UNDERLINE":4,
        "BLINKSLOW":5,
        "BLINKRAPID":6,
        "ITALIC":3,
        "NEGATIVE":7
    }

def printColorido(texto, cor, back="NORMAL", style="NORMAL"):
    print("\033[{}m".format(Cor.fore.get(cor.upper())), end="")
    print("\033[{}m".format(Cor.back.get(back.upper())), end="")
    print("\033[{}m".format(Cor.style.get(style.upper())), end="")
    print(texto, end="")
    print("\033[{}m".format(Cor.style.get("RESETALL")), end="")
