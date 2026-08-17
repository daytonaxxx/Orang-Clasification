# Website Klasifikasi Kualitas Jeruk

Website ini dibuat berdasarkan notebook `belajar_kalsikfikasi_jekruk.ipynb`.

Model:
- Logistic Regression
- StandardScaler untuk fitur numerik
- OneHotEncoder untuk `asal_daerah` dan `musim_panen`
- OrdinalEncoder untuk `warna`

Fitur input:
1. berat
2. diameter
3. tebal_kulit
4. kadar_gula
5. asal_daerah
6. warna
7. musim_panen

Target:
- kualitas

## Menjalankan di Windows

Buka CMD/PowerShell di folder project:

python -m venv venv

Aktifkan:
venv\Scripts\activate

Install:
pip install -r requirements.txt

Jalankan:
python app.py

Buka:
http://127.0.0.1:5000

Contoh data dari notebook:
diameter = 4.9
berat = 220
tebal_kulit = 0.4
kadar_gula = 13
asal_daerah = Jawa Tengah
warna = kuning
musim_panen = kemarau

Catatan:
Pada model, urutan kolom yang benar adalah:
berat, diameter, tebal_kulit, kadar_gula, asal_daerah, warna, musim_panen.
