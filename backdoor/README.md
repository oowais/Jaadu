# Alien Backdoor

A direct secure command stream between Alien and an admin. Can be used to remotely trigger event-based triggers manually.

To be used for demo purposes (only) or to play God with the Alien (maybe?).

Needs a MQTT broker to be already setup which can relay the commands.

#### Before using

* Make sure you are in the same network as your MQTT Broker, and modify __connect.json__ to point to it.
* `pip3 install -r requirements.txt`

---

### Can anyone now send commands to Alien?

Ofcourse not, that would make it an open field for anyone to mess with the Alien at any point of time.

Credentials need to be setup during the installation phase of the RasPI to allow backdoor functionality.
