import streamlit as st
from iapws import IAPWS97



page = st.selectbox("Выберите страницу", ["p-T", "p-h", "p-s", "h-s", "p-x", "T-x"])



if page == "p-T":
    p = st.number_input('Введите давление p, МПа')
    T = st.number_input('Введите температуру T, °C')

    col1, col2 = st.columns(2)

    with col1:
        st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
        st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
        st.write("""  """)
        st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).h)) + """ кДж/кг""")
        st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).s)) + """ кДж/(кг*°C)""")
        st.write("""  """)
        st.write(""" v = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).v)) + """ м³/кг""")
        st.write(""" ρ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).rho)) + """ кг/м³""")
        st.write(""" u = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).u)) + """ кДж/кг""")
        st.write(""" cp = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cp)) + """ кДж/(кг*°C)""")
        st.write(""" cv = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).cv)) + """ кДж/(кг*°C)""")
        st.write(""" λ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).k)) + """ Вт/(м*°C)""")
        st.write(""" μ = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).mu)) + """ Па*с""")
        st.write(""" ν = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).nu)) + """ м²/с""")
        st.write(""" Pr = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).Prandt)) + """""")
        st.write("""  """)
        st.write(""" w = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).w)) + """ м²/с""")
        #st.write(""" k = """ + str('{:.6}'.format(IAPWS97(P=p, T=T + 273.15).gamma)) + """""")

    with col2:
        st.write(""" Давление """)
        st.write(""" Температура """)
        st.write("""  """)
        st.write(""" Удельная энтальпия """)
        st.write(""" Удельная энтропия """)
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
        #st.write(""" Коэф. изоэнтропы """)




if page == "p-h":
    p = st.number_input('Введите давление p, МПа')
    h = st.number_input('Введите энтальпию h, кДж/кг')


    st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
    st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
    st.write("""  """)
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
    st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
    st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x)*100)) + """ %""")


if page == "p-s":
    p = st.number_input('Введите давление p, МПа')
    s = st.number_input('Введите энтропию s, кДж/(кг*°C)')

    st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
    st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
    st.write("""  """)
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
    st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
    st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x)*100)) + """ %""")


if page == "h-s":
    h = st.number_input('Введите энтальпию h, кДж/кг')
    s = st.number_input('Введите энтропию s, кДж/(кг*°C)')

    st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
    st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
    st.write("""  """)
    st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
    st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x)*100)) + """ %""")


if page == "p-x":
    p = st.number_input('Введите давление p, МПа')
    x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

    st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
    st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
    st.write("""  """)
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x/100).T) - 273.15)) + """ °C""")
    st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).h)) + """ кДж/кг""")
    st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).s)) + """ кДж/(кг*°C)""")


if page == "T-x":
    T = st.number_input('Введите температуру T, °C')
    x = st.number_input('Введите степень сухости x, %', min_value=0.0, max_value=100.0)

    st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
    st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
    st.write("""  """)
    st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T+273.15, x=x/100).P))) + """ МПа""")
    st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).h)) + """ кДж/кг""")
    st.write(""" s = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).s)) + """ кДж/(кг*°C)""")


