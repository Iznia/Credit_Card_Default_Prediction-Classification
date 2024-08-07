# Import Libraries
import json
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.svm import SVC


# Load all files
with open('list_num_cols.txt', 'r') as file_1:
    list_num_cols = json.load(file_1)

with open('list_cat_cols.txt', 'r') as file_2:
    list_cat_cols = json.load(file_2)

# Load fitted pipeline
with open('best_svm_model.pkl', 'rb') as model_file:
    pipeline = pickle.load(model_file)



def run():
    st.title("Credit Card Default Prediction")

    with st.form('default_prediction_form'):
        # Limit balance
        limit_balance = st.number_input('Limit Balance', 
                                        value=30000, 
                                        min_value=1000, 
                                        max_value=1000000, 
                                        step=1000)

        # Education level
        education_level = st.selectbox('Education Level', 
                                       ('Graduate School', 'University', 'High School', 'Others'), index=1)
        education_mapping = {'Graduate School': 1, 
                             'University': 2, 
                             'High School': 3, 
                             'Others': 4}
        education_level = education_mapping[education_level]

        # Payment status
        pay_0 = st.selectbox('Pay_0 (Payment Status September)', (-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8), index=2)
        pay_2 = st.selectbox('Pay_2 (Payment Status August)', (-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8), index=2)
        pay_3 = st.selectbox('Pay_3 (Payment Status July)', (-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8), index=2)
        pay_4 = st.selectbox('Pay_4 (Payment Status June)', (-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8), index=2)
        pay_5 = st.selectbox('Pay_5 (Payment Status May)', (-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8), index=2)
        pay_6 = st.selectbox('Pay_6 (Payment Status April)', (-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8), index=2)

        # Submit button
        submitted = st.form_submit_button('Predict')

    data_inf = {
        'limit_balance': limit_balance,
        'education_level': education_level,
        'pay_0': pay_0,
        'pay_2': pay_2,
        'pay_3': pay_3,
        'pay_4': pay_4,
        'pay_5': pay_5,
        'pay_6': pay_6
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    # buat logikanya
    if submitted:
        # Predict using the pipeline
        y_pred_inf = pipeline.predict(data_inf)

        # Display prediction result
        for i, pred in enumerate(y_pred_inf):
            if pred == 0:
                st.write(f'Prediction for entry {i}: Non-Default')
            else:
                st.write(f'Prediction for entry {i}: Default')

if __name__ == '__main__':
    run()

