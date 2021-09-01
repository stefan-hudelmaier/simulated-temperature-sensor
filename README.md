A simple simulator of a temperature sensor that sends values to Azure IoT Hub

# Running via Docker

```
docker run --rm -ti \
  -e DEVICE_CONNECTION_STRING="HostName=ux4iot-iothub-e5ucf6glooqfi.azure-devices.net;DeviceId=simulated-device;SharedAccessKey=xxx" \
  ghcr.io/stefan-hudelmaier/simulated-temperature-sensor:main
```

`DEVICE_CONNECTION_STRING` is the connection string of your Azure IoT Hub Device

# Running locally

Init venv

```
virtualenv venv
source venv/bin/activate
```

```
pip3 install -r requirements.txt
python3 main.py
```

Exit venv:

```
deactivate
```
