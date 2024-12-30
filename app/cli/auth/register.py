import os

def start_register(name, email, password, prodi, semester, notelp):
    try:
        # Enkripsi sederhana untuk kata sandi (gunakan hashing pada implementasi sebenarnya)
        with open('./app/cli/data/logindatabase.txt', 'a') as file:
            file.write(f"{name},{email},{password},{prodi},{semester},{notelp}\n")
        print('Registrasi Berhasil')
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def email_upi(email):
    return email.endswith('@upi.edu')

def access_register(option):
    if option == 'start_register':
        if not os.path.exists('./app/cli/data/'):
            os.makedirs('./app/cli/data/', exist_ok=True)
        while True:
            name = input('Masukkan Username baru (min 3 karakter): ').strip()
            email = input('Masukkan Email (@upi.edu): ').strip()
            password = input('Masukkan Password baru (min 6 karakter): ').strip()
            prodi = input('Masukkan prodi (RPL, TEKKOM, PMM, PGSD, PGPAUD): ').strip()
            semester = input('Masukkan semester: ').strip()
            notelp = input('Masukkan nomor telefon: ').strip()
            
            if name and email and password and prodi and semester and notelp:
                if len(name) < 3 or len(password) < 6:
                    print("Username harus minimal 3 karakter dan Password minimal 6 karakter. Coba lagi.")
                    continue
                elif not name.isalpha() or not password.isalnum() or not notelp.isdigit():
                    print("Nama harus huruf, password harus alfanumerik, dan nomor telefon harus angka.")
                    continue
                elif not email_upi(email):
                    print("Email harus menggunakan @upi.edu")
                    continue
                elif ',' in name or ',' in email or ',' in password or ',' in prodi or ',' in semester or ',' in notelp:
                    print("Data tidak boleh mengandung koma (,).")
                    continue
                elif prodi not in ("RPL", "TEKKOM", "PMM", "PGSD", "PGPAUD"):
                    print("Masukkan prodi yang benar.")
                    continue
                elif not semester.isdigit():
                    print("Semester harus berupa angka.")
                    continue
                try:
                    with open('./app/cli/data/logindatabase.txt', 'r') as file:
                        existing_users = [line.strip().split(',')[0] for line in file if ',' in line]
                        if name in existing_users:
                            print("Username sudah terdaftar. Silahkan ke menu Login.")
                            return
                    start_register(name, email, password, prodi, semester, notelp)
                    break
                except FileNotFoundError:
                    print("Database tidak ditemukan. Membuat database baru.")
                    start_register(name, email, password, prodi, semester, notelp)
                    break
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")
            else:
                print("Semua data harus diisi. Silakan coba lagi.")
    else:
        print('Opsi tidak valid.')
