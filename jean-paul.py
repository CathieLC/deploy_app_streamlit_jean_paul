import streamlit as st
import pandas as pd
import numpy as np







def main():

    pages = {
        'Accueil': Accueil,
        'Obtenir une estimation' : estimation_volume
        #'Base de données': base_de_donnees,
        
        }

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Accueil'
        })



    with st.sidebar:
        st.image('assets/demenagement.png', width=300)
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
        st.image('assets/demenagement.png', width=300)
    




def estimation_volume():

    #graphs centrés
    config = {'displayModeBar': False}

    with open('p2.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)


    link = 'bdd/items.csv'
    df_items = pd.read_csv(link)



    #now code the plotly chart based on the widget selection
    item = df_items['item'].unique()
    line = st.selectbox("choisis l'item",item)
    loc = df_items.loc[df_items['item'] == line]

    def load_data():

        return pd.DataFrame(
            {
                "item": [line],
                "volume calculé": loc['volume (m3)'],
            }
        )


    df_display = load_data()

    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    st.dataframe(df_display)

   

if __name__ == "__main__":
    main()






