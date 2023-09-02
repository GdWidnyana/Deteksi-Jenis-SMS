import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import time

# load save model
model_fraud = pickle.load(open('model_fraud.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))

st.set_page_config(page_title="WebApp Prediksi SMS Penipuan", page_icon="✉️")

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# judul halaman

st.markdown("<h1 class='centered-title'>Prediksi SMS Penipuan</h1>", unsafe_allow_html=True)

clean_teks = st.text_input('Masukan Teks SMS')

fraud_detection = ''

if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))
    
    if (predict_fraud == 0):
        fraud_detection = 'SMS Normal'
    elif (predict_fraud == 1):
        fraud_detection = 'SMS Fraud'
    else :
        fraud_detection = 'SMS Promo'
    with st.empty():
        st.info("Sedang memproses prediksi...")
        with st.spinner():
            time.sleep(2)
        st.success("Selesai!")
        time.sleep(1)
        st.snow()

st.success(fraud_detection)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1483401757487-2ced3fa77952?ixlib=rb-4.0.3");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.set_option('deprecation.showPyplotGlobalUse', False)
