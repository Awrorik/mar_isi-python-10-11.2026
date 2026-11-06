import streamlit as st
import cv2 
import numpy as np 
from PIL import Image

st.set_page_config(page_title="Mar_isi Photo Editor", page_icon="", layout="wide") 
st.title("📸 Mar_isi Photo Editor 📸") 
st.subheader(":blue[Загрузите фото и используйте фильтры]")
st.sidebar.header("Настройки фильтров") 
uploaded_file = st.sidebar.file_uploader("Выберите фотку...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None: 
   image = Image.open(uploaded_file) 
   img_array = np.array(image)

   col1, col2 = st.columns(2)

   with col1:
     st.subheader("Оригинальное фото")
     st.image(img_array, width="stretch")

     filter_option = st.sidebar.selectbox( "Выберите фильтр", ["Оригинал", "черно-белый", "Контраст", "Инверсия", "Яркость", "Размывчивость", "Настройки яркости", "Настройки контраста", "Настройки инверсии", "Настройки размывчивости", "Настройки черно-белого"])
     processed_img = img_array.copy()

     
     if filter_option == "черно-белый":
      gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
      processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
 
     elif filter_option == "Размывчивость":
      processed_img = cv2.GaussianBlur(img_array, (33, 33), 0)

     elif filter_option == "Яркость":
      processed_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=50)

     elif filter_option == "Контраст":
      processed_img = cv2.convertScaleAbs(img_array, alpha=1.7, beta=0)
      

     elif filter_option == "Инверсия":
      processed_img = 255 - img_array

     elif filter_option =="Настройки яркости":
           brightness_val = st.sidebar.slider("Яркость", -100, 100, 0)
        
           processed_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=brightness_val)
     elif filter_option == "Настройки контраста":
           contrast_val = st.sidebar.slider("Контраст", -100, 100, 0)
           processed_img = cv2.convertScaleAbs(img_array, alpha=1.7, beta=contrast_val)

     elif filter_option == "Настройки инверсии":
              inversion_val = st.sidebar.slider("Инверсия", -255, 255, 0)
              processed_img = cv2.convertScaleAbs(255 - img_array, alpha=1.0, beta=inversion_val)

     elif filter_option == "Настройки размывчивости":
              blur_val = st.sidebar.slider("Размывчивость", 0, 50, 100)
              processed_img = cv2.GaussianBlur(img_array, (blur_val * 2 + 1, blur_val * 2 + 1), 0)    
              
     elif filter_option =="Настройки черно-белого":
                gray_val = st.sidebar.slider("Черно-белый", -100, 200, 0)
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
                processed_img = cv2.convertScaleAbs(processed_img, alpha=1.0, beta=gray_val)


     with col2:
        st.subheader("Оброблена фотка")
        st.image(processed_img, width="stretch")