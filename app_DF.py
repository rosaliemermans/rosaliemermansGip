#modules
import pandas as pd  
import plotly.express as px
import streamlit as st
#start 
st.set_page_config(
    page_title="GIP Dashboard", 
    page_icon=":bar_chart:", 
    layout="wide",
    initial_sidebar_state="expanded",
    )

# ---- READ EXCEL Liquiditeit ----
@st.cache
def get_Liquiditeit_from_excel():
    df = pd.read_excel(
        io="data/GIP.xlsx",
        engine="openpyxl",
        sheet_name="Liquiditeit",
        usecols="A:D",
        nrows=40,
        skiprows=1
    )

    # add column
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    Liquiditeit = ["Liquiditeit in ruime zin", "Liquiditeit in enge zin"]
    df = df[df['Type'].isin(Liquiditeit)]
    df = df.T
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2","Boekjaar 3":"3"})

    df = df.iloc[1: , :]
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2","Boekjaar 3"],True)
    df.columns = ["Boekjaar","Liquiditeit in ruime zin","Liquiditeit in enge zin"]


    return df

df_Liquiditeit = get_Liquiditeit_from_excel()
# ---- READ EXCEL KlantLevKrediet ----
@st.cache
def get_KlantLevKrediet_from_excel():
    df = pd.read_excel(
        io="data/GIP.xlsx",
        engine="openpyxl",
        sheet_name="KlantLevKrediet",
        usecols="A:D",
        nrows=40,
    )

    # add column
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    KlantLevKrediet = ["Klantenkrediet", "Leverancierskrediet "]
    df = df[df['Type'].isin(KlantLevKrediet)]
    df = df.T
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2","Boekjaar 3":"3"})

    df = df.iloc[1: , :]
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2","Boekjaar 3"],True)
    df.columns = ["Boekjaar","Klantenkrediet","Leverancierskrediet"]


    return df

df_KlantLevKrediet = get_KlantLevKrediet_from_excel()

# ---- READ EXCEL Solvabiliteit  ----
@st.cache
def get_Solvabiliteit_from_excel():
    df = pd.read_excel(
        io="data/GIP.xlsx",
        engine="openpyxl",
        sheet_name="Solvabiliteit",
        usecols="A:D",
        nrows=40,
        skiprows=1
       
        
    )

    # add column
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    Solvabiliteit = ["Solvabiliteit"]
    df = df[df['Type'].isin(Solvabiliteit)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Solvabiliteit"] # change column names
    df = df.astype({'Boekjaar':'string','Solvabiliteit':'float64'})

    return df

df_Solvabiliteit= get_Solvabiliteit_from_excel()

# ---- READ EXCEL REV ----
@st.cache
def get_REV_from_excel():
    df = pd.read_excel(
        io="data/GIP.xlsx",
        engine="openpyxl",
        sheet_name="REV",
        usecols="A:D",
        nrows=20,
        skiprows=1
    )

    # add column
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    
    REV = ["REV"]
    df = df[df['Type'].isin(REV)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","REV"] # change column names
    



    return df

df_REV = get_REV_from_excel()

# ---- READ EXCEL Voorraad ----
@st.cache
def get_Voorraad_from_excel():
    df = pd.read_excel(
        io="data/GIP.xlsx",
        engine="openpyxl",
        sheet_name="Voorraad",
        usecols="A:D",
        nrows=4,
        skiprows=0
    )

    # add column
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    Voorraad = ["Omlooptijd", "Omloopsnelheid voorraden"]
    df = df[df['Type'].isin(Voorraad)]
    df = df.T
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2","Boekjaar 3":"3"})

    df = df.iloc[1: , :]
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2","Boekjaar 3"],True)
    df.columns = ["Boekjaar","Omlooptijd","Omloopsnelheid voorraden"]


    return df

df_Voorraad = get_Voorraad_from_excel()
df = df.round({"klantenkrediet":2})
# ---- MAINPAGE ----
st.title(":bar_chart: Jaarrekening Dashboard Agora Group")
st.markdown("##")


#----Sidebar----
st.sidebar.image ("LOGO.jpg")
st.sidebar.header("gelieve te filteren")
grafiek = st.sidebar.selectbox(
    "Selecteer ratio",
    ("homepage","Liquiditeit", "Solvabiliteit", "KlantLevKrediet", "Voorraad", "REV"),
    index = 0
)
st.sidebar.image ("bloemen.jpg")


#start 

#fotos 
if grafiek == "homepage": 
    st.header ("homepage")
    st.image ("LOGO.jpg")

#grafiek Liquiditeit
    
elif grafiek == "Liquiditeit":
    
    st.write(df_Liquiditeit)
    fig = px.line(df_Liquiditeit, x="Boekjaar", y=["Liquiditeit in ruime zin", "Liquiditeit in enge zin"], markers=True)
    fig.update_layout({
          'plot_bgcolor': 'rgba(0,0,0,0)',
             'paper_bgcolor': 'rgba(0,0,0,0)',})
    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True )

    liq = st.sidebar.selectbox(
        "Selecteer soort Liquiditeit ",
        ("Liquiditeit in ruime zin","Liquiditeit in enge zin"),
        index = 0
        )  
    if liq == "Liquiditeit in ruime zin":
        st.header("Liquiditeit in ruime zin")
        st.write(df_Liquiditeit)
        fig = px.line(df_Liquiditeit, x="Boekjaar", y=["Liquiditeit in ruime zin"], markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
             'paper_bgcolor': 'rgba(0,0,0,0)',})
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True )

    else :
        st.header("Liquiditeit in enge zin")
        st.write(df_Liquiditeit)
        fig = px.line(df_Liquiditeit, x="Boekjaar", y=["Liquiditeit in enge zin"], markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
             'paper_bgcolor': 'rgba(0,0,0,0)',})
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True )

#grafiek KlantLevKrediet
elif grafiek == "KlantLevKrediet":
    st.header("KlantLevKrediet")
    st.write(df_KlantLevKrediet)
    fig = px.line(df_KlantLevKrediet, x="Boekjaar", y=["Klantenkrediet", "Leverancierskrediet"], markers=True)
    fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',})
    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True )
    KenL = st.sidebar.selectbox(
        "Selecteer soort klantlevkrediet ",
        ("Klantenkrediet","Leverancierskrediet"),
        index = 0
        )  
    if KenL == "Klantenkrediet":
        st.header("Klantenkrediet")
        st.write(df_KlantLevKrediet)
        fig = px.line(df_KlantLevKrediet, x="Boekjaar", y=["Klantenkrediet"], markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
             'paper_bgcolor': 'rgba(0,0,0,0)',})
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True )
    else :
        st.header("Leverancierskrediet")
        st.write(df_KlantLevKrediet)
        fig = px.line(df_KlantLevKrediet, x="Boekjaar", y=["Leverancierskrediet"], markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
             'paper_bgcolor': 'rgba(0,0,0,0)',})
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True )

#grafiek Solvabiliteit 
elif grafiek == "Solvabiliteit":
    st.header("Solvabiliteit")
    st.write(df_Solvabiliteit)
    fig = px.bar(df_Solvabiliteit, y="Solvabiliteit", x="Boekjaar",barmode="group")
    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)',
       'paper_bgcolor': 'rgba(0,0,0,0)',})
    #fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True )

#grafiek REV 
elif grafiek == "REV":
    st.header("REV")
    st.write(df_REV)
    fig = px.bar(df_REV, x="REV", y="Boekjaar")
    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',})
    #fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True )

#grafiek voorraad
else: 
    st.header("Voorraad")
    st.write(df_Voorraad)
    fig = px.bar(df_Voorraad, x=['Omlooptijd','Omloopsnelheid voorraden'], y="Boekjaar")
    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',})
    #fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True )
    Voor = st.sidebar.selectbox(
        "Selecteer soort Voorraad ",
        ("Omlooptijd","Omloopsnelheid voorraden"),
        index = 0
        )  
    if Voor == "Omlooptijd":
        st.header("Omlooptijd")
        st.write(df_Voorraad)
        fig = px.line(df_Voorraad, x="Boekjaar", y=["Omlooptijd"], markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
             'paper_bgcolor': 'rgba(0,0,0,0)',})
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True )

    else :
        st.header("Omloopsnelheid voorraden")
        st.write(df_Voorraad)
        fig = px.line(df_Voorraad, x="Boekjaar", y=["Omloopsnelheid voorraden"], markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
             'paper_bgcolor': 'rgba(0,0,0,0)',})
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True )

