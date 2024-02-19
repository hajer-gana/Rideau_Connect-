import time
import streamlit as st
import paho.mqtt.client as mqtt
def publish_message(client, topic, message):
    client.publish(topic, message)
subscribe_client = mqtt.Client()
subscribe_client.connect("broker.hivemq.com", 1883, 60)
subscribe_client.connect("broker.hivemq.com", 1883, 60)
subscribe_client.subscribe("light")
subscribe_client.subscribe("cmd")
subscribe_client.subscribe("motion")
subscribe_client.subscribe("servo_position")
subscribe_client.subscribe("Alarm")
def main2():
    subscribe_client.loop_start()
    st.markdown('<h3 style="color: #cc0000;">Mode</h3>', unsafe_allow_html=True)
    curtain_action = st.radio("Choisissez le mode", ["auto", "manuel"],index=None)
    if curtain_action == "auto":
        publish_message(subscribe_client, "cmd", "auto")
    elif curtain_action == "manuel":
        publish_message(subscribe_client, "cmd", "manuel")
    # st.markdown('<h3 style="color:#5d5d5d;">Commande manuelle du rideau</h3>', unsafe_allow_html=True)
    st.markdown('### Commande manuelle du rideau')

    if st.button('Ouvrir le rideau'):
        publish_message(subscribe_client, "cmd", "servo_open")
        st.write(f"Commande pour ouvrir le rideau envoyée.")

    if st.button('Fermer le rideau'):
        publish_message(subscribe_client, "cmd", "servo_close")
        st.write(f"Commande pour fermer le rideau envoyée.")

    st.markdown('### Réglage du temps')
    selected_hours = st.number_input("Sélectionnez les heures", min_value=0, max_value=23, step=1, value=12)
    selected_minutes = st.number_input("Sélectionnez les minutes", min_value=0, max_value=59, step=5, value=0)

    curtain_action = st.radio("Choisissez l'action pour le rideau", ["Ouvrir", "Fermer"],index=None)
    if curtain_action == "Ouvrir":
        aff = f"{selected_hours:02d}:{selected_minutes:02d} Ouvrir"
        publish_message(subscribe_client, "alarm",aff)
        st.write(f"Temps d'ouverture de rideau : {selected_hours:02d}:{selected_minutes:02d}")
    elif curtain_action == "Fermer":
        affi = f"{selected_hours:02d}:{selected_minutes:02d} Fermer"
        publish_message(subscribe_client,"alarm",affi)
        st.write(f"Temps de fermeture de rideau : {selected_hours:02d}:{selected_minutes:02d}")
    subscribe_client.loop_stop()

