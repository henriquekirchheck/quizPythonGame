from ssl import OP_NO_RENEGOTIATION


def createFile(path:str):
    try:
        if(path.find('.txt') == -1):
            path = f'{path}.txt'
        file = open(path, 'x')
        file.close()
    except FileExistsError:
        return 'Esse arquivo já existe'

def addLinetoFile(info:str ,path:str):
    if(path.find('.txt') == -1):
        path = f'{path}.txt'
    if(info.find('\n') == -1):
        info = f'{info}\n'

    try:
        file = open(path, 'a')
        file.write(info)
        file.close
    except:
        print('Esse arquivo não existe')

def readFile(path:str):
    try:
        if(path.find('.txt') == -1):
            path = f'{path}.txt'

        uplines = list()

        file = open(path, 'r')
        lines = file.readlines()

        for x in lines:
            y = x.replace('\n', '')
            uplines.append(y)

        file.close
        return(uplines)
    except OSError:
        print('Esse arquivo não existe')

def removeLinefromFile(index:int, path:str):
    try:
        arquivo = open(path, 'r')
        conteudo = arquivo.readlines()
        conteudo.pop(index)

        arquivo = open(path, 'w')
        arquivo.writelines(conteudo)

        arquivo.close()
    except IndexError:
        print('O Index é invalido ou o arquivo esta vazio')


def removeTextfromFile(path:str):
    try:
        arquivo = open(path, 'r')
        conteudo = arquivo.readlines()
        if(conteudo != []):
            arquivo = open(path, 'w')
            arquivo.close()
        else:
            print('O arquivo já esta vazio')
    except:
        print('Esse arquivo não existe')

def recreateFile(lista:list, path:str):
    novalista = list()
    if(path.find('.txt') == -1):
        path = f'{path}.txt'
    try:
        for x in lista:
            y = f'{x}\n'
            novalista.append(y)


        arquivo = open(path, 'w')
        arquivo.writelines(novalista)
        arquivo.close()
    except:
        print('Ocorreu um erro, provavelmente o arquivo não existe')


if __name__ == '__main__':
    createFile('D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt')
    addLinetoFile('Teste 1', 'D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt')
    addLinetoFile('Teste 2', 'D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt')
    print(readFile('D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt'))
    #removeLinefromFile(0, 'D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt')
    #print(readFile('D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt'))
    #removeTextfromFile('D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt')
    #print(readFile('D:/Programação/Curso-em-Video-Python/desafio/utils/tests/list.txt'))