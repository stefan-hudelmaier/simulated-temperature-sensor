import time
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import json
import random
import os
import sys

connection_string = sys.argv[1] if len(sys.argv) > 1 else os.getenv("DEVICE_CONNECTION_STRING")
if connection_string is None:
    print("The device connection string must either be passed as the first parameter or as the DEVICE_CONNECTION_STRING env variable")
    sys.exit(1)

print("Using connection string", connection_string)

send_interval = 3


def main():

    def updateTwin():
        configuration_settings = {
            'transferInterval': send_interval
        }
        print("Updating device twin", configuration_settings)
        device_client.patch_twin_reported_properties(configuration_settings)

    def method_request_handler(method_request):
        print("Method received:", method_request.name)
        status = 200
        payload = {"result": True, "version": 1}
        global send_interval
        send_interval = int(method_request.payload)
        updateTwin()
        method_response = MethodResponse.create_from_method_request(method_request, status, payload)
        device_client.send_method_response(method_response)

    device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

    device_client.connect()

    device_client.on_method_request_received = method_request_handler

    updateTwin()

    while True:

        normal_telemetry_msg = json.dumps({
            'temperature': random.random() * 40.0})
        print("Sending telemetry:", normal_telemetry_msg)
        device_client.send_message(normal_telemetry_msg)

        print(f"Waiting for {send_interval} seconds")
        time.sleep(send_interval)

    device_client.disconnect()


if __name__ == '__main__':
    main()
