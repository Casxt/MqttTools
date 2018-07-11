import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("TEST")
        
def on_publish(client, userdata, mid):
    print(mid)
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("sh2.casxt.com", 1883, 60)

count = 0
while True:
    count += 1
    client.publish("TEST","TESTMsg"+str(count))
    #client.loop()
    time.sleep(1)