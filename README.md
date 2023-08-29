# M5-MQTT-Statsd-Receiver
A python program to receive data from MQTT topics and forward them to a Datadog Agent via statsd

When adding a room, make sure it is preceded by a space. This is used in the python program to split it from the temperature. 

### Debuging:

Mosquitto client startup:
        
```
mosquitto_sub -t "temp"
```

optional to follow value updates as they come in
