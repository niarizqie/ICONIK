import numpy as np
import pandas as pd
from getpass import getpass
import os


def select_main():
    print('Please enter username and pass')
    name = input('Name: ')
    password = input('password: ')
    daftar_object = open('username.txt', 'r')

    if f'{name}#${password}' in daftar_object.read():
        print('Login Berhasil - lets play!!!!!')
        print('''=============================================================================
Aturan permainan:
   Pemain akan memiliki score awal 100
   Pemain akan menebak angka yang digenerate oleh komputer
   Nilai yang dibuat oleh komputer berkisar antara 10 - 20
   Jika tebakan salah, maka akan dilakukan penalti sebesar 10pts
   Jika yang dimasukkan bukanlah angka, anan diberlakukan penalti sebesar 20pts
        
   GOOD LUCK WITH THE GAME!!!
=============================================================================
        ''')
        play_the_game(name)
    else:
        print('Username dan passowrd anda salah')


def play_the_game(name):
    rand_guess = np.random.randint(0, 20)
    i = 10
    print(rand_guess)

    while i > 0:
        score = i * 10

        print(f'''
silahkan masukkan angka acak antara 1 - 20
angka adalah bilangan ANGKA
score saat ini {score}
''')
        user_guess = input('masukkan angka: ')
        try:
            int(user_guess)
            input_type = 'number'
        except:
            input_type = 'text'

        if input_type == 'number':
            if (int(user_guess) == rand_guess) :
                print(f'success menebak, score anda adalah {score}')
                save_score(name, score)
                i = -1
            else:
                i -= 1
                if int(user_guess) > rand_guess:
                    word = 'BESAR'
                else:
                    word = 'KECIL'

                if i == 0:
                    print('----- Tebakan anda terlalu BESAR. GAME OVER, your score is 0')
                else:
                    print(f'----- Tebakan anda terlalu {word}. Penalti 10.  silahkan coba lagi ----')
        else:
            i -= 2
            if i == 0:
                print('----- Anda tidak memasukkan STR. Penalti 20. GAME OVER, your score is 0')
            else:
                print('----- Anda tidak memasukkan STR. Penalti 20. Silahkan coba lagi')


def save_score(name, score):
    if ~os.path.exists('score.txt'):
        open('score.txt', 'w').close()

    score_object = open('score.txt', 'r').read().split('\n')[:-1]
    data_user = [val.split('#$')[0] for val in score_object]
    data_score = [int(val.split('#$')[1]) for val in score_object]

    if name in data_user:

        idx = data_user.index(name)
        if score > data_score[idx]:
            data_score[idx] = score
            text = [f'{i[0]}#${i[1]}\n' for i in zip(data_user, data_score)]
            text_con = ''
            for val in text:
                text_con += val

            open('score.txt', 'w').close()

            score_object = open('score.txt', 'a')
            score_object.write(text_con)

            print('your score has been updated')
        elif score < data_score[idx]:
            print('your previous score is higher, score will not saved')
    else:
        score_object = open('score.txt', 'a')
        score_object.write(f'{name}#${score}\n')
        print('Score saved Success')


def select_daftar():
    name = input('Name: ')
    password = input('pasword: ')

    if ~os.path.exists('username.txt'):
        open('username.txt', 'w').close()

    daftar_object = open('username.txt', 'r')

    if f'{name}#${password}' in daftar_object.read():
        print('Account has already exists')
    else:
        print('Registration Success')
        daftar_object = open('username.txt', 'a')
        daftar_object.write(f'{name}#${password}\n')

def select_highscore():


    score_object = open('score.txt', 'r').read().split('\n')[:-1]
    data_user = [val.split('#$')[0] for val in score_object]
    data_score = [int(val.split('#$')[1]) for val in score_object]

    score_df = pd.DataFrame(data=np.c_[data_user, data_score], columns=['user', 'score'])
    score_df = score_df.sort_values(by=['score']).reset_index(drop=True)
    score_df = score_df.iloc[:5]
    print(f'**  username \t\t score  **')
    print('*************************')
    [print(f'** {val[0]} \t\t\t {val[1]} **') for val in score_df.values]
    print('*************************')



def select_keluar():
    print('Thank you for playing')
    quit()


def select_out():
    print('not an option')


program_to_run = {'1': select_main,
                  '2': select_daftar,
                  '3': select_highscore,
                  '4': select_keluar}

while True:
    try:
        print('''
*****************************
PERMAINAN TEBAK ANGKA
*****************************
menu:

1. Main
2. Daftar
3. High Score
4. keluar
''')

        select = input('Pilihan anda: ')
        program_to_run[str(select)]()
    except:
        'your input is not in option, please select between 1 - 4'
