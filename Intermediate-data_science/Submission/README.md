# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi

Proyek ini menganalisis dataset Bike Sharing untuk menjawab pertanyaan bisnis terkait pengaruh musim, cuaca, dan pola waktu terhadap penyewaan sepeda.

## Struktur Direktori

```
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── Bike-sharing-dataset/
│   ├── day.csv
│   ├── hour.csv
│   └── Readme.txt
├── Proyek_Analisis_Data.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Dicoding Collection Dashboard ✨

### Setup Environment - Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

### Menjalankan Streamlit App

```bash
cd dashboard
streamlit run dashboard.py
```

Dashboard akan terbuka di browser pada `http://localhost:8501`

## Pertanyaan Bisnis

1. Bagaimana pengaruh musim dan kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Kapan waktu puncak penyewaan sepeda berdasarkan jam dan bagaimana perbedaannya antara hari kerja dan hari libur?
