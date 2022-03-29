import streamlit as st
from iapws import IAPWS97
from iapws import IAPWS95
import json
import requests
from streamlit_lottie import st_lottie
import numpy as np

def chek(funk):
    try:
        funk()
    except: "Нет значения"




def text_1():
    st.write("""  """)
    st.write(""" Удельный объем """)
    st.write(""" Плотность """)
    st.write(""" Удельная внутренняя энергия """)
    st.write(""" Удельная изобарная теплоемкость """)
    st.write(""" Удельная изохорная теплоемкость """)
    st.write(""" Коэф. теплопроводности """)
    st.write(""" Динамическая вязкость """)
    st.write(""" Кинематическая вязкость """)
    st.write(""" Число Прандтля""")
    st.write("""  """)
    st.write(""" Скорость звука""")
    st.write(""" Коэф. изоэнтропы """)
def text_2():
    st.write("""  """)
    st.write("""Удельный объем """)
    st.write("""Плотность""")
    st.write("""Уд. внутренняя энергия""")
    st.write("""Уд. изобарная тепл.""")
    st.write("""Уд. изохорная тепл""")
    st.write("""Коэф. теплопроводности""")
    st.write("""Динамическая вязкость""")
    st.write("""Кинематическая вязкость""")
    st.write("""Число Прандтля""")
    st.write("""  """)
    st.write("""Скорость звука""")
    st.write("""Коэф. изоэнтропы""")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_ps = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_pz3drqq8.json")
lottie_cat1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_yriifcob.json")
lottie_cat2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ldqqbtdk.json")
lottie_cat3 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zrn901s1.json")

st.set_page_config(
     page_title="IAPWS",
     page_icon="💨",
 )



with st.sidebar:
    page = st.selectbox(
        "Выберите количество страниц?",
        ("Одна", "Две", "Три")
    )

    st.write("#")


    st.write("## Раздел в разработке")


    P = st.radio(
        "Выберите размерность давления:",
        ('кПа', 'бар', 'атм', 'МПа'), index = 3)
    T = st.radio(
        "Выберите размерность давления:",
        ('K', '°C'), index = 1)
    st.write("## Раздел в разработке")



    if(page == "Одна"):
        st_lottie(lottie_cat1, height=250, key='cat1')
    if (page == "Две"):
        st_lottie(lottie_cat2, height=250, key='cat2')
    if (page == "Три"):
        st_lottie(lottie_cat3, height=250, key='cat3', speed=0.5)


    st.write("Страница проекта на " + "[Github](https://github.com/tederix/WSP)")
    #st.write("https://github.com/tederix/WSP")

if page == "Одна":

    page = st.selectbox("Выберите исходные параметры", ["p-T", "p-h", "p-s", "h-s", "p-x", "T-x"])

    if page == "p-T":
        p = st.number_input('Введите давление p, МПа')
        T = st.number_input('Введите температуру T, °C')

        col1, col2 = st.columns(2)

        with col1:

            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            st.write("""  """)

            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).gamma)) + """""")
            chek(f)


        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Температура """)
                st.write("""  """)
                st.write(""" Удельная энтальпия """)
                st.write(""" Удельная энтропия """)
                st.write("""  """)
                text_1()


    if page == "p-h":
        p = st.number_input('Введите давление p, МПа')
        h = st.number_input('Введите энтальпию h, кДж/кг')

        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write("""  """)



            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x)*100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).gamma)) + """""")
            chek(f)

        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Удельная энтальпия """)
                st.write("""  """)
                st.write(""" Температура """)
                st.write(""" Удельная энтропия """)
                st.write(""" Степень сухости """)
                text_1()


    if page == "p-s":
        p = st.number_input('Введите давление p, МПа')
        s = st.number_input('Введите энтропию s, кДж/(кг*°C)')
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            st.write("""  """)

            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
            chek(f)
            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x)*100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).gamma)) + """""")
            chek(f)

        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Удельная энтропия """)
                st.write("""  """)
                st.write(""" Температура """)
                st.write(""" Удельная энтальпия""")
                st.write(""" Степень сухости """)
                text_1()


    if page == "h-s":
        h = st.number_input('Введите энтальпию h, кДж/кг')
        s = st.number_input('Введите энтропию s, кДж/(кг*°C)')

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            st.write("""  """)

            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
            chek(f)
            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
            chek(f)
            f = lambda:st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x)*100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).gamma)) + """""")
            chek(f)

        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Удельная энтальпия """)
                st.write(""" Удельная энтропия """)
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Температура """)
                st.write(""" Степень сухости """)
                st.write("""  """)
                text_1()


    if page == "p-x":
        p = st.number_input('Введите давление p, МПа')
        x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)

            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x/100).T) - 273.15)) + """ °C""")
            chek(f)
            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS95(P=p, x=x/100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(P=p, x=x/100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, x=x/100).gamma)) + """""")
            chek(f)

            if x == 100: x = x-0.001
            elif x == 0: x = x + 0.001
            else: x = x

            f = lambda:st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)


        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Степень сухости """)
                st.write("""  """)
                st.write(""" Температура """)
                st.write(""" Удельная энтальпия """)
                st.write(""" Удельная энтропия """)
                text_1()
                st.write(""" Уд. теплота парообразования """)


    if page == "T-x":
        T = st.number_input('Введите температуру T, °C')
        x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)

            f = lambda:st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T+273.15, x=x/100).P))) + """ МПа""")
            chek(f)
            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS95(T=T+273.15, x=x/100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(T=T+273.15, x=x/100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(T=T+273.15, x=x/100).gamma)) + """""")
            chek(f)

            if x == 100: x = x-0.001
            elif x == 0: x = x + 0.001
            else: x = x

            f = lambda:st.write(""" r = """ + str('{:.6}'.format(IAPWS95(T=T+273.15, x=x/100).Hvap)) + """ кДж/кг""")
            chek(f)

        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Температура """)
                st.write(""" Степень сухости """)
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Удельная энтальпия """)
                st.write(""" Удельная энтропия """)
                text_1()
                st.write(""" Уд. теплота парообразования """)

if page == "Две":

    col1, col2, col3 = st.columns(3)

    with col1:
        page = st.selectbox("Выберите исходные параметры", ["p-T", "p-h", "p-s", "h-s", "p-x", "T-x"])
        if page == "p-T":
            p = st.number_input('Введите давление p, МПа')
            T = st.number_input('Введите температуру T, °C')


            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).x)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "p-h":
            p = st.number_input('Введите давление p, МПа')
            h = st.number_input('Введите энтальпию h, кДж/кг')


            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "p-s":
            p = st.number_input('Введите давление p, МПа')
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)')

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
            chek(f)
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "h-s":
            h = st.number_input('Введите энтальпию h, кДж/кг')
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)')

            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
            chek(f)
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "p-x":
            p = st.number_input('Введите давление p, МПа')
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x / 100).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "T-x":
            T = st.number_input('Введите температуру T, °C')
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T + 273.15, x=x / 100).P))) + """ МПа""")
            chek(f)
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

    with col2:
        page1 = st.selectbox("Выберите исходные параметры", ["p-T ", "p-h ", "p-s ", "h-s ", "p-x ", "T-x "])
        if page1 == "p-T ":
            p = st.number_input('Введите давление p, МПа', key=1)
            T = st.number_input('Введите температуру T, °C', key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).x)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "p-h ":
            p = st.number_input('Введите давление p, МПа', key=1)
            h = st.number_input('Введите энтальпию h, кДж/кг', key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "p-s ":
            p = st.number_input('Введите давление p, МПа', key=1)
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
            chek(f)
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "h-s ":
            h = st.number_input('Введите энтальпию h, кДж/кг', key=1)
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=1)

            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
            chek(f)
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "p-x ":
            p = st.number_input('Введите давление p, МПа', key=1)
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x / 100).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "T-x ":
            T = st.number_input('Введите температуру T, °C', key=1)
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=1)

            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T + 273.15, x=x / 100).P))) + """ МПа""")
            chek(f)
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ s = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ λ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(
                """ r = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

    with col3:
        #st.write("""#""")
        #st.write("""#""")
        #st.write("""#""")
        #st.write("""#""")
        #st.write("""  """)
        #st.write("""  """)
        #st.write("""  """)
        #st.write("""  """)
        #st.write("""  """)

        st_lottie(lottie_ps, height=200, key='ps')



        with st.expander("Показать названия свойств", expanded=True):
            st.write("""  """)
            st.write(""" Давление """)
            st.write(""" Температура """)
            st.write("""  """)
            st.write(""" Удельная энтальпия """)
            st.write(""" Удельная энтропия """)
            st.write(""" Степень сухости """)
            text_2()
            st.write(""" Уд. теплота пар-ния """)

if page == "Три":
    col1, col2, col3 = st.columns(3)

    with col1:
        page = st.selectbox("Выберите исходные параметры", ["p-T", "p-h", "p-s", "h-s", "p-x", "T-x"])
        if page == "p-T":
            p = st.number_input('Введите давление p, МПа')
            T = st.number_input('Введите температуру T, °C')

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).x)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "p-h":
            p = st.number_input('Введите давление p, МПа')
            h = st.number_input('Введите энтальпию h, кДж/кг')

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "p-s":
            p = st.number_input('Введите давление p, МПа')
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)')

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
            chek(f)
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "h-s":
            h = st.number_input('Введите энтальпию h, кДж/кг')
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)')

            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
            chek(f)
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "p-x":
            p = st.number_input('Введите давление p, МПа')
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x / 100).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

        if page == "T-x":
            T = st.number_input('Введите температуру T, °C')
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T + 273.15, x=x / 100).P))) + """ МПа""")
            chek(f)
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ s = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ λ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(
                """ r = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

    with col2:
        page1 = st.selectbox("Выберите исходные параметры", ["p-T ", "p-h ", "p-s ", "h-s ", "p-x ", "T-x "])
        if page1 == "p-T ":
            p = st.number_input('Введите давление p, МПа', key=1)
            T = st.number_input('Введите температуру T, °C', key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).x)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "p-h ":
            p = st.number_input('Введите давление p, МПа', key=1)
            h = st.number_input('Введите энтальпию h, кДж/кг', key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "p-s ":
            p = st.number_input('Введите давление p, МПа', key=1)
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
            chek(f)
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "h-s ":
            h = st.number_input('Введите энтальпию h, кДж/кг', key=1)
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=1)

            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
            chek(f)
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "p-x ":
            p = st.number_input('Введите давление p, МПа', key=1)
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=1)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x / 100).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

        if page1 == "T-x ":
            T = st.number_input('Введите температуру T, °C', key=1)
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=1)

            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T + 273.15, x=x / 100).P))) + """ МПа""")
            chek(f)
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ s = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ λ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(
                """ r = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

    with col3:
        page2 = st.selectbox("Выберите исходные параметры", [" p-T ", " p-h ", " p-s ", " h-s ", " p-x ", " T-x "])
        if page2 == " p-T ":
            p = st.number_input('Введите давление p, МПа', key=2)
            T = st.number_input('Введите температуру T, °C', key=2)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).x)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, T=T + 273.15).Hvap)) + """ кДж/кг""")
            chek(f)

        if page2 == " p-h ":
            p = st.number_input('Введите давление p, МПа', key=2)
            h = st.number_input('Введите энтальпию h, кДж/кг', key=2)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, h=h).Hvap)) + """ кДж/кг""")
            chek(f)

        if page2 == " p-s ":
            p = st.number_input('Введите давление p, МПа', key=2)
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=2)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
            chek(f)
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page2 == " h-s ":
            h = st.number_input('Введите энтальпию h, кДж/кг', key=2)
            s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=2)

            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
            chek(f)
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            f = lambda: st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x) * 100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(h=h, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).gamma)) + """""")
            chek(f)
            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(h=h, s=s).Hvap)) + """ кДж/кг""")
            chek(f)

        if page2 == " p-x ":
            p = st.number_input('Введите давление p, МПа', key=2)
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=2)

            st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
            f = lambda: st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x / 100).T) - 273.15)) + """ °C""")
            chek(f)

            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)

        if page2 == " T-x ":
            T = st.number_input('Введите температуру T, °C', key=2)
            x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=2)

            st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T + 273.15, x=x / 100).P))) + """ МПа""")
            chek(f)
            st.write("""  """)

            f = lambda: st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ s = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ λ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15, x=x / 100).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).gamma)) + """""")
            chek(f)

            if x == 100:
                x = x - 0.001
            elif x == 0:
                x = x + 0.001
            else:
                x = x

            f = lambda: st.write(
                """ r = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15, x=x / 100).Hvap)) + """ кДж/кг""")
            chek(f)
