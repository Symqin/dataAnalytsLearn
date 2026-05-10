# String dan Dictionary di Python
salam = "Selamat datang di Python!" 
nama = "qin"

pesan = salam + " Nama saya adalah " + nama
print(pesan)  # Output: Selamat datang di Python! Nama saya adalah qin

#indeks dan slicing
print(salam[0])  # Output: S    
print(salam[1:8])  # Output: elamat
print(salam[-1])  # Output: !

#String manipulasi
salam_kecil = salam.lower()
print(salam_kecil)  # Output: selamat datang di python! 
salam_besar = salam.upper()
print(salam_besar)  # Output: SELAMAT DATANG DI PYTHON!
salam_clean = salam.strip()
print(salam_clean)  # Output: Selamat datang di Python!
salam_ganti = salam.replace("Python", "Dunia")
print(salam_ganti)  # Output: Selamat datang di Dunia!

#format string
umur = 25
pesan_umur = f"Saya berumur {umur} tahun."
print(pesan_umur)  # Output: Saya berumur 25 tahun.

pesan_format = "Saya berumur {} tahun.".format(umur)
print(pesan_format)  # Output: Saya berumur 25 tahun.

#dictionary
kamus = {
    "nama": "qin",
    "umur": 25,
    "pekerjaan": "programmer"
}

print(kamus["nama"])  # Output: qin
print(kamus["umur"])  # Output: 25

#modifikasi dictionary
kamus["umur"] = 26
print(kamus["umur"])  # Output: 26

for key, value in kamus.items():
    print(f"{key}: {value}")

#nested dictionary
orang = {
    "nama": "qin",  
    "umur": 25,
    "alamat": {
        "jalan": "Jl. Merdeka",
        "kota": "Jakarta",
        "kode_pos": "12345"
    }
}

print(orang["alamat"]["kota"])  # Output: Jakarta

#menggabungkan dictionary dan string

template = "Mahasiswa bernama {nama} berumur {umur} tahun."
mahasiswa = [{"nama": "qin", "umur": 25}, {"nama": "budi", "umur": 22}
             ]

for mhs in mahasiswa:
    print(template.format(nama=mhs["nama"], umur=mhs["umur"]))

pengguna = {"nama": "Ani", "email": "ani@example.com"}
template_email = "Kepada {nama},\n\nTerima kasih telah mendaftar.\n\nSalam,\nTim Kami"

isi_email = template_email.format(**pengguna)
print(isi_email)