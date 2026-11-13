
import streamlit as st
import os
import cv2
import numpy as np
from PIL import Image
import requests
from dotenv import load_dotenv
import urllib.parse
import io

load_dotenv()
HF_API_URL = "https://router.huggingface.co/hf-interface/models/black-forest-labs/FLUX.1-schnell"
HF_TOKEN = os.getenv("HF_TOKEN")

def generate_image_hf(prompt):
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed=43"
        response = requests.get(url, timeout=45)
        if response.status_code == 200:
            return response.content, None
        else:
            
            return None, f"Сервис закрыт! ({response.status_code})"
    except requests.exceptions.Timeout:
        return None, "Отказано"
    except Exception as e:
        return None, f"Ошибка: {e}"
st.title("Ai creative studio")
st.write("Какую фотку вы бы хотели сгенерировать?")
prompt = st.text_area("Опиши (промт пиши на английском пожалуйста)")
if st.button("Згенеруй фото") and prompt:

    with st.spinner("Ai делает фото..."):
        image_bytes, error = generate_image_hf(prompt)

    if error:
        st.error(error)
    elif image_bytes:
        st.session_state["image"] = image_bytes
if "image" in st.session_state:
    result_image = Image.open(

        io.BytesIO(st.session_state["image"])).convert("RGB")
    img_array = np.array(result_image)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Оригинальное фото")
        st.image(img_array, width="stretch")

    filter_option = st.sidebar.selectbox(
        "Какой эффект вы бы хотели использовать?",
        [ "Оригинал","черно-белый", "Контраст","Инверсия","Яркость", "Размывчивость","Настройки яркости","Настройки контраста", "Настройки инверсии","Настройки размывчивости","Настройки черно-белого"])

    processed_img = img_array.copy()

    if filter_option == "черно-белый":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    elif filter_option == "Размывчивость":
        processed_img = cv2.GaussianBlur(img_array, (33, 33), 0)

    elif filter_option == "Яркость":
        processed_img = cv2.convertScaleAbs(
            img_array, alpha=1.0, beta=50)

    elif filter_option == "Контраст":
        processed_img = cv2.convertScaleAbs(
            img_array, alpha=1.7, beta=0)
    elif filter_option == "Инверсия":
        processed_img = 255 - img_array
    elif filter_option == "Настройки яркости":
        brightness_val = st.sidebar.slider(
            "Яркость", -100, 100, 0)
        
        processed_img = cv2.convertScaleAbs(
            img_array, alpha=1.0, beta=brightness_val)
    elif filter_option == "Настройки контраста":
        contrast_val = st.sidebar.slider(
            "Контраст", 0, 300, 100 )

        processed_img = cv2.convertScaleAbs(
            img_array, alpha=contrast_val / 100, beta=0)

    elif filter_option == "Настройки инверсии":
        inversion_val = st.sidebar.slider("Инверсия", -255, 255, 0)
        processed_img = cv2.convertScaleAbs(
            255 - img_array, alpha=1.0, beta=inversion_val)

    elif filter_option == "Настройки размывчивости":
        blur_val = st.sidebar.slider( "Размывчивость", 0, 50, 0)

        if blur_val > 0:
            processed_img = cv2.GaussianBlur(img_array,(blur_val * 2 + 1, blur_val * 2 + 1),0)

    elif filter_option == "Настройки черно-белого":
        gray_val = st.sidebar.slider("Черно-белый", -100, 200, 0)

        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

        processed_img = cv2.convertScaleAbs(processed_img, alpha=1.0, beta=gray_val)

    with col2:
        st.subheader("Обработанная фотография")
        st.image(processed_img, width="stretch")

    result_image = Image.fromarray(processed_img)

    buf = io.BytesIO()
    result_image.save(buf, format="JPEG")
    byte_im = buf.getvalue()

    st.download_button(label="Скачать фото", data=byte_im, file_name="smart_photo.jpeg",mime="image/jpeg")

