import streamlit as st
from iapws import IAPWS97
from iapws import IAPWS95
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import json
import numpy as np
import CoolProp.CoolProp as CP

#функция "переадресации" ошибок
def chek(funk):
    try:
        funk()
    except: "Нет значения"
#текст для IAPWS однотабличный
def text_1():  #текст для IAPWS однотабличный
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
#текст для IAPWS многотабличный
def text_2(): #текст для IAPWS многотабличный
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
#lottie анимации
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#функция поиска действительной точки
def hdres():
    imagehs = Image.open('1.png')
    imagehd = Image.open('2.png')
    st.image(imagehs)
    st.image(imagehd)
    h1 = st.number_input('h1, кДж/кг')
    h2 = st.number_input('h2, кДж/кг')
    eta_oi = st.number_input('ηoi')
    st.write("h2д = " + str('{:.6}'.format(h1-(h1-h2)*eta_oi)) + """ кДж/кг""")
#Использование билиотеки IAPWS для многотабличных страниц
def WSP(key):
    page = st.selectbox("Выберите исходные параметры", ["p-T", "p-h", "p-s", "h-s", "p-x", "T-x"], key = key)
    if page == "p-T":
        p = st.number_input('Введите давление p, МПа', key=key)
        T = st.number_input('Введите температуру T, °C', key=key)

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
        p = st.number_input('Введите давление p, МПа', key=key)
        h = st.number_input('Введите энтальпию h, кДж/кг', key=key)

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
        p = st.number_input('Введите давление p, МПа', key=key)
        s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=key)

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
        h = st.number_input('Введите энтальпию h, кДж/кг', key=key)
        s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key=key)

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
        p = st.number_input('Введите давление p, МПа', key=key)
        x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=key)

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
        T = st.number_input('Введите температуру T, °C', key=key)
        x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key=key)

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

#перечень lottie анимаций (ссылки)
lottie_ps = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_pz3drqq8.json")
lottie_cat1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_yriifcob.json")
lottie_cat2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ldqqbtdk.json")
lottie_cat3 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zrn901s1.json")

#настройки конфигурации страницы
st.set_page_config(
     page_title="IAPWS",
     page_icon="💨",
 )



with st.sidebar:
    page = st.selectbox(
        "Выберите количество страниц?",
        ("Одна", "Две", "Три", "Test Coolprop")
    )

    st.write("#")

    # работа с единицами измерения
    if(page == 'Одна'):
        #Работа с давлением через коэффициенты перевода
        P = st.radio(
            "Выберите размерность давления:",
            ('кПа', 'бар', 'атм', 'МПа'), index = 3)

        if (P == 'кПа'):
            ch = str("кПа")
            k = 1000
        if (P == 'бар'):
            ch = str("бар")
            k = 10
        if (P == 'атм'):
            ch = str("атм")
            k = 9.87
        if (P == 'МПа'):
            ch = str("МПа")
            k = 1
        # Работа с температурой через коэффициенты перевода
        T = st.radio(
            "Выберите размерность температуры:",
            ('K', '°C'), index = 1)
        if (T == 'K'):
            chT = str("K")
            kT = -273.15
        if (T == '°C'):
            chT = str("°C")
            kT = 0

    #включение функции поиска действительной точки
    st.write("#")
    hd = st.checkbox('Поиск действ. точки', value=False)
    if hd:
        hdres()
    #включение анимаций
    lt = 0
    lottie = st.checkbox('Вкл анимации', value=False)
    if lottie:
        lt = 1

    #распределение заранее подготовленных анимаций по страницам
    if (lt == 1):
        if(page == "Одна"):
            st_lottie(lottie_cat1, height=250, key='cat1')
        if (page == "Две"):
            st_lottie(lottie_cat2, height=250, key='cat2')
        if (page == "Три"):
            st_lottie(lottie_cat3, height=250, key='cat3', speed=0.5)

    st.write("Страница проекта на " + "[Github](https://github.com/tederix/WSP)")

if page == "Одна":

    page = st.selectbox("Выберите исходные параметры", ["p-T", "p-h", "p-s", "h-s", "p-x", "T-x"], key=1)

    if page == "p-T":
        p = st.number_input('Введите давление p, ' + ch, key = 1)
        T = st.number_input('Введите температуру T, ' + chT, key = 1)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + " " + ch)
            st.write(""" T = """ + str('{:.6}'.format(T)) + " " + chT)
            st.write("""  """)

            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p/k, T=T + 273.15 + kT).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p/k, T=T + 273.15 + kT).gamma)) + """""")
            chek(f)


        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Температура """)
                st.write("""  """)
                st.write(""" Удельная энтальпия """)
                st.write(""" Удельная энтропия """)
                text_1()

    if page == "p-h":
        p = st.number_input('Введите давление p, ' + ch, key = 1)
        h = st.number_input('Введите энтальпию h, кДж/кг', key = 1)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + " " + ch)
            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write("""  """)



            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p/k, h=h).T) - 273.15 - kT)) + " " + chT)
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).s)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p/k, h=h).x)*100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p/k, h=h).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p/k, h=h).gamma)) + """""")
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
        p = st.number_input('Введите давление p, ' + ch, key = 1)
        s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key = 1)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + " " + ch)
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            st.write("""  """)

            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p/k, s=s).T) - 273.15 - kT)) + " " + chT)
            chek(f)
            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p/k, s=s).x)*100)) + """ %""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p/k, s=s).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p/k, s=s).gamma)) + """""")
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
        h = st.number_input('Введите энтальпию h, кДж/кг', key = 1)
        s = st.number_input('Введите энтропию s, кДж/(кг*°C)', key = 1)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
            st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
            st.write("""  """)

            f = lambda: st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P) * k)) + " " + ch)
            chek(f)
            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15 - kT)) + " " + chT)
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
                text_1()

    if page == "p-x":
        p = st.number_input('Введите давление p, ' + ch, key = 1)
        x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key = 1)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p)) + " " + ch)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)

            f = lambda:st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p/k, x=x/100).T) - 273.15 - kT)) + " " + chT)
            chek(f)
            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS95(P=p/k, x=x/100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(P=p/k, x=x/100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p/k, x=x/100).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p/k, x=x/100).gamma)) + """""")
            chek(f)

            if x == 100: x = x-0.001
            elif x == 0: x = x + 0.001
            else: x = x

            f = lambda:st.write(""" r = """ + str('{:.6}'.format(IAPWS95(P=p/k, x=x / 100).Hvap)) + """ кДж/кг""")
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
        T = st.number_input('Введите температуру T, ' +chT, key = 1)
        x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0, key = 1)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" T = """ + str('{:.6}'.format(T)) + " " + chT)
            st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
            st.write("""  """)

            f = lambda:st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T + 273.15 + kT, x=x/100).P) * k)) + " " + ch)
            chek(f)
            f = lambda:st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).h)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" s = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).s)) + """ кДж/(кг*°C)""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" v = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).v)) + """ м³/кг""")
            chek(f)
            f = lambda:st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).rho)) + """ кг/м³""")
            chek(f)
            f = lambda:st.write(""" u = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).u)) + """ кДж/кг""")
            chek(f)
            f = lambda:st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" cv = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15 + kT, x=x/100).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda:st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda:st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).mu)) + """ Па*с""")
            chek(f)
            f = lambda:st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).nu)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" Pr = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15 + kT, x=x/100).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda:st.write(""" w = """ + str('{:.6}'.format(IAPWS97(T=T + 273.15 + kT, x=x/100).w)) + """ м²/с""")
            chek(f)
            f = lambda:st.write(""" k = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15 + kT, x=x/100).gamma)) + """""")
            chek(f)

            if x == 100: x = x-0.001
            elif x == 0: x = x + 0.001
            else: x = x

            f = lambda:st.write(""" r = """ + str('{:.6}'.format(IAPWS95(T=T + 273.15 + kT, x=x/100).Hvap)) + """ кДж/кг""")
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
        WSP(key=1)
    with col2:
        WSP(key=2)
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
        WSP(key=1)
    with col2:
        WSP(key=2)
    with col3:
        WSP(key=3)


if(page == 'Test Coolprop'):
    page = st.selectbox("Выберите исходные параметры", ["p-T"])

    if page == "p-T":
        p = st.number_input('Введите давление p, МПа')
        T = st.number_input('Введите температуру T, С')
        p=p*10**6
        T=T+273.15
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Свойства')
            st.write(""" p = """ + str('{:.6}'.format(p/10**6)) + " МПа" )
            st.write(""" T = """ + str('{:.6}'.format(T-273.15)) + " С" )
            st.write("""  """)

            f = lambda: st.write(
                """ h = """ + str('{:.6}'.format(CP('H','P', p,'T', T, 'carbondioxide'))) + """ Дж/кг""")
            chek(f)
            f = lambda: st.write(
                """ s = """ + str('{:.6}'.format(CP('S','P', p,'T', T, 'carbondioxide'))) + """ Дж/(кг*°C)""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(
                """ v = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).v)) + """ м³/кг""")
            chek(f)
            f = lambda: st.write(
                """ ρ = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).rho)) + """ кг/м³""")
            chek(f)
            f = lambda: st.write(
                """ u = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).u)) + """ кДж/кг""")
            chek(f)
            f = lambda: st.write(
                """ cp = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).cp)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ cv = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).cv)) + """ кДж/(кг*°C)""")
            chek(f)
            f = lambda: st.write(
                """ λ = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).k)) + """ Вт/(м*°C)""")
            chek(f)
            f = lambda: st.write(
                """ μ = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).mu)) + """ Па*с""")
            chek(f)
            f = lambda: st.write(
                """ ν = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).nu)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(
                """ Pr = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).Prandt)) + """""")
            chek(f)
            st.write("""  """)
            f = lambda: st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p / k, T=T + 273.15 + kT).w)) + """ м²/с""")
            chek(f)
            f = lambda: st.write(""" k = """ + str('{:.6}'.format(IAPWS95(P=p / k, T=T + 273.15 + kT).gamma)) + """""")
            chek(f)

        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Температура """)
                st.write("""  """)
                st.write(""" Удельная энтальпия """)
                st.write(""" Удельная энтропия """)
                text_1()