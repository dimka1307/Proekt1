import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 60)
    client.publish('Proekt/sharzeri', payload="Sharzerot 5 e prazen", qos=2, retain=True)

if __name__ == "__main__":
    main()