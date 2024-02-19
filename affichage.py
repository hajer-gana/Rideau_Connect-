import time
import streamlit as st
import paho.mqtt.client as mqtt

message_light="1000"
message_motion="Motion detected!"
message_servo="0"


# Définir la fonction de rappel pour la réception des messages

def on_message(client, userdata, msg):
    global message_light
    global message_motion
    global message_servo
    # Utiliser global pour modifier la variable globale
    if msg.topic == "light":
        message_light = (msg.payload.decode())
        print(message_light)
        client.disconnect()
        time.sleep(2)
    if msg.topic == "motion":
        message_motion = (msg.payload.decode())
        print(message_motion)
        client.disconnect()
        time.sleep(2)
    if msg.topic == "servo_position":
        message_servo = (msg.payload.decode())
        print(message_servo)
        client.disconnect()
        time.sleep(2)
      
    

        

#if "message_light" in st.session_state:
  #  st.session_state.message_light = "55"

# Créer un client MQTT
subscribe_client = mqtt.Client()



def main():
   

    # Row A
    subscribe_client.loop_forever() # Start the MQTT loop
    st.markdown('<h3 style="color: #cc0000;">Affichage</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.markdown('### Luminosité')
    col1.write(message_light)
    
    col2.markdown('### Presence')
    col2.write(message_motion)

    col3.markdown('### État actuel de rideau')
    col3.write(message_servo)
    
    time.sleep(2)
    st.rerun()
    
    

subscribe_client.on_message = on_message           # Connexion au broker MQTT et souscription aux topics
subscribe_client.connect("broker.hivemq.com", 1883, 60)
subscribe_client.subscribe("light")
subscribe_client.subscribe("cmd")
subscribe_client.subscribe("motion")
subscribe_client.subscribe("servo_position")
subscribe_client.subscribe("Alarm")
subscribe_client.loop_forever() # Start the MQTT loop
main()
time.sleep(2)



        
        
        
