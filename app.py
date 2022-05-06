import pandas as pd  
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="GIP Dashboard", 
    page_icon=":bar_chart:", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"}
    )

# ---- READ EXCEL ACTIVA ----
@st.cache
def get_activa_from_excel():
    df = pd.read_excel(
        io="data/Jules Destrooper oplossing.xlsx",
        engine="openpyxl",
        sheet_name="verticale analyse balans",
        usecols="A:E",
        nrows=100,
        header=2
    )

    # filter row on column value
    activa = ["VASTE ACTIVA","VLOTTENDE ACTIVA"]
    df = df[df['ACTIVA'].isin(activa)]

    return df

df_activa = get_activa_from_excel()

# ---- READ EXCEL PASIVA ----
@st.cache
def get_passiva_from_excel():
    df = pd.read_excel(
        io="data/Jules Destrooper oplossing.xlsx",
        engine="openpyxl",
        sheet_name="verticale analyse balans",
        usecols="A:E",
        nrows=100,
        header=50
    )

    # filter row on column value
    passiva = ["EIGEN VERMOGEN","VOORZIENINGEN EN UITGESTELDE BELASTINGEN","SCHULDEN"]
    df = df[df['PASSIVA'].isin(passiva)]

    return df

df_passiva = get_passiva_from_excel()


# ---- SIDEBAR ----
st.sidebar.header("Gelieve hier te filteren:")
boekjaar = st.sidebar.radio(
    "Selecteer boekjaar:",
    ("Boekjaar 1","Boekjaar 2","Boekjaar 3"),
    index=0
)

# ---- MAINPAGE ----
st.title(":bar_chart: Jaarrekening Dashboard")
st.markdown("##")

# Samenstelling activa boekjaar [TAART DIAGRAM]
fig_activa = px.pie(df_activa, 
            values=boekjaar, 
            names='ACTIVA',
            title=f'Samenstelling activa {boekjaar}'            
            )
fig_activa.update_traces(textfont_size=20, pull=[0, 0.2], marker=dict(line=dict(color='#000000', width=2)))
fig_activa.update_layout(legend = dict(font = dict(size = 20)), title = dict(font = dict(size = 30)))

# Samenstelling pasiva boekjaar [TAART DIAGRAM]
fig_passiva = px.pie(df_passiva, 
            values=boekjaar, 
            names='PASSIVA',
            title= f'Samenstelling passiva {boekjaar}'            
            )
fig_passiva.update_traces(textfont_size=20, pull=[0, 0.2], marker=dict(line=dict(color='#000000', width=2)))
fig_passiva.update_layout(legend = dict(font = dict(size = 20)), title = dict(font = dict(size = 30)))


##test
#
#
col1, col2 = st.columns([1,1])
with col1:
    st.write(df_activa)
with col2:
    st.write(df_passiva)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_activa, use_container_width=True)
right_column.plotly_chart(fig_passiva, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)