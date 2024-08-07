# Import libraries
import streamlit as st
import eda
import prediction

# Add side bar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Default Payment Predictor'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write(''' Aplikasi ini menyediakan alat untuk Analisis Data Eksplorasi dan 
             Prediksi credit card default payments.''')

# Features
st.sidebar.write('''### Features:
- **Exploratory Data Analysis**: Explorasi data secara mendalam untuk menemukan pola dan wawasan terkait dengan default pembayaran kartu kredit.
- **Default Payment Predictor**: Menggunakan model prediktif untuk meramalkan kemungkinan terjadinya default pembayaran kartu kredit pada periode mendatang.''')



# Define the Home Page
def show_home():
    
    # Create title and introduction
    st.title('Welcome to Credit Analysis Tool')
    st.write('''Aplikasi ini menyediakan alat untuk Analisis Data Eksplorasi dan 
             Prediksi credit card default payments.''')
             
    st.write('''Gunakan panel navigasi di sebelah kiri untuk memilih modul yang ingin digunakan.''')
    
    # Add image
    st.image('gambar_cc2.jpg')
             
    
    st.markdown('---')
    
    # Dataset
    st.write('#### Dataset')
    st.markdown(''' Dataset diperoleh dari Big Query mengenai Credit Card Default. 
                Untuk detail lebih lanjut, silahkan visit atau download dataset
                [Credit Card Default Dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table&project=hacktiv8-sql-417802&ws=!1m9!1m3!3m2!1sbigquery-public-data!2sml_datasets!1m4!4m3!1sbigquery-public-data!2sml_datasets!3scredit_card_default).''')
    

    # Objective
    st.write('#### Objective')
    st.markdown('''Program ini bertujuan untuk mengembangkan model klasifikasi menggunakan algoritma 
                `K-Nearest Neighbors (KNN)`, `Support Vector Machine (SVM)`, dan `Logistic Regression` 
                untuk memperkirakan default kartu kredit untuk bulan berikutnya. Metrik evaluasi digunakan
                untuk penilaian kinerja model adalah `F1-Score` untuk menghitung kinerja setiap model.''')
    
# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Default Payment Predictor':
    prediction.run()