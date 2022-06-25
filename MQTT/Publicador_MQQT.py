
#pip install paho-mqtt
#pip install pandas

#importación de librerias
import pandas as pd
import time
import paho.mqtt.client as mqttClient

#Tratado del archivo excel
dataframe = pd.read_csv("../Sample/DatosPruebaMQTT.csv", index_col=0)
dataframe.head()
dataframe.describe(include="all")
df=dataframe.dropna()

temp = df.Temperature.tolist()
hum = df.Humidity.tolist()
co = df.CO2.tolist()

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

Connected = False # Verificar el estado de la conexión
broker_address = "broker.hivemq.com"
# broker_address = '192.168.0.239'
#puerto por defecto de mqtt
port = 1883
tag1 = "/MNA/IoT/EQ48/temp" # Tag, etiqueta o topico
tag2 = "/MNA/IoT/EQ48/humedad"  # Tag, etiqueta o topico
tag3 = "/MNA/IoT/EQ48/co2"

client = mqttClient.Client("identificador")
client.on_connect = on_connect
client.connect(broker_address, port)
client.loop_start()

while not Connected:
    time.sleep(0.1)
    try:
        for i, j, k in zip(temp, hum, co):
            val1, val2, val3 = '{"Temperature":"' + str(i)+'"}', '{"Humidity":"'+str(j)+'"}', '{"CO2":"'+str(k)+'"}'
            print(tag1, val1, '\n', tag2, val2, '\n', tag3, val3)
            client.publish(tag1, val1, qos=2)
            client.publish(tag2, val2, qos=2)
            client.publish(tag3, val3, qos=2)
            time.sleep(2)
    except KeyboardInterrupt:
        print("User stopped sending data")
        client.disconnect()
        client.loop_stop()
