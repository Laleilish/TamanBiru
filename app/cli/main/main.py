# main.py
<<<<<<< HEAD

from chat.reply import *

=======
import sys
import os
sys.path.append(os.path.abspath('./app/cli/chat/'))
from chat_all import chat_all
from chatProdi import program_studi
>>>>>>> 334470393ad00f2b3602c8d7dda508e302fbb3d1
# tampilan halaman utama aplikasi
def start_lobby():
    while True:
        print('┌───────────────────୨ৎ──────────────────┐')
        print('│               TamanBiru               │')
        print('│───────────────────────────────────────│')
        print('│ 1. 👥 Chat All                        │')
        print('│ 2. 💼 Program Studi                   │')
        print('│ 3. 🥇 Leaderboard                     │')
        print('│ 4. 👤 Cek Akun                        │')
        print('│ 5. ❌ Logout                          │')
        print('│───────────────────────────────────────│')
        print('└───────────────────────────────────────┘')

# user memilih menu
        masuk = input('Pilih menu: ')
# kondisional untuk memilih menu
        if masuk == '1' or masuk == 'Chat All'.lower:
<<<<<<< HEAD
            print('Chat All')
            break
        elif masuk == '2' or masuk == 'Program Studi'.lower:
            print('Program Studi')
            
=======
            chat_all()
        elif masuk == '2' or masuk == 'Program Studi'.lower:
            program_studi()
>>>>>>> 334470393ad00f2b3602c8d7dda508e302fbb3d1
        elif masuk == '3' or masuk == 'Leaderboard'.lower:
            print('Leaderboard')
            
        elif masuk == '4' or masuk == 'Cek Akun'.lower:
            print('Cek Akun')
            
        elif masuk == '5' or masuk == 'Logout'.lower:
            print('Anda telah keluar dari aplikasi')
            break

        else:
            print('Menu tidak tersedia')
        