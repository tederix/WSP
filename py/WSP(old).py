import streamlit as st
from iapws import IAPWS97



page = st.selectbox("Выберите страницу", ["p-T", "p-h", "p-s", "h-s", "p-x", "T-x"])



if page == "p-T":
    p = st.number_input('Введите давление, МПа')
    T = st.number_input('Введите температуру, °C')


    st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
    st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
    st.write("""  """)
    st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, T=T+273.15).h)) + """ кДж/кг""")
    st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, T=T+273.15).s)) + """ кДж/(кг*°C)""")


if page == "p-h":
    p = st.number_input('Введите давление, МПа')
    h = st.number_input('Введите энтальпию, кДж/кг')


    st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
    st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
    st.write("""  """)
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, h=h).T) - 273.15)) + """ °C""")
    st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, h=h).s)) + """ кДж/(кг*°C)""")
    st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, h=h).x)*100)) + """ %""")


if page == "p-s":
    p = st.number_input('Введите давление, МПа')
    s = st.number_input('Введите энтропию, кДж/(кг*°C)')

    st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
    st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
    st.write("""  """)
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, s=s).T) - 273.15)) + """ °C""")
    st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, s=s).h)) + """ кДж/кг""")
    st.write(""" x = """ + str('{:.4}'.format((IAPWS97(P=p, s=s).x)*100)) + """ %""")


if page == "h-s":
    h = st.number_input('Введите энтальпию, кДж/кг')
    s = st.number_input('Введите энтропию, кДж/(кг*°C)')

    st.write(""" h = """ + str('{:.6}'.format(h)) + """ кДж/кг""")
    st.write(""" s = """ + str('{:.6}'.format(s)) + """ кДж/(кг*°C)""")
    st.write("""  """)
    st.write(""" p = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).P))) + """ МПа""")
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(h=h, s=s).T) - 273.15)) + """ °C""")
    st.write(""" x = """ + str('{:.4}'.format((IAPWS97(h=h, s=s).x)*100)) + """ %""")


if page == "p-x":
    p = st.number_input('Введите давление, МПа')
    x = st.number_input('Введите степень сухости, %')

    st.write(""" p = """ + str('{:.6}'.format(p)) + """ МПа""")
    st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
    st.write("""  """)
    st.write(""" T = """ + str('{:.6}'.format((IAPWS97(P=p, x=x/100).T) - 273.15)) + """ °C""")
    st.write(""" h = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).h)) + """ кДж/кг""")
    st.write(""" s = """ + str('{:.6}'.format(IAPWS97(P=p, x=x/100).s)) + """ кДж/(кг*°C)""")


if page == "T-x":
    T = st.number_input('Введите температуру, °C')
    x = st.number_input('Введите степень сухости, %')

    st.write(""" T = """ + str('{:.6}'.format(T)) + """ °C""")
    st.write(""" x = """ + str('{:.6}'.format(x)) + """ %""")
    st.write("""  """)
    st.write(""" p = """ + str('{:.4}'.format((IAPWS97(T=T+273.15, x=x/100).P))) + """ МПа""")
    st.write(""" h = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).h)) + """ кДж/кг""")
    st.write(""" s = """ + str('{:.6}'.format(IAPWS97(T=T+273.15, x=x/100).s)) + """ кДж/(кг*°C)""")


