
import streamlit as st
st.set_page_config(page_title="Mar_isi/world",page_icon="https://www.flaticon.com/free-icon/vampire_570863", layout="wide")
st.title("Привет, ты на сайте Mar_isi")
import streamlit as st
tab1, tab2, tab3  = st.tabs(["Про меня", "Путешествия", "Полезные ссылки"])
with tab1: 
  st.header("факты про меня")
  col1, col2 =st.columns([1,2 ])
  with col1:
   st.image("photo_2026-10-29_20-27-18.jpg", caption="моя фотка")
   with col2:
     st.title("мне 13 лет и я учусь в компьютерной академии шаг и хожу на pole dance")

     with st.container():
       st.subheader(":yellow[контакты для связи]")
       st.markdown(":yellow[telegram - Mar_isi]")
       st.markdown(":yellow[email - mariamalyh488@gmail.com]")

with tab2:
    st .header(" в каких странах я была")
    col1, col2, col3, col4 =st.columns([1.7,4,2,4])
    with col1:
        st.image("photo_2026-10-29_21-04-51.jpg",use_container_width=True, width=500 , caption="бухарест🤍")
    with col2:
      st.subheader(" :Румыния ")
      st.write(":yellow[- первая страна в списке стран в которых я была,туда я часто приезжяю, Руміния мне как второй дом,но есть и минусы. в Бухаресте я бываю намного чаще и там довольно шумно так как это столица румынии, так же, еще один огромный минус это то, что там нету моря и изза этого там повышена температура, она отличается от температуры в Одессе на 2-4 и больше градусов, в зависимости от времени года, летом в Бухаресте температура может доходить до 46 градусов! для меня это большой минус, так как я не люблю жару.]")
    with col3:
        st.image("photo_2026-10-29_21-47-35.jpg", use_container_width=True , width=350, caption="Германия🤍")
    with col4:
        st.subheader(":Германия" )
        st.write(":yellow[-Я прилетала в Германию на неделю к своей сестре, она там живет уже два года и захотела показать мне страну, была я в Фридрисхафене,Мюнхене,Штутгарте,Амберге,Боденском озере,Констанце. Хочу сказать, что Германия понравилась мне больше чем румыния, своими максимально чистыми городками, красивыми домами,очень добрыми и отзывчивыми людьми, была я в июне и мне очень понравилось, собираюсь прилететь повторнов германию зимой, но уже точно больше чем на неделю)).]")

    col5,col6,col7,col8=st.columns([1.8,4,2,4])
    with col5:
        st.image("photo_2026-10-29_22-29-01.jpg", use_container_width=True , width=350, caption="Болгария🤍")
        with col6:
            st.subheader("Болгария ")
            st.write(":yellow[-Я приезжяла в Болгарию :yellow[20 Августа] на отдых была я в Софии,Балчике,Крапеце. Болгария мне понравилась красивой природой, уютными улицами и чистым морем. Мне очень понравилось отдыхать этим летом в Варне, в остальных городах мне нравилось наслаждаться атмосферой этой страны по фотке можно понять что летом на отдых прилетала также моя сестра, Мы посмотрели очень много красивых мест, у меня осталось много приятных воспоминаний.]")

        with col7:
           st.image("photo_2026-10-29_22-44-30.jpg", use_container_width=True , width=350, caption="Швейцария🤍")
        with col8:
            st.subheader(":Швейцария ")
            st.write(":yellow[- Когда я была в фридрисхафене мы с семьей решили поехать в Швейцарию на яхте, переплыв Боденское озеро мы ездили осматривая Швейцарию. была я в Цюрихе,Романсрохне,санкт-галлене. Швейцария такая же чистая как и германия, мне понравилось там,я бы также хотела там жить, там очень красивые горы и там делают вкусный шоколад, мне понравились очень красвые города и природа,хочу поездить на поезде среди Гор Альп и насладится видом гор]")
    with tab3:
     
     st.title("Полезные ссылки ")
     st.subheader(" несколько полезных ссылок на сайты, которые про путешествия:")
     col1,col2,col3=st.columns([2,2,1.5])
     with col1:
      st.markdown(":yellow[ссылки на сайты]:")
      st.write(":yellow[https://trips.com.ua/?utm_source]")
      st.write(":yellow[https://ukrainaincognita.com/?utm_source]")
      st.write(":yellow[https://visitukraine.today/?utm_source]")
      with col2:
         st.markdown(":yellow[про путешествия в мире:]")
         st.write(":yellow[https://ua-travels.in.ua/?utm_source]")
         st.write(":yellow[https://wanderlust.com.ua/?utm_source]")
         st.write(":yellow[https://discover.in.ua/?utm_source]")
    with col3:
          st.image("photo_2026-10-30_15-40-28.jpg")

    st.title("Игра угадай число")
    import random
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.subheader("🎲 Игра: Угадай число от 1 до 100 🤍")
    
user_guess = st.number_input("Твой вариант:", min_value=1, max_value=100, step=1)
    
if st.button("Проверить"):
        st.session_state.attempts += 1
        if user_guess < st.session_state.secret_number:
            st.info("📈Число Больше!")
        elif user_guess > st.session_state.secret_number:
            st.info("📉Число Меньше!")
        else:
            st.success(f"🎉 Ура ты угадал число 🙌🏼 {st.session_state.secret_number} за {st.session_state.attempts} спроб!")
            st.session_state.game_over = True
            
if st.button("Играть снова"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
   