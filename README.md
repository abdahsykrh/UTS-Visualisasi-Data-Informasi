# UTS Visualisasi Data & Informasi  
**Nama:** Abdah Syakiroh Gustian  
**NPM:** 220660121144  
**Kelas:** Informatika ISSI VII-B  

---

## 📌 Deskripsi Singkat  
Repositori ini berisi beberapa komponen penting untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah **Visualisasi Data & Informasi**, yaitu:

- Dataset gempa bumi (`earthquakes_cleaned_100.csv`)
- Source code preprocessing (`preprocess.py`)
- Tiga visualisasi Datawrapper (Line Chart, Bar Chart, Symbol Map)
- Dashboard GitHub Pages untuk menampilkan visualisasi secara online

---

## 📊 Link Visualisasi Datawrapper

### 1️⃣ **Tren Kekuatan Gempa (Line Chart)**  
🔗 https://datawrapper.dwcdn.net/jIQgg/1/

### 2️⃣ **Rata-Rata Gempa per Wilayah (Bar Chart)**  
🔗 https://datawrapper.dwcdn.net/Z8opl/1/

### 3️⃣ **Sebaran Gempa Bumi Indonesia (Symbol Map)**  
🔗 https://datawrapper.dwcdn.net/bAa5S/1/

---

## 🌐 Dashboard GitHub Pages  
Seluruh visualisasi ditampilkan dalam satu halaman web:  

👉 [https://github.com/abdahsykrh/UTS-Visualisasi-Data-Informasi]

---

## 🗂 Dataset  
**File:** `earthquakes_cleaned_100.csv`  
Dataset ini merupakan data gempa bumi Indonesia tahun 2008–2025 yang sudah dibersihkan dan dipilih sebanyak 100 data untuk visualisasi.

---

## 💻 Source Code  
**File:** `preprocess.py`  

### Fungsi utama:
- Membersihkan dataset (drop missing values)
- Mengonversi kolom tanggal ke format datetime
- Membuat kolom **Year** dan **Month**
- Menyimpan data hasil preprocessing dalam bentuk CSV yang siap divisualisasikan

---

## 📁 Struktur Folder

📁 Struktur Folder

```
UTS-Visualisasi-Data-Informasi/
│
├── index.html                   → Dashboard GitHub Pages
├── README.md                    → Dokumentasi UTS
├── earthquakes_cleaned_100.csv  → Dataset gempa bumi Indonesia (100 data)
└── preprocess.py                → Script preprocessing dataset
```
