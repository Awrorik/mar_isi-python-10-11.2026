import streamlit as st
st.title("Привет это мой первый сайт")
st.title("давай поговорим")
c1,c2, c3, c4 = st.columns(4)

with c1:
    user_name = st.text_input("как тебя зовут?")
    st.button("сказать свое имя")

    if user_name :
         st.success(f"Привет {user_name} рада тебя видеть🐈‍⬛")
    else:
         st.warning(" сначала введи свое имя")


with c2:
    st.title("Меня зовут маша")
    st.write("Мне 13 лет ")

    user_name = st.text_input(" можем пообщатся ")
    st.button("написать ")
with c3:
    
    if user_name :
             st.success(f" ответ пользователю : все хорошо!")
    else:
             st.warning("пользователь для начала введи сообщение!")

with c4:
    st.subheader(" Моя фотка внизу  ")     
    uploaded_file = st.file_uploader(" ✨✨", type =["png"," jpg", "jpeg"])   
      
    if uploaded_file is not None :
     st.image(uploaded_file, use_container_width=True)


    st.set_page_config(page_title="Самый лучший сайт в мире",page_icon="https://www.flaticon.com/free-icon/vampire_570863", layout="wide")
st.title("Привет ты зашел на самый лучший сайт в мире")
import streamlit as st
tab1, tab2 = st.tabs(["Про меня",  "что я продаю "])
with tab1: 
  st.header(" факты про меня")

  col1, col2 =st.columns([1,2 ])
  with col1:
   st.image("5397566589110001791.jpg",width=200)
   with col2:
     st.subheader("мне 13 лет и я учусь в компьютерной академии шаг и хожу на танцы")

     with st.container():
       st.info("контакты для связи")
       st.markdown("- telegram Mar_isi")
       st.markdown("email - mariamalyh488@gmail.com")

with tab2:
    st .info






