# M5-MQTT-Statsd-Receiver
A python program to receive data from MQTT topics and forward them to a Datadog Agent via statsd

### Mosquitto broker headless startup:

```
mosquitto -c /etc/mosquitto/conf.d/default.conf -d
```
        
Can close terminal when mosquitto is started this way

### Python mqtt to statsd startup:

```
sudo systemctl start mqtttest.service
```

Can close terminal after starting, it runs in the background using systemd like the Agent

### Debuging:

Mosquitto client startup:
        
```
mosquitto_sub -u m5receiver -P test4375 -t "value"
```

optional to follow value updates as they come in
