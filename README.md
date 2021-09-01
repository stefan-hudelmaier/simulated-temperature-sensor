A simple simulator of a temperature sensor that sends values to Azure IoT Hub

# Running via Docker

```
docker run --rm -ti \
  -e DEVICE_CONNECTION_STRING="HostName=myiothub.azure-devices.net;DeviceId=dev1;SharedAccessKey=xxx" \
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
