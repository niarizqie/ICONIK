import numpy as np
import pandas as pd

def select_main():
    print('Please enter username and pass')
    name = input('Name: ')
    password = input('password: ')
    daftar_object = open('username.txt', 'r')

    if f'{name}#${password}' in daftar_object.read():
        print('success - lets play!')
        play_the_game(name)
    else:
        print('Salah password dan input')
        
    

def play_the_game(name):

    score = 100
    rand_guess = np.random.randint(0,20)
    i = 10
    print(rand_guess)
    while i>0:
        score = i*10
        print(f'''
silahkan masukkan angka acak antara 1 - 20
angka adalah bilangan bulat
score saat ini {score}
''')
        user_guess = input('masukkan angka: ')
        
        if int(score) == 10:
            print('GAMEOVER')
            save_score(name, score = 0)
            i = -1
            
        elif int(user_guess) > 20:
            print('Angka yang anda Masukan Salah')
            i -= 1
        elif int(user_guess) == rand_guess:
            print(f'success menebak, score anda adalah {score}')
            save_score(name, score)
            i = -1
        elif int(user_guess) > rand_guess:
            print('Angka Anda Terlalu Besar')
            i -= 1
        elif int(user_guess) < rand_guess:
            print ('Angka Anda Terlalu Kecil')
            
            i-= 1
    
       
      
       
   
     

def save_score(name, score):
    daftar_object = open('score.txt', 'a')
    daftar_object.write(f'{name}, {score}\n')
    print('Score saved Success')


def select_daftar():
    daftar_object = open('username.txt', 'a')
    name = input('Name: ')
    password = input('pasword: ')
    daftar_object.write(f'{name}#${password}\n')
    print('Registration Success')

def select_highscore():
    temp = pd.read_csv('score.txt', header=None)
    temp.columns = ['name', 'score']
    temp = temp.sort_values(['score'])
    temp = temp.iloc[:5]

    print(temp.columns[0],'\t', temp.columns[1])
    print('*************************')
    [print(f'{val[0]}\t\t{val[1]}') for val in temp.values]

def select_keluar():
    print('Thank you for playing')
    quit()
    

def select_out():
    print('not an option')


program_to_run = {1: select_main,
                  2: select_daftar,
                  3: select_highscore,
                  4: select_keluar
                }

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
        program_to_run[int(select)]()
       
        
    except:
        'err not an option'