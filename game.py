def new_game(path, numberOfQuestions:int = 4):
    from utils import text, string
    import random
    questionChoices = list()
    choosedQuestions = list()
    alphabet = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = list()
    points = 0
    totalQuestions = 0

    string.line('Quiz legal', totalcaracters=60)

    try:
        questions = text.readFile(path)
        for question in questions:
            question = question.split(';')
            questionChoices.append(question)
        while True:
            if(numberOfQuestions > len(questions)):
                numberOfQuestions -= 1
            else:
                break
        while True:
            question = random.choices(questionChoices)
            question = question[0]
            if(len(choosedQuestions) >= numberOfQuestions):
                break
            if(question in choosedQuestions):
                pass
            else:
                choosedQuestions.append(question)
        del(question,  questions,  questionChoices)
    except FileNotFoundError:
        print('O arquivo não foi encontrado')
    try:
        for index, question in enumerate(choosedQuestions):
            totalQuestions += 1
            print(f'{index + 1}- {question[0]}')
            for options in range(1,(len(question) - 1)): 
                print(f'{alphabet[options]}) {question[options]}')
                alpha.append(alphabet[options])
            answer = str(input(f'Escolha uma opção {alpha}: ')).lower().strip()
            alpha.clear()
            if(answer == question[-1]):
                points += 1
            else:
                points += 0
            string.line(totalcaracters=60)    

        check_score(totalQuestions, points)
    except KeyboardInterrupt:
        print('Obrigado por jogar o quiz')
    except:
        print('Aconteceu algum erro')

    play_again(path, numberOfQuestions)

def check_score(totalQuestions, points):
    from utils import string
    print(f'Você acetou {int((points / totalQuestions) * 100)}% das perguntas')
    string.line(totalcaracters=60)

def play_again(path, numberOfQuestions):
    while True:
        play_choice = str(input('Quer jogar de novo? [S/n]: ')).strip().lower()
        if(play_choice in 'sn'):
            if(play_choice == 's'):
                new_game(path, numberOfQuestions)
            else:
                break
        else:
            print('Digite um valor valido')


path = 'questions.txt'

new_game(path, 2)