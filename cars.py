import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px







def main():

    pages = {
        'Accueil': Accueil,
        'Première analyse': premiere_analyse,
        'Les différentes corrélations': best_corr,
        'Résultats par région' : region_results,
        }

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Accueil'
        })



    with st.sidebar:
        st.image('hot_wheels.png', width=300)
        page = st.selectbox("Choose a page", tuple(pages.keys()))


    pages[page]()


def Accueil():

    st.write('\n')
    st.write('\n')
    st.write('\n')

    def _max_width_():
        max_width_str = "max-width: 1300px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()

           
    with open('p1_accueil.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)

    st.write('\n')
    st.write('\n')
    st.write('\n')

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('old_car.png', width=300)
    
      
    

def premiere_analyse():



    def _max_width_():
        max_width_str = "max-width: 800px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('data_analysis.png', width=200)
    
    
    #texte explicatif en html    
    with open('p2_première analyse.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)
    
            
    st.write('\n')
    st.write('\n')
    st.write('\n')

    link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
    df_cars = pd.read_csv(link)

    df_corr = df_cars.corr()

    #taille heatmap
    fig, ax = plt.subplots(figsize=(11, 9))
    
    #style
    ax = sns.set_theme(style="whitegrid")
    
    # heatmap
    ax = sns.heatmap(df_corr,                    
                                            
                        cmap=sns.cubehelix_palette(as_cmap=True),                  
                        vmax=.3,
                        mask=np.triu(np.ones_like(df_corr, dtype=bool)),                        
                        center=0,                   
                        square=True,                
                        linewidths=5,               
                        cbar_kws={"shrink": .6},                                
                        linecolor='white',
                        )

    fig = plt.title('Corrélation between characteristics of cars', size = 18)

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

    #seconde analyse
    with open('p2_Seconde_analyse.html','r',encoding='UTF-8') as file :
        data2 = file.read()

    st.markdown(data2, unsafe_allow_html=True)

    #insertion du df : df_cars.cor()
    st.dataframe(df_corr)



def best_corr():

    #graphs centrés
    config = {'displayModeBar': False}


    #utilisation de la largeur de la page
    def _max_width_():
        max_width_str = "max-width: 800px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()



    link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
    df_cars = pd.read_csv(link)
    df_cars.rename(columns={"mpg": "Miles per gallon_(mpg)","cylinders": "Cylinders", "cubicinches": "Cubic_Inches","hp" : "Horse_Power", "weightlbs": "Weight_Lbs",  "time-to-60" : "Time_to_60" , "year" : "Year", "continent" : "Continent"}, inplace=True)


    #commentaire graph 1 et accueil page
    with open('p3_diff_corr.html','r',encoding='UTF-8') as file :
        data3 = file.read()

    st.markdown(data3, unsafe_allow_html=True)


    # graph 1
    # distance parcourue par gallon consommée - Plus la voiture est lourde, moins elle fait de miles
    fig = plt.figure(figsize=(12, 9))

    fig = px.scatter(data_frame = df_cars,
                    y= "Miles per gallon_(mpg)", x="Weight_Lbs",
                    color="Continent",
                    )

    fig.update_layout(title ="<b>Distance parcourue en fonction du poids des véhicules<b>",
                    title_x = 0.5,
                    dragmode='select',
                    width=1300,
                    height=700,
                    hovermode='closest',
                    template='plotly_dark')


    st.plotly_chart(fig, config = config, use_container_width = True)



    #commentaire graph 2
    with open('p3_resum_graph2.html','r',encoding='UTF-8') as file :
        data4 = file.read()

    st.markdown(data4, unsafe_allow_html=True)   




    # graph 2
    fig2 = go.Figure() 

    df = df_cars.sort_values(by="Horse_Power")

    fig2 = plt.figure(figsize=(15, 9))

    fig2 = px.scatter(data_frame = df, x= "Horse_Power", y="Time_to_60", color="Horse_Power")

    fig2.update_layout(title ="<b>Temps pour atteindre les 60m/h en fonction de la puissance du véhicule<b>",
                    title_x = 0.5,
                    dragmode='select',
                    width=1300,
                    height=600,
                    hovermode='closest',
                    template='none',
                    xaxis_title='Puissance fiscale',
                    yaxis_title='Temps pour atteindre 60m/h (secondes)')
    
    
    st.plotly_chart(fig2, use_container_width = True)



def region_results():

    #graphs centrés
    config = {'displayModeBar': False}

    with open('p4_Intro_selection_region.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)


    link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
    df_cars = pd.read_csv(link)
    df_cars.rename(columns={"mpg": "Miles per gallon_(mpg)","cylinders": "Cylinders", "cubicinches": "Cubic_Inches","hp" : "Horse_Power", "weightlbs": "Weight_Lbs",  "time-to-60" : "Time_to_60" , "year" : "Year", "continent" : "Continent"}, inplace=True)



    #now code the plotly chart based on the widget selection
    item = df_cars['Continent'].unique()
    line = st.selectbox("choisis le continent",item)
    
    fig = px.scatter(data_frame = (df_cars[df_cars['Continent'] == line]),
                    x="Weight_Lbs",
                    y= "Miles per gallon_(mpg)",
                    size="Weight_Lbs",
                    color="Weight_Lbs")

    
    fig.update_layout(title ="<b>Distance parcourue en fonction du poids des véhicules<b>",
                    title_x = 0.5,
                    dragmode='select',
                    width=1300,
                    height=700,
                    hovermode='closest',
                    template='plotly_dark')

    st.plotly_chart(fig, use_container_width = True)

     
    
    fig2 = px.bar(data_frame = (df_cars[df_cars['Continent'] == line]),
                    x="Year",
                    y= "Horse_Power",
                    color_discrete_sequence=['mediumspringgreen'],
                    )

    
    fig2.update_layout(title ="<b>Variation de la puissance des véhicules dans le temps<b>",
                    title_x = 0.5,
                    dragmode='select',
                    width=1300,
                    height=700,
                    
                    template='none')

    st.plotly_chart(fig2, use_container_width = True)
   

if __name__ == "__main__":
    main()






