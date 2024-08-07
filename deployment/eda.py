# Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



# Create program
def run():

    # Main page setup
    st.title('Credit Card Default Users')

    # Deskripsi
    st.write("""
             Aplikasi ini bertujuan untuk menyediakan platform analisis data yang interaktif. 
             Pengguna dapat memfilter data berdasarkan usia dan jenis kelamin, dan melakukan 
             visualisasi data menggunakan berbagai jenis plot seperti histogram, scatter plot, 
             dan bar chart.
             """)
    st.write('*Page ini dibuat oleh Iznia*')


    # membuat sub header
    st.subheader('Data Exploration untuk Analisa Dataset Credit Card Default')

    # tambahkan gambar
    image = Image.open('gambar_cc.jpeg')
    st.image(image, caption = 'Credit Card')

    # mmebuat batas dengan garis lurus
    st.markdown('---')

    # show dataframe
    st.write('### Dataset')
    data = pd.read_csv('P1G5_Set_1_Iznia_Azyati.csv')
    st.dataframe(data)

    # User selection
    st.header('User Input Features')


    # Default Payment Next Month Percentages
    st.write('Default Payment Next Month Percentages')
    default_status = data['default_payment_next_month'].replace({1: 'Default', 0: 'Non-Default'})
    default_counts = default_status.value_counts()
    default_percentages = (default_counts / default_counts.sum()) * 100
    fig = plt.figure(figsize=(10,6))
    plt.pie(default_percentages, labels=default_percentages.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    st.pyplot(fig)

    # Paragraf teks panjang
    st.write("""
             Pie chart ini menunjukkan seberapa banyak klien yang melakukan pembayaran tepat waktu 
             dan yang tidak tepat waktu. Mostly, sebesar 78.6% membayar tepat waktu (non-default). 
             Namun sekitar 21,4% tidak membayar tepat waktu (default). Kelompok yang lebih kecil 
             (default) ini perlu perhatian lebih dari lembaga kredit untuk mencari tahu mengapa 
             mereka kesulitan dalam pembayaran. 
             """)


    # Membuat histogram berdasarkan input user
    st.write('#### Histogram Berdasarkan Input User')
    option = st.selectbox('Pilih column:', data.columns)  # Create a selection box with all columns
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[option], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat plotly plot
    st.write('#### Plotly plot - Scatter Plot')
    x_axis = st.selectbox('Pilih X-axis:', data.columns)
    y_axis = st.selectbox('Pilih Y-axis:', data.columns)
    fig = px.scatter(data, x=x_axis, y=y_axis, hover_data=data.columns)
    st.plotly_chart(fig)

    # Age slider
    st.subheader('Filter Data')
    selected_age = st.slider('Filter by age',
                             min_value=int(data['age'].min()),
                             max_value=int(data['age'].max()),
                             value=(int(data['age'].min()), int(data['age'].max())))

    # Sex selection
    sex_mapping = {'Male': 1, 'Female': 2}
    sex_options = ['Male', 'Female']
    sex_selection = st.multiselect('Filter by gender', options=sex_options, default=sex_options)
    
    # Convert selected sex from names to numerical values for filtering
    selected_sex_numerical = []
    for sex in sex_selection:
        selected_sex_numerical.append(sex_mapping[sex])

    # Filtering data based on user selection
    filtered_data = data[(data['age'] >= selected_age[0]) & (data['age'] <= selected_age[1]) & (data['sex'].isin(selected_sex_numerical))]
    st.write('Data Dimension: ' + str(filtered_data.shape[0]) + ' rows and ' + str(filtered_data.shape[1]) + ' columns.')
    st.dataframe(filtered_data)

    # Visualization selections
    st.header('Visualization Settings')
    plot_type = st.selectbox('Select the type of plot', ['Scatter Plot', 'Bar Chart', 'Histogram'])



    # Create condition for selected visualization
    
    # Histogram
    if plot_type == 'Histogram':
        st.subheader('Histogram')
        column = st.selectbox('Select column to display', options=['age', 'limit_balance', 'education_level'])
        fig, ax = plt.subplots()
        sns.histplot(data=filtered_data, x=column, kde=True, ax=ax, color='skyblue')
        ax.set_title(f'{column} Distribution')
        st.pyplot(fig)

    # Bar Chart
    elif plot_type == 'Bar Chart':
        st.subheader('Bar Chart')
        column = st.selectbox('Select column to display', options=['sex', 'education_level', 'marital_status'])
        fig, ax = plt.subplots()
        sns.countplot(data=filtered_data, x=column, ax=ax, palette='coolwarm')
        ax.set_title(f'Count of {column}')
        st.pyplot(fig)

    # Scatter Plot
    elif plot_type == 'Scatter Plot':
        st.subheader('Scatter Plot')
        x_axis = st.selectbox('X-axis', options=['age', 'limit_balance'])
        y_axis = st.selectbox('Y-axis', options=['bill_amt_1', 'bill_amt_2', 'bill_amt_3', 'bill_amt_4', 'bill_amt_5', 'bill_amt_6',
                                                 'pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6'])
        fig, ax = plt.subplots()
        sns.scatterplot(data=filtered_data, x=x_axis, y=y_axis, ax=ax, hue='sex', palette='coolwarm')
        ax.set_title(f'{x_axis} vs {y_axis}')
        st.pyplot(fig)

if __name__ == '__main__':
    run()