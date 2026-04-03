# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

**Nama:** Moh Asrori
**Email:** irvanea1@gmail.com
**ID Dicoding:** azzror

---

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan berkualitas. Namun, masih terdapat permasalahan tingginya jumlah mahasiswa yang tidak menyelesaikan studi (dropout).

Permasalahan ini menjadi krusial karena berdampak pada reputasi institusi serta efisiensi proses pendidikan. Oleh karena itu, diperlukan solusi untuk mendeteksi mahasiswa yang berisiko dropout sedini mungkin agar dapat diberikan intervensi yang tepat.

---

## Permasalahan Bisnis

Beberapa pertanyaan utama yang ingin dijawab:

* Bagaimana mendeteksi mahasiswa yang berisiko dropout sejak dini?
* Faktor apa saja yang paling berpengaruh terhadap risiko dropout?
* Apa rekomendasi aksi yang dapat dilakukan untuk menurunkan angka dropout?

---

## Cakupan Proyek

Proyek ini mencakup:

* Analisis data (Exploratory Data Analysis)
* Identifikasi faktor utama penyebab dropout
* Pembuatan dashboard untuk visualisasi insight
* Pengembangan model machine learning untuk prediksi dropout
* Penyusunan rekomendasi berbasis data

---

## ersiapan

**Sumber data:**
Dataset mahasiswa dari Jaya Jaya Institut
https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

**Setup environment:**

```bash
conda create --name dicoding
conda activate dicoding
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Business Dashboard

**Link Dashboard:**
https://lookerstudio.google.com/reporting/da5b9f79-75b2-45f1-81fc-578e4d500eeb

Dashboard menampilkan analisis performa akademik mahasiswa berdasarkan status:

* **Graduate**
* **Dropout**
* **Enrolled (aktif)**

Hasil analisis menunjukkan bahwa:

* Mahasiswa yang **graduate** memiliki jumlah mata kuliah lulus dan nilai yang tinggi
* Mahasiswa yang **dropout** menunjukkan performa akademik yang rendah sejak semester pertama
* Mahasiswa **enrolled** berada di antara keduanya, menunjukkan potensi menuju dropout atau kelulusan

**Catatan:**
Status *Enrolled* digunakan dalam tahap eksplorasi data (EDA) untuk memberikan gambaran menyeluruh.
Namun, pada tahap modeling, analisis difokuskan pada klasifikasi **Dropout vs Graduate** agar model lebih terarah dan menghasilkan prediksi yang lebih actionable.

---

## Machine Learning Model

Model yang digunakan adalah **Random Forest Classifier** dengan pendekatan pipeline (scaling + model).

### Fitur yang digunakan:

* Curricular_units_2nd_sem_approved
* Curricular_units_1st_sem_approved
* Curricular_units_2nd_sem_grade
* Curricular_units_1st_sem_grade
* Curricular_units_2nd_sem_evaluations
* Admission_grade
* Tuition_fees_up_to_date
* Curricular_units_1st_sem_evaluations
* Previous_qualification_grade
* Course

Model difokuskan untuk memprediksi:

* **0 → Dropout**
* **1 → Graduate**

---

## Menjalankan Sistem Machine Learning

### Jalankan secara lokal

```bash
streamlit run app.py
```

### Akses web

https://edutech-problem.streamlit.app/

### Cara penggunaan:

1. Isi data akademik mahasiswa
2. Klik tombol **Predict**
3. Sistem akan menampilkan:

   * Prediksi status mahasiswa
   * Probabilitas hasil prediksi

---

## Conclusion

Berdasarkan analisis dan modeling yang dilakukan:

* Performa akademik, terutama pada semester pertama, merupakan faktor paling berpengaruh terhadap risiko dropout
* Mahasiswa dengan jumlah mata kuliah lulus dan nilai yang rendah cenderung memiliki risiko dropout lebih tinggi
* Mahasiswa aktif (*enrolled*) menunjukkan performa di tingkat menengah, yang berpotensi berkembang menjadi dropout atau graduate

Model machine learning yang dikembangkan mampu membantu mendeteksi mahasiswa berisiko secara lebih dini.

Implementasi sistem ini berpotensi:

* Menurunkan angka dropout
* Meningkatkan tingkat kelulusan
* Membantu institusi dalam pengambilan keputusan berbasis data

---

## Rekomendasi Action Items

* **Deteksi Dini**
  Identifikasi mahasiswa dengan performa akademik rendah sejak semester pertama

* **Pendampingan Akademik**
  Berikan tutoring atau bimbingan tambahan bagi mahasiswa berisiko

* **Monitoring Berkala**
  Lakukan evaluasi performa setiap semester

* **Konseling & Dukungan Psikologis**
  Sediakan layanan konseling bagi mahasiswa

* **Sistem Early Warning**
  Kembangkan notifikasi otomatis untuk mendeteksi risiko dropout

---

## Penutup

Proyek ini menunjukkan bagaimana data dan machine learning dapat digunakan untuk menyelesaikan permasalahan nyata di dunia pendidikan, khususnya dalam meningkatkan keberhasilan akademik mahasiswa.
