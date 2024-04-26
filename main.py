import streamlit as st
from st_pages import Page, show_pages, add_page_title


def wrap():
    st.set_page_config(
        page_title="Joule heating",
        page_icon="♨️",
    )
    page_bg = """
        <style>
        [data-testid="stSidebarContent"]{
        background-color: #ffffff;
        background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #ffffff 40px ), repeating-linear-gradient( #dadada55, #dadada );
        font-weight: 300;
        font-family: monospace;
        }
        [class="main st-emotion-cache-uf99v8 ea3mdgi8"]{
        background-color: #ffffff;
        font-weight: 300;
        font-family: monospace;
        }
        </style>
        """
    st.markdown(page_bg, unsafe_allow_html=True)


def main():
    wrap()
    st.title("Проект 4.")

    st.header("Численное моделирование задачи о джоулевом нагреве. ")

    show_pages(
        [
            Page("main.py", "Введение", "♨️"),
            Page("tasks.py","Цели и задачи", "♨️"),
            Page("formulation.py", "Постановка задачи", "♨️"),
            Page("realization.py", "Реализация", "♨️"),
        ]
    )

    st.subheader("Работу выполнили студенты МГУ Саров из группы ВМ-123:")
    st.write(
        """
                - Файн Евгений
                - Устюжанин Илья
                - Шапаренко Владислав
                - Хасанов Максим
                """

          
    )


if __name__ == "__main__":
    main()
