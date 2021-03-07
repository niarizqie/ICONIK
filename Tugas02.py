import numpy as np
import pandas as pd
import getpass as gp


def select_main():
    print('Please enter username and pass')
    name = input('Name: ')
    password = gp.getpass('password: ')
    daftar_object = open('username.txt', 'r')

    if f'{name}#${password}' in daftar_object.read():
        print('success - lets play!')
        play_the_game(name)
    else:
        main('username and pass salah ...')


def play_the_game(name):
    rand_guess = np.random.randint(0, 20)
    i = 10
    m = ''
    print(rand_guess)
    while i > 0:
        score = i * 10
        print(f'''
silahkan masukkan angka acak antara 1 - 20
angka adalah bilangan bulat
score saat ini {score}
{m}
''')
        user_guess = input('masukkan angka: ')

        try:
            g = int(user_guess)
            if g == rand_guess:
                m = f'success menebak, score anda adalah {score}'
                save_score(name, score)
                i = -1
            elif g > rand_guess and (g - rand_guess) < 5:
                m = '----- Angka anda sudah mendekati tapi masih lebih besar ----'
                i -= 1
            elif g < rand_guess and (rand_guess - g) < 5:
                m = '----- Angka anda sudah mendekati tapi masih lebih kecil ----'
                i -= 1
            elif g > rand_guess:
                m = '----- Angka anda terlalu besar ----'
                i -= 1
            elif g < rand_guess:
                m = '----- Angka anda terlalu kecil ----'
                i -= 1
            else:
                m = '----- coba lagi ----'
                i -= 1

        except:
            m = '----- hanya boleh angka kurang 20 ----'
            i -= 2
    main(m)


def save_score(name, score):
    daftar_object = open('score.txt', 'a')
    daftar_object.write(f'{name}, {score}\n')
    print('Score saved Success')


def select_daftar():
    daftar_object = open('username.txt', 'a')
    name = input('Name: ')
    password = gp.getpass('pasword: ')
    daftar_object.write(f'{name}#${password}\n')
    daftar_object.close()
    main('Registration Success')


def select_highscore():
    temp = pd.read_csv('score.txt', header=None)
    temp.columns = ['name', 'score']
    temp = temp.sort_values(['score'])
    temp = temp.iloc[:5]

    print(temp.columns[0], '\t', temp.columns[1])
    print('*************************')
    [print(f'{val[0]}\t\t{val[1]}') for val in temp.values]
    t = input('1 :kembali, 2: keluar')
    if t == '1':
        main('')
    elif t == '2':
        select_keluar()
    else:
        main('pilih yng benar')


def select_keluar():
    print('Thank you for playing')
    exit()


def select_out():
    print('not an option')


def program_to_run(n) :
    if n == '1':
        select_main()
    elif n == '2':
        select_daftar()
    elif n == '3':
        select_highscore()
    elif n == '4':
        select_keluar()
    else:
        main('Tidak ada dalam pilihan')

# while loop:
#    try:
def main(message):
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
    if message != '':
        print(message)
    select = input('Pilihan anda: ')
    program_to_run(select)


#    except:
#        'err not an option'

main('')
