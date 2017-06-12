import paho.mqtt.client as mqtt
import time

def on_connect(mqttc, userdata, rc):
    print('connected...rc=' + str(rc))
   
    #Resgitration
    mqttc.subscribe(topic='device/3333', qos=0)
    

def on_disconnect(mqttc, userdata, rc):
    print('disconnected...rc=' + str(rc))

def on_message(mqttc, userdata, msg):
    print('message received...')
    print('topic: ' + msg.topic + ', qos: ' + str(msg.qos) + ', message: ' + str(msg.payload))

def on_publish(mqttc, userdata, mid):
    print('message published')
    #mqttc.disconnect()

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.connect(host='localhost', port=1883)
while(1):    
    mqttc.loop_start() 	
    #time.sleep(2)
    mqttc.loop_stop()
    inp1= raw_input("Enter id of Reciver: ") 
    inp= raw_input("Msg: ")
    mqttc.loop_start()
    mqttc.publish(topic='device/abcd', payload=inp1+inp, qos=0)
    mqttc.loop_stop()	
    #time.sleep(2)
