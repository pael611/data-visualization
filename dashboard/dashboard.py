import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
st.header('Dashboard')

# Import dataset yang akan kita gunakan (csv)
uploaded_file1 = st.file_uploader("dongsi.csv", type="csv")
if uploaded_file1 is not None:
    df1 = pd.read_csv(uploaded_file1)
uploaded_file2 = st.file_uploader("shunyi.csv", type="csv")
if uploaded_file2 is not None:
    df2 = pd.read_csv(uploaded_file2)
# Menampilkan dataset
st.subheader('Dataset Dongsi')
st.write(df1)
st.subheader('Dataset Shunyi')
st.write(df2)

# Membuat fungsi untuk cleaning data df1 dan df2 dari duplikasi dan missing value
def clean_data(df):
    # Menghapus duplikasi
    df = df.drop_duplicates()
    # Menghapus missing value
    df = df.dropna()
    return df

# Membersihkan data
df1 = clean_data(df1)
df2 = clean_data(df2)

# Menampilkan dataset yang sudah dibersihkan
st.subheader('Dataset Dongsi yang sudah dibersihkan')
st.write(df1)
st.subheader('Dataset Shunyi yang sudah dibersihkan')
st.write(df2)

# Mengelompokkan data berdasarkan tahun dan bulan, station untuk melihat rata-rata dari NO2, CO, dan TEMP
data1_grouped = df1.groupby(['year', 'month', 'station']).agg({
    'NO2': ['mean'],
    'CO': ['mean'],
    'TEMP': ['mean', 'min', 'max']
})
data2_grouped = df2.groupby(['year', 'month', 'station']).agg({
    'NO2': ['mean'],
    'CO': ['mean'],
    'TEMP': ['mean', 'min', 'max']
})

# Menampilkan data yang sudah dikelompokkan
st.subheader('Data Dongsi yang sudah dikelompokkan dari tahun-bulan')
st.write(data1_grouped)
st.subheader('Data Shunyi yang sudah dikelompokkan dari tahun-bulan')
st.write(data2_grouped)

# Sidebar untuk memilih rentang waktu
st.sidebar.header('Filter Rentang Waktu')
start_year = st.sidebar.selectbox('Pilih Tahun Mulai', sorted(df1['year'].unique()))
end_year = st.sidebar.selectbox('Pilih Tahun Akhir', sorted(df1['year'].unique(), reverse=True))

# Filter data berdasarkan rentang waktu yang dipilih
filtered_data1 = data1_grouped.loc[(data1_grouped.index.get_level_values('year') >= start_year) & (data1_grouped.index.get_level_values('year') <= end_year)]
filtered_data2 = data2_grouped.loc[(data2_grouped.index.get_level_values('year') >= start_year) & (data2_grouped.index.get_level_values('year') <= end_year)]

# Visualisasi data Dongsi
plt.figure(figsize=(15, 5))
sns.lineplot(data=filtered_data1, x='month', y=('TEMP', 'mean'), hue='year')
plt.title(f'Rata-rata Suhu Stasiun Dongsi Tahun {start_year}-{end_year}')
plt.xlabel('Bulan')
plt.ylabel('Suhu (°C)')
plt.xticks(rotation=45)
plt.legend(title='Tahun')
plt.grid()
plt.tight_layout()
st.subheader(f'Diagram Suhu Stasiun Dongsi Tahun {start_year}-{end_year}')
st.pyplot(plt)

# Visualisasi data Shunyi
plt.figure(figsize=(15, 5))
sns.lineplot(data=filtered_data2, x='month', y=('CO', 'mean'), hue='year')
plt.title(f'Rata-rata CO Stasiun Shunyi Tahun {start_year}-{end_year}')
plt.xlabel('Bulan')
plt.ylabel('CO (mg/m3)')
plt.xticks(rotation=45)
plt.legend(title='Tahun')
plt.grid()
plt.tight_layout()
st.subheader(f'Diagram CO Stasiun Shunyi Tahun {start_year}-{end_year}')
st.pyplot(plt)

plt.figure(figsize=(15, 5))
sns.lineplot(data=filtered_data2, x='month', y=('NO2', 'mean'), hue='year')
plt.title(f'Rata-rata NO2 Stasiun Shunyi Tahun {start_year}-{end_year}')
plt.xlabel('Bulan')
plt.ylabel('NO2 (mg/m3)')
plt.xticks(rotation=45)
plt.legend(title='Tahun')
plt.grid()
plt.tight_layout()
st.subheader(f'Diagram NO2 Stasiun Shunyi Tahun {start_year}-{end_year}')
st.pyplot(plt)
