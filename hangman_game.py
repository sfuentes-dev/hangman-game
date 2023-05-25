import os
import random

def logo_hangman():
    print('''
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
''')

def image_hangman():
    die0 = '''
   













'''
    die1 = '''
    










        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / \\
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / \\
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / \\
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / \\
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / \\
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / \\
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die11 = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / \\
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10, 11: die11}
    return deaths

def read_word():
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data_words:
        words = [word.strip().upper().replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U') for word in data_words]
    return random.choice(words)

def new_word():
    word = read_word()
    dict_word = {i: letter for i, letter in enumerate(word)}
    discovered = ['- ' for _ in range(len(dict_word))]
    deaths = 0
    letters = [chr(code) for code in range(ord('A'), ord('N')+1)] + ['Ñ'] + [chr(code) for code in range(ord('O'), ord('Z')+1)]
    return word, dict_word, discovered, deaths, letters

def compare_letter(letter, dict_word, discovered):
    fail = True
    for i, char in dict_word.items():
        if char == letter:
            discovered[i] = letter + ' '
            fail = False
    return discovered, fail

def refresh(hangman_deaths, deaths, letters):
    os.system('cls' if os.name == 'nt' else 'clear')
    logo_hangman()
    print('Letras disponibles:', ' '.join(letters))
    print(hangman_deaths.get(deaths))

def play_again():
    while True:
        choice = input('¿Quieres jugar otra vez? (Sí: S, No: N): ').upper()
        if choice == 'S':
            return True
        elif choice == 'N':
            return False
        else:
            print('Opción inválida. Por favor, elige S para sí o N para no.')

def hangman():
    word, dict_word, discovered, deaths, letters = new_word()
    hangman_deaths = image_hangman()
    refresh(hangman_deaths, deaths, letters)
    while deaths < 11:
        if '- ' not in discovered:
            print('¡Felicidades, ganaste!')
            break
        letter = input('Elige una letra: ').strip().upper()
        if letter in letters:
            letters.remove(letter)
            discovered, fail = compare_letter(letter, dict_word, discovered)
            if fail:
                deaths += 1
            refresh(hangman_deaths, deaths, letters)
            print(''.join(discovered))
        else:
            print('Letra inválida. Intenta nuevamente.')
    else:
        print('¡Lo siento, has perdido! La palabra era:', word)
    return play_again()

def main():
    logo_hangman()
    while True:
        if not hangman():
            break

if __name__ == '__main__':
    main()
