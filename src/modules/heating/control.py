import mqtt
from . import storage, websockets as ws

def heating_on():
    mqtt.publish("flat/heating/hallway/chState", "on")
    storage.set("ch_is_on", True)

    ws.push_state()


def heating_off():
    mqtt.publish("flat/heating/hallway/chState", "off")
    storage.set("ch_is_on", False)

    ws.push_state()

def handle_temperature(topic, message):
    global temperature
    temperature = float(message)
    storage.set("temperature", temperature)

    ws.get_instance().publish("temperature", {
        "latest_reading": temperature
    })

def initialise(module_id):
    mqtt.subscribe("flat/heating/hallway/temperature", handle_temperature)