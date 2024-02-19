import time
import streamlit as st
import paho.mqtt.client as mqtt
import domo.affichage as affichage  # Importer le module hhhh.py
import domo.commande as commande  # Importer le module tt.py

def fn():
    st.set_page_config(layout='wide', initial_sidebar_state='expanded')
    st.markdown('''
        <style>
            [data-testid="stSidebar"] {
                background-image: url(https://scontent.fnbe1-2.fna.fbcdn.net/v/t1.15752-9/426626674_1123871495606251_3132973377989992148_n.png?_nc_cat=111&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=iJdnbkBoJzUAX8hLL9D&_nc_ht=scontent.fnbe1-2.fna&oh=03_AdQllhFQJMtRz6cdI6JFc7VFZCm6--utkOTTnlaDa0ddTA&oe=65EEE446);
                background-size: 240px;
                background-repeat: no-repeat;
                background-position: 5px 25px;
            }
        </style>
    ''', unsafe_allow_html=True)
    
    st.sidebar.header('Tableau de bord')

    # Ajouter les boutons pour sélectionner la page préférée dans la sidebar
    selected_page = st.sidebar.radio("Sélectionner la page préférée", ["affichage", "commande"])

    # Vérifier quelle page a été sélectionnée et afficher son contenu
    if selected_page == "affichage":
        affichage.main()  # Appeler la fonction principale de hhhh.py
    elif selected_page == "commande":
        commande.main2()  # Appeler la fonction principale de tt.py

# Appeler la fonction principale
fn()
