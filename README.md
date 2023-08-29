# M5-MQTT-Statsd-Receiver
A python program to receive data from MQTT topics and forward them to a Datadog Agent via statsd. This expects that a Datadog Agent is running on the server you run mosquitto and the python code on. 

When adding a room, make sure it is preceded by a space. This is used in the python program to split it from the temperature. 

### Debuging:

Mosquitto client startup:
        
```
mosquitto_sub -t "temp"
```

optional to follow value updates as they come in
