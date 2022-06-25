import time
import paho.mqtt.client as mqttClient

#IoT_Python
def on_connect(client, userdata, flags, rc):
    """ Función que establece la conexión"""
    #Codigo de retorno
    if rc == 0:
        print("Conectado al broker")
        #No hacer mala practica
        global Connected
        Connected = True
    else:
        print("Falla de la conexión")
    return

def on_message(client, userdata, message):
    """Función que recibe los mensajes del broker"""
    print("Mensaje - {}: {}".format(message.topic, message.payload))
    return


Connected = False  # Verificar el estado de la conexión
broker_address = "broker.hivemq.com"
port = 1883  # puerto por defecto de mqtt
tag = "/MNA/IoT/EQ48/#"  # Tag, etiqueta o topico


client1 = mqttClient.Client("cliente")  # instanciación
client1.on_connect = on_connect  # Agregando la función
client1.on_message = on_message  # Agregando la función
client1.connect(broker_address, port)
client1.loop_start()  # inicia la instancia

while Connected != True:
    time.sleep(0.1)
    client1.subscribe(tag)
    try:
        while  True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Envio de datos detenido por el usuario")
        client1.disconnect()
        client1.loop_stop()
