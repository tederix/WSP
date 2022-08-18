import streamlit as st
import numpy as np
import CoolProp.CoolProp as CP
from WSP import Vers


st.set_page_config(page_title="CoolProp", page_icon="💦")

#вещества

Sub = {'1-Butene / 1-Бутен': ('1-Butene', 50000000.0, 525.0),
       'Acetone / Ацетон': ('Acetone', 700000000.0, 550.0),
       'Air / Воздух': ('Air', 2000000000.0, 2000.0),
       'Ammonia / Аммиак': ('Ammonia', 1000000000.0, 725.0),
       'Argon / Аргон': ('Argon', 1000000000.0, 2000.0),
       'Benzene / Бензол': ('Benzene', 500000000.0, 725.0),
       'CarbonDioxide / Диоксид углерода': ('CarbonDioxide', 800000000.0, 2000.0),
       'CarbonMonoxide / Монооксид углерода': ('CarbonMonoxide', 100000000.0, 500.0),
       'CarbonylSulfide / Карбонилсульфид': ('CarbonylSulfide', 50000000.0, 650.0),
       'CycloHexane / Циклогексан': ('CycloHexane', 250000000.0, 700.0),
       'CycloPropane / Циклопропан': ('CycloPropane', 28000000.0, 473.0),
       'Cyclopentane / Циклопентан': ('Cyclopentane', 250000000.0, 550.0),
       'D4 / Октаметилциклотетрасилоксан': ('D4', 180000000.0, 1200.0),
       'D5 / Декаметилциклопентасилоксан': ('D5', 120000000.0, 630.0),
       'D6 / Додекаметилциклопентасилоксан': ('D6', 30000000.0, 673.0),
       'Deuterium / Дейтерий': ('Deuterium', 2000000000.0, 600.0),
       'Dichloroethane / 1,2-Дихлорэтан': ('Dichloroethane', 1000000000.0, 1000.0),
       'DiethylEther / Диэтиловый эфир': ('DiethylEther', 100000000.0, 548.0),
       'DimethylCarbonate / Диметилкарбонат': ('DimethylCarbonate', 60000000.0, 600.0),
       'DimethylEther / Диметиловый эфир': ('DimethylEther', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),
       '1-Бутен / 1-Butene': ('1-Butene', 50000000.0, 525.0),

                }

Subst = list(Sub.keys())

#функция "переадресации" ошибок
def chek(funk):
    try:
        funk()
    except: "Нет значения"

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
#боковое меню
with st.sidebar:
    page1 = st.selectbox("Выберите вещество", Subst)
    tab1, tab2 = st.tabs(["Настройки", " "])
    with tab1:
        st.write(Sub[page1][0])
        st.write("#")
        Vers()
        st.write("Страница проекта на " + "[Github](https://github.com/tederix/WSP)")





page = st.selectbox("Выберите исходные параметры", ["p-T"])
if page == "p-T":
    p = st.number_input('Введите давление p, МПа', max_value = (Sub[page1][1])/10**6)
    T = st.number_input('Введите температуру T, С', max_value = (Sub[page1][2]) - 273.15)
    p = p*10**6
    T = T+273.15
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Свойства')
        st.write(""" p = """ + str('{:.6}'.format(p/10**6)) + " МПа")
        st.write(""" T = """ + str('{:.6}'.format(T-273.15)) + " С")
        st.write("""  """)

        f = lambda: st.write(
            """ h = """ + str('{:.6}'.format((CP.PropsSI('H','P', p,'T', T, Sub[page1][0]))/1000)) + """ кДж/кг""")
        chek(f)
        f = lambda: st.write(
            """ s = """ + str('{:.6}'.format((CP.PropsSI('S','P', p,'T', T, Sub[page1][0]))/1000)) + """ кДж/(кг*°C)""")
        chek(f)
        st.write("""  """)
        f = lambda: st.write(
            """ v = """ + str('{:.6}'.format(1/CP.PropsSI('D','P', p,'T', T, Sub[page1][0]))) + """ м³/кг""")
        chek(f)
        f = lambda: st.write(
            """ ρ = """ + str('{:.6}'.format((CP.PropsSI('D','P', p,'T', T, Sub[page1][0])))) + """ кг/м³""")
        chek(f)
        f = lambda: st.write(
            """ u = """ + str('{:.6}'.format((CP.PropsSI('U','P', p,'T', T, Sub[page1][0]))/1000)) + """ кДж/кг""")
        chek(f)
        f = lambda: st.write(
            """ cp = """ + str('{:.6}'.format((CP.PropsSI('C','P', p,'T', T, Sub[page1][0]))/1000)) + """ кДж/(кг*°C)""")
        chek(f)
        f = lambda: st.write(
            """ cv = """ + str('{:.6}'.format((CP.PropsSI('O','P', p,'T', T, Sub[page1][0]))/1000)) + """ кДж/(кг*°C)""")
        chek(f)
        f = lambda: st.write(
            """ λ = """ + str('{:.6}'.format((CP.PropsSI('conductivity','P', p,'T', T, Sub[page1][0])))) + """ Вт/(м*°C)""")
        chek(f)
        f = lambda: st.write(
            """ μ = """ + str('{:.6}'.format(CP.PropsSI('viscosity','P', p,'T', T, Sub[page1][0]))) + """ Па*с""")
        chek(f)
        f = lambda: st.write(
            """ ν = """ + str('{:.6}'.format((CP.PropsSI('viscosity','P', p,'T', T, Sub[page1][0])/CP.PropsSI('D','P', p,'T', T, Sub[page1][0])))) + """ м²/с""")
        chek(f)
        f = lambda: st.write(
            """ Pr = """ + str('{:.6}'.format((CP.PropsSI('Prandtl','P', p,'T', T, Sub[page1][0])))) + """""")
        chek(f)
        st.write("""  """)
        f = lambda: st.write(""" w = """ + str('{:.6}'.format((CP.PropsSI('speed_of_sound','P', p,'T', T, Sub[page1][0])))) + """ м/с""")
        chek(f)
        f = lambda: st.write(""" k = """ + str('{:.6}'.format((CP.PropsSI('isentropic_expansion_coefficient','P', p,'T', T, Sub[page1][0])))) + """""")
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


