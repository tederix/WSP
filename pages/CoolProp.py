import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import numpy as np
import CoolProp.CoolProp as CP
import WSP

st.set_page_config(page_title="CoolProp", page_icon="💦")

#функция "переадресации" ошибок
def chek(funk):
    try:
        funk()
    except: "Нет значения"

with st.sidebar:
    page1 = st.selectbox("Выберите вещество", ["Вода", "Диоксид углерода", "Воздух", "Кислород", "Водород",
                                               "Указать свое из библиотеки Coolprop"])
    if (page1 == "Вода"):
        fluid = 'Water'
        Pmax = 1000000000.0
        Tmax = 2000.0
    if (page1 == "Диоксид углерода"):
        fluid = 'carbondioxide'
        Pmax = 800000000.0
        Tmax = 2000.0
    if (page1 == "Воздух"):
        fluid = 'AIR'
        Pmax = 2000000000.0
        Tmax = 2000.0
    if (page1 == "Кислород"):
        fluid = 'oxygen'
        Pmax = 80000000.0
        Tmax = 2000.0
    if (page1 == "Водород"):
        fluid = 'hydrogen'
        Pmax = 2000000000.0
        Tmax = 1000.0
    if (page1 == "Указать свое из библиотеки Coolprop"):
        st.write("[Список веществ](http://www.coolprop.org/fluid_properties/PurePseudoPure.html#list-of-fluids)")
        fluid = st.text_input('Название вещества:', 'carbondioxide')
        Pmax = 20000000000.0
        Tmax = 50000.0
    st.write("#")
    st.write("Страница проекта на " + "[Github](https://github.com/tederix/WSP)")



page = st.selectbox("Выберите исходные параметры", ["p-T"])
if page == "p-T":
    p = st.number_input('Введите давление p, МПа', max_value = Pmax/10**6)
    T = st.number_input('Введите температуру T, С', max_value = Tmax - 273.15)
    p=p*10**6
    T=T+273.15
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Свойства')
        st.write(""" p = """ + str('{:.6}'.format(p/10**6)) + " МПа" )
        st.write(""" T = """ + str('{:.6}'.format(T-273.15)) + " С" )
        st.write("""  """)

        f = lambda: st.write(
            """ h = """ + str('{:.6}'.format((CP.PropsSI('H','P', p,'T', T, fluid))/1000)) + """ кДж/кг""")
        chek(f)
        f = lambda: st.write(
            """ s = """ + str('{:.6}'.format((CP.PropsSI('S','P', p,'T', T, fluid))/1000)) + """ кДж/(кг*°C)""")
        chek(f)
        st.write("""  """)
        f = lambda: st.write(
            """ v = """ + str('{:.6}'.format(1/CP.PropsSI('D','P', p,'T', T, fluid))) + """ м³/кг""")
        chek(f)
        f = lambda: st.write(
            """ ρ = """ + str('{:.6}'.format((CP.PropsSI('D','P', p,'T', T, fluid)))) + """ кг/м³""")
        chek(f)
        f = lambda: st.write(
            """ u = """ + str('{:.6}'.format((CP.PropsSI('U','P', p,'T', T, fluid))/1000)) + """ кДж/кг""")
        chek(f)
        f = lambda: st.write(
            """ cp = """ + str('{:.6}'.format((CP.PropsSI('C','P', p,'T', T, fluid))/1000)) + """ кДж/(кг*°C)""")
        chek(f)
        f = lambda: st.write(
            """ cv = """ + str('{:.6}'.format((CP.PropsSI('O','P', p,'T', T, fluid))/1000)) + """ кДж/(кг*°C)""")
        chek(f)
        f = lambda: st.write(
            """ λ = """ + str('{:.6}'.format((CP.PropsSI('conductivity','P', p,'T', T, fluid)))) + """ Вт/(м*°C)""")
        chek(f)
        f = lambda: st.write(
            """ μ = """ + str('{:.6}'.format(CP.PropsSI('viscosity','P', p,'T', T, fluid))) + """ Па*с""")
        chek(f)
        f = lambda: st.write(
            """ ν = """ + str('{:.6}'.format((CP.PropsSI('viscosity','P', p,'T', T, fluid)/CP.PropsSI('D','P', p,'T', T, fluid)))) + """ м²/с""")
        chek(f)
        f = lambda: st.write(
            """ Pr = """ + str('{:.6}'.format((CP.PropsSI('Prandtl','P', p,'T', T, fluid)))) + """""")
        chek(f)
        st.write("""  """)
        f = lambda: st.write(""" w = """ + str('{:.6}'.format((CP.PropsSI('speed_of_sound','P', p,'T', T, fluid)))) + """ м/с""")
        chek(f)
        f = lambda: st.write(""" k = """ + str('{:.6}'.format((CP.PropsSI('isentropic_expansion_coefficient','P', p,'T', T, fluid)))) + """""")
        chek(f)

        with col2:
            with st.expander("Показать названия свойств", expanded=True):
                st.write("""  """)
                st.write(""" Давление """)
                st.write(""" Температура """)
                st.write("""  """)
                st.write(""" Удельная энтальпия """)
                st.write(""" Удельная энтропия """)
                WSP.text_1()