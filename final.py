
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="FutureLab AI Assistant",
    page_icon="🧪",
    layout="wide"
)

col1, col2, col3 = st.columns([1, 2.2, 1])

with col2:
    st.title("🧪 FutureLab AI Assistant")
    st.subheader("Твой помощник по физике, химии и биологии")

with col3:
     st.caption("Created by Mariia Malykh")
     st.caption("For support or issues, contact me on Telegram: @Mar_isi")


def ask_ai(question, history=None):

    if not API_KEY:
        return None, "API-ключ Groq не найден. Проверь файл .env"

    try:
        client = Groq(api_key=API_KEY)

        messages = [
            {
                "role": "system",
                "content": """
                Ты FutureLab AI Assistant.
                Ты помогаешь школьникам изучать физику,
                химию и биологию.

                Объясняй сложные темы простыми словами,
                как ученику 8 класса.

                Отвечай понятно, дружелюбно и с примерами.
                Если ученик чего-то не понимает,
                объясни ещё проще.

                При создании опытов обязательно указывай:
                название, цель, материалы, ход работы,
                ожидаемый результат и научное объяснение.

                Предлагай только безопасные школьные опыты.
                Используй обычные безопасные материалы.
                Не предлагай огонь, опасные химикаты,
                токсичные вещества, электрические эксперименты
                или рискованные действия.
                """
            }
        ]

        if history:
            messages.extend(history)

        messages.append({
            "role": "user",
            "content": question
        })

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=0.7,
            max_completion_tokens=1500
        )

        answer = response.choices[0].message.content

        if not answer:
            return None, "AI не вернул ответ. Попробуй ещё раз."

        return answer, None

    except Exception as e:
        return None, str(e)


tab1, tab2, tab3 = st.tabs([
    "💬 AI Чат",
    "🔬 Объяснение явлений",
    "🧪 Создание опытов"
])


with tab1:

    st.header("💬 Чат с искусственным интеллектом")
    st.write("Задавай вопросы по физике, химии и биологии!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    question = st.text_area(
        "Твой вопрос",
        key="chat_question"
    )

    if st.button("Спросить AI", key="chat_button"):

        if not question.strip():
            st.warning("Сначала напиши вопрос!")

        else:
            old_history = st.session_state.chat_history.copy()

            with st.spinner("AI думает..."):
                answer, error = ask_ai(question, old_history)

            if error:
                st.error("Ошибка Groq API: " + error)

            else:
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": question
                })

                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": answer
                })

                st.rerun()

    if st.button("Очистить чат", key="clear_chat"):
        st.session_state.chat_history = []
        st.rerun()


with tab2:

    st.header("🔬 Объяснение научных явлений")

    subject = st.selectbox(
        "Выбери предмет",
        ["Физика", "Химия", "Биология"]
    )

    phenomenon = st.text_area(
        "Какое явление нужно объяснить?",
        placeholder="Например: почему лёд плавает в воде?"
    )

    if st.button("Объяснить", key="explain_button"):

        if not phenomenon.strip():
            st.warning("Напиши название явления!")

        else:
            prompt = (
                "Объясни явление по предмету "
                + subject + ": " + phenomenon
                + ". Объясни простыми словами и приведи пример."
            )

            with st.spinner("Готовлю объяснение..."):
                answer, error = ask_ai(prompt)

            if error:
                st.error("Ошибка Groq API: " + error)

            else:
                st.subheader("Ответ AI")
                st.write(answer)


with tab3:

    st.header("🧪 Создание школьных опытов")

    experiment_subject = st.selectbox(
        "Выбери предмет",
        ["Физика", "Химия", "Биология"],
        key="experiment_subject"
    )

    topic = st.text_area(
        "На какую тему нужен опыт?",
        placeholder="Например: плотность воды"
    )

    if st.button("Создать опыт", key="experiment_button"):

        if not topic.strip():
            st.warning("Сначала напиши тему!")

        else:
            prompt = (
                "Придумай простой и безопасный школьный опыт "
                "по предмету " + experiment_subject
                + " на тему: " + topic
                + ". Укажи название, цель, материалы, "
                + "ход работы, ожидаемый результат "
                + "и научное объяснение. "
                + "Ответ должен быть подробным, "
                + "полным и понятным ученику 8 класса. "
                + "Используй только обычные безопасные материалы. "
                + "Не используй огонь, опасные химикаты, "
                + "электричество, токсичные вещества "
                + "или рискованные действия."
            )

            with st.spinner("Придумываю опыт..."):
                answer, error = ask_ai(prompt)

            if error:
                st.error("Ошибка Groq API: " + error)

            else:
                st.subheader("Твой опыт")
                st.write(answer)
