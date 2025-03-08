# Dashboard Visualisasi Data

Dashboard ini menampilkan visualisasi data kualitas udara dari dua stasiun: Dongsi dan Shunyi. Anda dapat memilih rentang waktu untuk melihat perubahan rata-rata suhu, CO, dan NO2.

## Setup Environment

### Setup Environment - Anaconda

1. Buat dan aktifkan environment baru menggunakan Anaconda:
    ```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    ```

2. Instal semua dependensi yang diperlukan dari `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Setup Environment - Shell/Terminal

1. Buat direktori proyek dan masuk ke dalamnya:
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    ```

2. Instal `pipenv` jika belum terinstal:
    ```bash
    pip install pipenv
    ```

3. Instal semua dependensi yang diperlukan dan aktifkan shell:
    ```bash
    pipenv install
    pipenv shell
    pip install -r requirements.txt
    ```

## Run Streamlit App

Untuk menjalankan dashboard, gunakan perintah berikut di terminal Anda:

```bash
streamlit run dashboard.py
```