import streamlit as st
import CoolProp.CoolProp as CP
from WSP import Vers

st.set_page_config(page_title="CoolProp", page_icon="💦")

# вещества
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
       'Ethane / Этан': ('Ethane', 900000000.0, 675.0),
       'Ethanol / Этанол': ('Ethanol', 280000000.0, 650.0),
       'EthylBenzene / Этилбензол': ('EthylBenzene', 60000000.0, 700.0),
       'Ethylene / Этилен': ('Ethylene', 300000000.0, 450.0),
       'EthyleneOxide / Окись этилена': ('EthyleneOxide', 1000000000.0, 1000.0),
       'Fluorine / Фтор': ('Fluorine', 20000000.0, 300.0),
       'HFE143m / RE143A': ('HFE143m', 7200000.0, 420.0),
       'HeavyWater / Тяжёлая вода': ('HeavyWater', 1200000000.0, 825.0),
       'Helium / Гелий': ('Helium', 1000000000.0, 2000.0),
       'Hydrogen / Водород': ('Hydrogen', 2000000000.0, 1000.0),
       'HydrogenChloride / Хлороводород': ('HydrogenChloride', 680000000.0, 670.0),
       'HydrogenSulfide / Сероводород': ('HydrogenSulfide', 170000000.0, 760.0),
       'IsoButane/ Изобутан': ('IsoButane', 35000000.0, 575.0),
       'IsoButene / Изобутилен': ('IsoButene', 50000000.0, 550.0),
       'Isohexane / 2-метилпентан': ('Isohexane', 1000000000.0, 550.0),
       'Isopentane / Изопентан': ('Isopentane', 1000000000.0, 500.0),
       'Krypton / Криптон': ('Krypton', 200000000.0, 750.0),
       'MD2M / Декаметилциклопентасилоксан': ('MD2M', 130000000.0, 600.0),
       'MD3M / Dodecamethylpentasiloxane': ('MD3M', 125000000.0, 673.0),
       'MD4M / Tetradecamethylhexasiloxane': ('MD4M', 125000000.0, 655.0),
       'MDM / Octamethyltrisiloxane': ('MDM', 130000000.0, 575.0),
       'MM / Гексаметилдисилоксан': ('MM', 30000000.0, 673.0),
       'Methane / Метан': ('Methane', 1000000000.0, 625.0),
       'Methanol / Метанол': ('Methanol', 500000000.0, 620.0),
       'MethylLinoleate / MethylLinoleate': ('MethylLinoleate', 50000000.0, 1000.0),
       'MethylOleate / Метилолеат': ('MethylOleate', 50000000.0, 1000.0),
       'MethylPalmitate / Метилпальмитат': ('MethylPalmitate', 50000000.0, 1000.0),
       'MethylStearate / Метилстеарат': ('MethylStearate', 50000000.0, 1000.0),
       'Neon / Неон': ('Neon', 1000000000.0, 725.0),
       'Neopentane / Неопентан': ('Neopentane', 200000000.0, 550.0),
       'Nitrogen / Азот': ('Nitrogen', 2200000000.0, 2000.0),
       'NitrousOxide / Оксид азота': ('NitrousOxide', 50000000.0, 525.0),
       'Novec649 / Novec 649': ('Novec649', 50000000.0, 500.0),
       'OrthoDeuterium / OrthoDeuterium': ('OrthoDeuterium', 2000000000.0, 600.0),
       'OrthoHydrogen / OrthoHydrogen': ('OrthoHydrogen', 2000000000.0, 1000.0),
       'Oxygen / Кислород': ('Oxygen', 80000000.0, 2000.0),
       'ParaDeuterium / ParaDeuterium': ('ParaDeuterium', 2000000000.0, 600.0),
       'ParaHydrogen / ParaHydrogen': ('ParaHydrogen', 2000000000.0, 1000.0),
       'Propylene / Пропилен': ('Propylene', 1000000000.0, 575.0),
       'Propyne / Пропин': ('Propyne', 31800000.0, 474.0),
       'R11 / R11': ('R11', 100000000.0, 625.0),
       'R113 / R113': ('R113', 200000000.0, 525.0),
       'R114 / R114': ('R114', 21000000.0, 507.0),
       'R115 / R115': ('R115', 60000000.0, 550.0),
       'R116 / R116': ('R116', 50000000.0, 425.0),
       'R12 / R12': ('R12', 200000000.0, 525.0),
       'R123 / R123': ('R123', 76000000.0, 600.0),
       'R1233zd(E) / R1233zd(E)': ('R1233zd(E)', 100000000.0, 550.0),
       'R1234yf / R1234yf': ('R1234yf', 30000000.0, 410.0),
       'R1234ze(E) / R1234ze(E)': ('R1234ze(E)', 15000000.0, 420.0),
       'R1234ze(Z) / R1234ze(Z)': ('R1234ze(Z)', 34000000.0, 440.0),
       'R124 / R124': ('R124', 40000000.0, 470.0),
       'R1243zf / R1243zf': ('R1243zf', 30000000.0, 410.0),
       'R125 / R125': ('R125', 60000000.0, 500.0),
       'R13 / R13': ('R13', 50000000.0, 450.0),
       'R134a / R134a': ('R134a', 70000000.0, 455.0),
       'R13I1 / R13I1': ('R13I1', 50000000.0, 420.0),
       'R14 / R14': ('R14', 51000000.0, 623.0),
       'R141b / R141b': ('R141b', 400000000.0, 500.0),
       'R142b / R142b': ('R142b', 60000000.0, 470.0),
       'R143a / R143a': ('R143a', 150000000.0, 650.0),
       'R152A / R152A': ('R152A', 58000000.0, 500.0),
       'R161 / R161': ('R161', 50000000.0, 450.0),
       'R21 / R21': ('R21', 138000000.0, 473.0),
       'R218 / R218': ('R218', 20000000.0, 440.0),
       'R22 / R22': ('R22', 60000000.0, 550.0),
       'R227EA / R227EA': ('R227EA', 60000000.0, 475.0),
       'R23 / R23': ('R23', 120000000.0, 475.0),
       'R236EA / R236EA': ('R236EA', 6000000.0, 412.0),
       'R236FA / R236FA': ('R236FA', 70000000.0, 400.0),
       'R245ca / R245ca': ('R245ca', 10000000.0, 450.0),
       'R245fa / R245fa': ('R245fa', 200000000.0, 440.0),
       'R32 / R32': ('R32', 70000000.0, 435.0),
       'R365MFC / R365MFC': ('R365MFC', 35000000.0, 500.0),
       'R40 / Хлорметан': ('R40', 100000000.0, 730.0),
       'R404A / R404A': ('R404A', 50000000.0, 500.0),
       'R407C / R407C': ('R407C', 50000000.0, 500.0),
       'R41 / R41': ('R41', 70000000.0, 425.0),
       'R410A / R410A': ('R410A', 50000000.0, 500.0),
       'R507A / R507A': ('R507A', 50000000.0, 500.0),
       'RC318 / RC318': ('RC318', 60000000.0, 623.0),
       'SES36 / SES36': ('SES36', 50000000.0, 725.0),
       'SulfurDioxide / Оксид серы(IV)': ('SulfurDioxide', 35000000.0, 525.0),
       'SulfurHexafluoride / Фторид серы (VI)': ('SulfurHexafluoride', 150000000.0, 625.0),
       'Toluene / Толуол': ('Toluene', 50000000.0, 700.0),
       'Water / Вода': ('Water', 1000000000.0, 2000.0),
       'Xenon / Ксенон': ('Xenon', 700000000.0, 750.0),
       'cis-2-Butene / cis-2-Butene': ('cis-2-Butene', 50000000.0, 525.0),
       'm-Xylene / m-Ксилол': ('m-Xylene', 200000000.0, 700.0),
       'n-Butane / n-Бутан': ('n-Butane', 12000000.0, 575.0),
       'n-Decane / n-Декан': ('n-Decane', 800000000.0, 675.0),
       'n-Dodecane / n-Додекан': ('n-Dodecane', 200000000.0, 700.0),
       'n-Heptane / n-Гептан': ('n-Heptane', 100000000.0, 600.0),
       'n-Hexane / n-Гексан': ('n-Hexane', 92000000.0, 600.0),
       'n-Nonane / n-Нонан': ('n-Nonane', 800000000.0, 600.0),
       'n-Octane / n-Октан': ('n-Octane', 1000000000.0, 730.0),
       'n-Pentane / n-Пентан': ('n-Pentane', 780000000.0, 650.0),
       'n-Propane / n-Пропан': ('n-Propane', 1000000000.0, 650.0),
       'n-Undecane / n-Ундекан': ('n-Undecane', 500000000.0, 700.0),
       'o-Xylene / o-Ксилол': ('o-Xylene', 70000000.0, 700.0),
       'p-Xylene / p-Ксилол': ('p-Xylene', 200000000.0, 700.0),
       'trans-2-Butene / Транс-2-бутен': ('trans-2-Butene', 50000000.0, 525.0)
       }
Subst = list(Sub.keys())


# функция "переадресации" ошибок
def chek(funk):
    try:
        funk()
    except:
        "Нет значения"


# текст
def text_1():
    st.write("""  """)
    st.write(""" Давление """)
    st.write(""" Температура """)
    st.write("""  """)
    st.write(""" Удельная энтальпия """)
    st.write(""" Удельная энтропия """)
    st.write(""" Степень сухости """)
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


# Основная функция
def Cool(inp_1, inp_2):
    st.subheader('Свойства')
    # Давление
    if par_1 == "p - давление, МПа" or par_2 == "p - давление, МПа":
        if par_1 == "p - давление, МПа":
            st.write(""" p = """ + str('{:.6}'.format(inp_1 / 10 ** 6)) + " МПа")
        if par_2 == "p - давление, МПа":
            st.write(""" p = """ + str('{:.6}'.format(inp_2 / 10 ** 6)) + " МПа")
    else:
        f = lambda: st.write(""" p = """ + str('{:.6}'.format((CP.PropsSI('P', Parametr[par_1][1], inp_1,
                                                                          Parametr[par_2][1], inp_2,
                                                                          Sub[page1][0])) / 10 ** 6)) + " МПа")
        chek(f)
    # Температура
    if par_1 == "t - температура, °C" or par_2 == "t - температура, °C":
        if par_1 == "t - температура, °C":
            st.write(""" t = """ + str('{:.6}'.format(inp_1 - 273.15)) + " °C")
        if par_2 == "t - температура, °C":
            st.write(""" t = """ + str('{:.6}'.format(inp_2 - 273.15)) + " °C")
    else:
        f = lambda: st.write(""" t = """ + str('{:.6}'.format((CP.PropsSI('T', Parametr[par_1][1], inp_1,
                                                                          Parametr[par_2][1], inp_2,
                                                                          Sub[page1][0])) - 273.15)) + " °C")
        chek(f)

    st.write("""  """)

    # Энтальпия
    if par_1 == "h - энтальпия, кДж/кг" or par_2 == "h - энтальпия, кДж/кг":
        if par_1 == "h - энтальпия, кДж/кг":
            st.write(""" h = """ + str('{:.6}'.format(inp_1 / 1000)) + " °C")
        if par_2 == "h - энтальпия, кДж/кг":
            st.write(""" h = """ + str('{:.6}'.format(inp_2 / 1000)) + " °C")
    else:
        f = lambda: st.write(""" h = """ + str('{:.6}'.format((CP.PropsSI('H', Parametr[par_1][1], inp_1,
                                                                          Parametr[par_2][1], inp_2,
                                                                          Sub[page1][0])) / 1000)) + " кДж/кг")
        chek(f)

    # Энтропия
    if par_1 == "s - энтропия, кДж/(кг*°C)" or par_2 == "s - энтропия, кДж/(кг*°C)":
        if par_1 == "s - энтропия, кДж/(кг*°C)":
            st.write(""" s = """ + str('{:.6}'.format(inp_1 / 1000)) + " кДж/(кг*°C)")
        if par_2 == "s - энтропия, кДж/(кг*°C)":
            st.write(""" s = """ + str('{:.6}'.format(inp_2 / 1000)) + " кДж/(кг*°C)")
    else:
        f = lambda: st.write(""" s = """ + str('{:.6}'.format((CP.PropsSI('S', Parametr[par_1][1], inp_1,
                                                                          Parametr[par_2][1], inp_2,
                                                                          Sub[page1][0])) / 1000)) + " кДж/(кг*°C)")
        chek(f)

    # Степень сухости
    if par_1 == "x - степень сухости, %" or par_2 == "x - степень сухости, %":
        if par_1 == "x - степень сухости, %":
            st.write(""" x = """ + str('{:.6}'.format(inp_1 * 100)) + " %")
        if par_2 == "x - степень сухости, %":
            st.write(""" x = """ + str('{:.6}'.format(inp_2 * 100)) + " %")
    else:
        try:
            X = ((CP.PropsSI('Q', Parametr[par_1][1], inp_1, Parametr[par_2][1], inp_2, Sub[page1][0])) * 100)
        except:
            X = 0

        if X != - 100:
            f = lambda: st.write(""" x = """ + str('{:.6}'.format((CP.PropsSI('Q', Parametr[par_1][1], inp_1,
                                                                              Parametr[par_2][1], inp_2,
                                                                              Sub[page1][0])) * 100)) + " %")
            chek(f)
        else:
            st.write("Нет значения")
    st.write("""  """)

    # Удельный объем и плотность
    if par_1 == "ρ - плотность, кг/м³" or par_2 == "ρ - плотность, кг/м³":
        if par_1 == "ρ - плотность, кг/м³":
            st.write(""" v  = """ + str('{:.6}'.format(1 / inp_1)) + " м³/кг")
            st.write(""" ρ = """ + str('{:.6}'.format(inp_1)) + " кг/м³")
        if par_2 == "ρ - плотность, кг/м³":
            st.write(""" v  = """ + str('{:.6}'.format(1 / inp_2)) + " м³/кг")
            st.write(""" ρ = """ + str('{:.6}'.format(inp_2)) + " кг/м³")
    else:
        f = lambda: st.write(""" v = """ + str('{:.6}'.format(
            1 / CP.PropsSI('D', Parametr[par_1][1], inp_1, Parametr[par_2][1], inp_2,
                           Sub[page1][0]))) + """ м³/кг""")
        chek(f)
        f = lambda: st.write(""" ρ = """ + str('{:.6}'.format(
            (CP.PropsSI('D', Parametr[par_1][1], inp_1, Parametr[par_2][1], inp_2, Sub[page1][0])))) + " кг/м³")
        chek(f)

    # Внутренняя энергия
    if par_1 == "u - внутренняя энергия, кДж/кг" or par_2 == "u - внутренняя энергия, кДж/кг":
        if par_1 == "u - внутренняя энергия, кДж/кг":
            st.write(""" u = """ + str('{:.6}'.format(inp_1 / 1000)) + " кДж/кг")
        if par_2 == "u - внутренняя энергия, кДж/кг":
            st.write(""" u = """ + str('{:.6}'.format(inp_2 / 1000)) + " кДж/кг")
    else:
        f = lambda: st.write(""" u = """ + str('{:.6}'.format((CP.PropsSI('U', Parametr[par_1][1], inp_1,
                                                                          Parametr[par_2][1], inp_2,
                                                                          Sub[page1][0])) / 1000)) + " кДж/кг")
        chek(f)

    f = lambda: st.write(""" cp = """ + str('{:.6}'.format((CP.PropsSI('C', Parametr[par_1][1], inp_1,
                                                                       Parametr[par_2][1], inp_2,
                                                                       Sub[page1][0])) / 1000)) + " кДж/(кг*°C)")
    chek(f)

    f = lambda: st.write(""" cv = """ + str('{:.6}'.format((CP.PropsSI('O', Parametr[par_1][1], inp_1,
                                                                       Parametr[par_2][1], inp_2,
                                                                       Sub[page1][0])) / 1000)) + " кДж/(кг*°C)")
    chek(f)

    f = lambda: st.write(""" λ = """ + str('{:.6}'.format((CP.PropsSI('conductivity', Parametr[par_1][1], inp_1,
                                                                      Parametr[par_2][1], inp_2,
                                                                      Sub[page1][0])))) + " Вт/(м*°C)")
    chek(f)

    f = lambda: st.write(""" μ = """ + str('{:.6}'.format(
        (CP.PropsSI('viscosity', Parametr[par_1][1], inp_1, Parametr[par_2][1], inp_2, Sub[page1][0])))) + " Па*с")
    chek(f)

    # Кин. вязкость
    if par_1 == "ρ - плотность, кг/м³" or par_2 == "ρ - плотность, кг/м³":
        if par_1 == "ρ - плотность, кг/м³":
            st.write(""" ν  = """ + str('{:.6}'.format((CP.PropsSI('viscosity', Parametr[par_1][1], inp_1,
                                                                   Parametr[par_2][1], inp_2,
                                                                   Sub[page1][0])) / inp_1)) + " м²/с")
        if par_2 == "ρ - плотность, кг/м³":
            st.write(""" ν  = """ + str('{:.6}'.format((CP.PropsSI('viscosity', Parametr[par_1][1], inp_1,
                                                                   Parametr[par_2][1], inp_2,
                                                                   Sub[page1][0])) / inp_2)) + " м²/с")
    else:
        f = lambda: st.write(""" ν = """ + str('{:.6}'.format(
            (CP.PropsSI('viscosity', Parametr[par_1][1], inp_1, Parametr[par_2][1], inp_2, Sub[page1][0])) / (
                CP.PropsSI('D', Parametr[par_1][1], inp_1, Parametr[par_2][1], inp_2, Sub[page1][0])))) + " м²/с")
        chek(f)

    f = lambda: st.write(""" Pr = """ + str('{:.6}'.format(
        (CP.PropsSI('Prandtl', Parametr[par_1][1], inp_1, Parametr[par_2][1], inp_2, Sub[page1][0])))) + " ")
    chek(f)
    st.write("""  """)

    f = lambda: st.write(""" w = """ + str('{:.6}'.format((CP.PropsSI('speed_of_sound', Parametr[par_1][1], inp_1,
                                                                      Parametr[par_2][1], inp_2,
                                                                      Sub[page1][0])))) + " м/с")
    chek(f)

    f = lambda: st.write(""" k = """ + str('{:.6}'.format((CP.PropsSI('isentropic_expansion_coefficient',
                                                                      Parametr[par_1][1], inp_1, Parametr[par_2][1],
                                                                      inp_2, Sub[page1][0])))) + " ")
    chek(f)


# боковое меню
with st.sidebar:
    page1 = st.selectbox("Выберите вещество", Subst)
    tab1, tab2 = st.tabs(["Настройки", " "])
    with tab1:
        st.write(Sub[page1][0])
        st.write("#")
        Vers()
        st.write("Страница проекта на " + "[Github](https://github.com/tederix/WSP)")

Parametr = {'p - давление, МПа': ('Введите давление p, МПа', 'P'),
            't - температура, °C': ('Введите температуру t, °C', 'T'),
            'h - энтальпия, кДж/кг': ('Ведите энтальпию h, кДж/кг', 'H'),
            's - энтропия, кДж/(кг*°C)': ('Ведите энтропию s, кДж/(кг*°C)', 'S'),
            'u - внутренняя энергия, кДж/кг': ('Ведите внутреннюю энергию u, кДж/кг', 'U'),
            'ρ - плотность, кг/м³': ('Ведите плотность ρ, кг/м³', 'D'),
            'x - степень сухости, %': ('Ведите степень сухости, %', 'Q')
            }
Par = list(Parametr.keys())

col1, col2 = st.columns(2)
with col1:
    par_1 = st.selectbox("Выберите 1-ый исходный параметр", Par, index=0, key=1)
    par_2 = st.selectbox("Выберите 2-ой исходный параметр", Par, index=1, key=2)
with col2:
    if par_1 == par_2:
        st.write("##### Выберите два различных параметра")
    else:
        match par_1:
            case "p - давление, МПа":
                inp_1 = st.number_input(Parametr[par_1][0], max_value=(Sub[page1][1]) / 10 ** 6)
                inp_1 = inp_1 * 10 ** 6
            case "t - температура, °C":
                inp_1 = st.number_input(Parametr[par_1][0], max_value=(Sub[page1][2]) - 273.15)
                inp_1 = inp_1 + 273.15
            case "x - степень сухости, %":
                inp_1 = st.number_input(Parametr[par_1][0], max_value=100, min_value=0)
                inp_1 = inp_1 / 100
            case "ρ - плотность, кг/м³":
                inp_1 = st.number_input(Parametr[par_1][0])
            case _:
                inp_1 = st.number_input(Parametr[par_1][0])
                inp_1 = inp_1 * 1000

        match par_2:
            case "p - давление, МПа":
                inp_2 = st.number_input(Parametr[par_2][0], max_value=(Sub[page1][1]) / 10 ** 6)
                int_2 = inp_2 * 10 ** 6
            case "t - температура, °C":
                inp_2 = st.number_input(Parametr[par_2][0], max_value=(Sub[page1][2]) - 273.15)
                inp_2 = inp_2 + 273.15
            case "x - степень сухости, %":
                inp_2 = st.number_input(Parametr[par_2][0], max_value=100, min_value=0)
                inp_2 = inp_2 / 100
            case "ρ - плотность, кг/м³":
                inp_2 = st.number_input(Parametr[par_2][0])
            case _:
                inp_2 = st.number_input(Parametr[par_2][0])
                inp_2 = inp_2 * 1000

if par_1 == par_2:
    st.write("### Выберите два различных параметра")

if par_1 != par_2:
    col1_1, col2_2 = st.columns(2)
    with col1_1:
        Cool(inp_1, inp_2)
    with col2_2:
        with st.expander("Названия свойств", expanded=True):
            text_1()
