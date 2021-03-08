import numpy as np
import pandas as pd
import getpass as gp
import time
from prettytable import PrettyTable as pt
import os.path
from os import path


def select_main(menu_):
    print('Please enter username and pass')
    
    name =''
    password =''
    while name=='' :   
        name = input('Name: ')
        if len(name) == 0 :
            print("username tidak boleh kosong ")
    
    while password=='' :   
        password = gp.getpass('password: ')
        if len(password) == 0 :
            print("password tidak boleh kosong ")

    if not path.exists("user_data.txt"):
        open("user_data.txt", 'w').close()

    file_registrasi = open("user_data.txt", "r+")
    data_registrasi = file_registrasi.readlines()
    file_registrasi.close()
    #menggabungkan user dan password
    userpassword_ = (name+"#$"+password+"\n")
    
    #membuat list username
    users_=[datauser.split("#$",1)[0] for datauser in data_registrasi]
    
    #mengecek user d list username
    cek_user = name in users_ 
    
    #untuk mengecek userpassword ada di list yang sudah ter registrasi
    cek_user_pass = userpassword_ in data_registrasi
    
    #authentification
    if menu_ == "main" :
        if cek_user_pass== True:
            play_the_game(name)
        else :   
            #print(cek_user)
            if cek_user== True:
                main('username and pass salah ...')
                print("Password kamu salah")
                #login()
            else:
                main("***** Kamu belum Daftar nih... Daftar dulu yaaa ***** ")
    else :
        if cek_user== True:
           main("***** Username " + name + " Sudah ada, Silahkan pilih Username yang lainnya *****")
        else :
            select_daftar(name,password)

# =============================================================================
#     daftar_object = open('username.txt', 'r')
#     print(daftar_object)
#     
#     if f'{name}#${password}' in daftar_object.read():
#         print('success - lets play!')
#         play_the_game(name)
#     else:
#         main('username and pass salah ...')
# 
# =============================================================================

def play_the_game(name):
    rand_guess = np.random.randint(1, 20)
    i = 10
    m = ''
    print("LOGIN BERHASIL !!!")
    print("Permainan Segera dimulai .... ")
    #loading
    time.sleep(3)
    print(f'''Silahkan masukkan angka acak antara 1 - 20
[WARNING !!!] Inputan harus berupa ANGKA bilangan bulat''')   
    print(rand_guess)
    win = 0
    while i > 0:
        score = i * 10
        print(f'''
Score Anda saat ini  = {score}
{m}
''')

        user_guess = input('Masukkan angka: ')

        try:
            g = int(user_guess)
            if g == rand_guess:
                m = f'Berhasil !!!, score anda adalah {score}'
                save_score(name, score)
                win = 1
                i = -1
            elif g >= 21:
                m = '----- angka yg anda masukan lebih dari range ----'
                i -= 1
            elif g <= 0:
                m = '----- angka yg anda masukan kurang dari range ----'
                i -= 1
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
            m = '----- Hanya boleh ANGKA, Score Anda dikurangi 20 :( ----'
            i -= 2

    if i < 1 and win != 1:
        m = '----- GAME OVER! ---- \n Coba Lagi...'
    main(m)


def save_score(name, score):
    daftar_object = open('user_score.txt','a')
    daftar_object.write(f'{name}#${score}\n')
    daftar_object.close()
    print('Score saved Success')


def select_daftar(name,password):
    daftar_object = open('user_data.txt','a')
    #name = input('Name: ')
    #password = gp.getpass('pasword: ')
    daftar_object.write(f'{name}#${password}\n')
    daftar_object.close()
    main('PENDAFTARAN BERHASIL')


def select_highscore():
    print("\n HIGH SCORE")

    if path.exists('user_score.txt'):
        highscore_list = open('user_score.txt','r+')

        #split highscore
        high = highscore_list.read().split("\n")
        high.remove("")
        highscore_list.close()

        user__ = [high_score.split("#$",1)[0] for high_score in high]
        list_user = set(user__)

        score__ = [high_score.split("#$",1)[1] for high_score in high]

        dic = {}
        for x,y in zip(user__,score__):
            dic.setdefault(x,[]).append(y)

        list_user = []

        for i in dic.keys():
            list_user.append(i)

        list_score = []

        for i in dic.values():
            for j in range(0,len(i)):
                i[j] = int(i[j])
            list_score.append(max(i))

        highscore_table = pt()

        highscore_table.add_column("Username", list_user)
        highscore_table.add_column("Score", list_score)

        #sorting
        highscore_table.sortby = "Score"
        highscore_table.reversesort = True

        #top 10 high score
        print(highscore_table.get_string(start=0,end=10))
        highscore_list.close()
        print('1 :kembali, 2: keluar')
        t = input('Pilihan anda: ')
        if t == '1':
            main('')
        elif t == '2':
            select_keluar()
        else:
            main('pilih yng benar')
    else:
        main('No high score Data')

    
# =============================================================================
#     temp = pd.read_csv('user_score.txt', header=None)
#     temp.columns = ['name','score']
#     temp = temp.sort_values(['score'])
#     temp = temp.iloc[:5]
# 
#     print(temp.columns[0], '\t', temp.columns[1])
#     print('*************************')
#     [print(f'{val[0]}\t\t{val[1]}') for val in temp.values]
#     t = input('1 :kembali, 2: keluar')
#     if t == '1':
#         main('')
#     elif t == '2':
#         select_keluar()
#     else:
#         main('pilih yng benar')
# =============================================================================


def select_keluar():
    print()
    print('Thank you for playing')
    #exit()


def select_out():
    print('not an option')


def program_to_run(n) :
    if n == '1':
        select_main("main")
    elif n == '2':
        select_main("daftar")
        
        #select_daftar()
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
Menu:
1. Main
2. Daftar
3. High Score
4. Keluar
''')
    if message != '':
        print(message)
    select = input('Pilihan anda: ')
    program_to_run(select)


#    except:
#        'err not an option'


print('''
*****************************
PERMAINAN TEBAK ANGKA
*****************************''')
main('')
