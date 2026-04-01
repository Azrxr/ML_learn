# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

* Nama: Moh Asrori
* Email: irvanea1@gmail.com
* Id Dicoding: azzror

## Business Understanding
**Jaya Jaya Institut** adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah berhasil mencetak banyak lulusan dengan reputasi yang sangat baik di berbagai bidang. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut juga menghadapi tantangan yang signifikan terkait dengan tingginya tingkat siswa yang tidak menyelesaikan pendidikannya alias dropout.

**Masalah dropout** ini merupakan masalah yang serius bagi institusi pendidikan, karena dropout yang tinggi dapat mempengaruhi citra institusi, mengurangi tingkat kelulusan, dan pada akhirnya berdampak pada daya tarik institusi bagi calon siswa di masa mendatang. Tingkat dropout yang tinggi juga bisa menjadi indikasi bahwa ada masalah mendasar dalam proses penerimaan siswa, pembelajaran, atau dukungan akademik yang disediakan oleh institusi.

### Permasalahan Bisnis
Masalah bisnis yang ingin diselesaikan adalah sebagai berikut:
1. Bagaimana cara mengidentifikasi mahasiswa yang berpotensi dropout sejak dini?
2. Apa saja faktor yang menyebabkan siswa tidak menyelesaikan pendidikannya (dropout)?
3. Tindakan apa yang dapat dilakukan untuk mengurangi mahasiswa dropout dan memastikan lebih banyak mahasisawa yang menyelesaikan pendidikannya?

### Cakupan Proyek
Berikut cakupan proyek yang telah dikerjakan:
* Eksplorasi dan Analysis Data : Melakukan eksplorasi pada data yang sudah diperoleh agar dapat mendapatkan gambaran umum tentang data. Selanjutnya melakukan analysis untuk mengidentifikasi faktor yang mempengaruhi mahasiswa dropout
* Visualisasi Data : Membuat dashboard laporan untuk memonitor dan menganalissis mahasiswa yang berpotensi dropout
* Model dan Rekomendasi : Membangun model klasifikasi untuk melakukan rekomendasi yang dapat dilakukan untuk mengurangi droput.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).

* Setup environment:
    ```
    conda create --name proyek-institusi-pendidikan python==3.9.15
    ```
* Install requirements: 
    ```
    pip install -r requirements.txt
    ```


## Business Dashboard
Berikut adalah dashboard yang telah dibuat:

Dashboard ini dirancang untuk memberikan wawasan komprehensif kepada institut terhadap faktor-faktor yang berkontribusi dengan **Status** baik dropout, enrolled, ataupun graduated. Dengan dashboard ini tim institut dapat :
1. Memantau Tingkat Dropout Secara Proaktif:
    - Melalui visualisasi persentase siswa yang dropout, enrolled, dan graduate, tim dapat memantau tren dropout secara real-time. Ini memungkinkan institusi untuk segera mengambil tindakan jika terlihat ada peningkatan signifikan dalam tingkat dropout.

2. Menganalisis Faktor-Faktor yang Mempengaruhi Dropout:
    - Dengan analisis mendalam tentang bagaimana faktor-faktor seperti nilai akademik, beasiswa, biaya pendidikan, dan kualifikasi orang tua mempengaruhi status siswa, tim dapat mengidentifikasi elemen-elemen yang paling berisiko bagi siswa. Ini memungkinkan penyesuaian kebijakan dan intervensi yang lebih tepat sasaran.

    <img src="https://raw.githubusercontent.com/Azrxr/ML_learn/fb82605804e840fabcbf185c6f4bff1a2fd6118e/image/azzror_dashboard.png" width="500">

    Atau buka [tautan](https://lookerstudio.google.com/s/qCLnx10DVHE) untuk membuka dashboard yang ada di looker studio.

## Menjalankan Sistem Machine Learning
Pada proyek ini telah disediakan sebuah prototype untuk melakukan prediksi terhadap model yang sudah dibuat. Untuk menjalankan protoype secara lokal jalankan perintah berikut di terminal: 

```
streamlit run app.py
```
👉 [Klik di sini untuk membuka aplikasi](https://edutech-problem.streamlit.app/)

 <img src="https://raw.githubusercontent.com/Azrxr/ML_learn/dcee27da7e4dca650cfd7d57199836f8968eda14/image/azzror-prototype.png" width="500">

## Conclusion
Proyek ini bertujuan untuk mengatasi masalah utama yang dihadapi Jaya Jaya Institut terkait tingkat dropout siswa. Berikut adalah rangkuman proyek ini:

1. Bagaimana cara mengidentifikasi siswa yang berpotensi dropout sejak awal?

- Dengan mengembangkan model prediktif berbasis algoritma seperti Random Forest, Decision Tree, maupun XGBoost, Jaya Jaya Institut dapat mengenali siswa yang berisiko dropout lebih dini. Model ini mampu mendeteksi siswa berisiko dengan tingkat akurasi yang baik berdasarkan data historis serta berbagai faktor yang berkaitan, seperti performa akademik (nilai masuk dan nilai semester), kondisi finansial (status pembayaran dan beasiswa), serta latar belakang pendidikan dan kondisi khusus mahasiswa. Dengan memanfaatkan kombinasi faktor tersebut, institusi dapat melakukan intervensi lebih cepat dan tepat untuk mengurangi tingkat dropout.
  
2. Apa saja faktor yang menyebabkan siswa tidak menyelesaikan pendidikannya (dropout)?

- Tingkat dropout mahasiswa dipengaruhi oleh faktor finansial, di mana mahasiswa yang tidak mampu membayar biaya pendidikan atau tidak mendapatkan beasiswa cenderung lebih tinggi untuk dropout. Selain itu, faktor usia juga berpengaruh, dengan mahasiswa yang lebih tua memiliki risiko dropout yang lebih besar karena kemungkinan memiliki tanggung jawab tambahan di luar akademik.

 <img src="https://raw.githubusercontent.com/Azrxr/ML_learn/dcee27da7e4dca650cfd7d57199836f8968eda14/image/azzror-korelasi.png" width="500">

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
Bimbingan Akademik yang Intensif:

1. Solusi Financial: Dengan menambah kuota program beasiswa, menyediakan skema pembayaran cicilan, dan memberikan peringatan dini untuk mahasiswa yang menunggak
   
2. Dukungan Mahasiswa Lebih Tua: Dengan menyediakan jadwal kuliah fleksibel, program kelas karyawan atau part-time, dan menyediakan dosen pembimbing khusus
