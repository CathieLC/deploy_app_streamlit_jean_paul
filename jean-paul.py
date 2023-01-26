import streamlit as st
#import pandas as pd
#import numpy as np







def main():

    pages = {
        'Accueil': Accueil,
        #'Base de données': base_de_donnees,
        
        }

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Accueil'
        })



    with st.sidebar:
        st.image('assets/artidem.png', width=300)
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
        st.image('assets/artidem.png', width=300)
    
      
   

if __name__ == "__main__":
    main()






