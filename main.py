from prometheus_client import start_http_server
from collector.prometheus_collector import setupRegistry
import time
import logging


if __name__ == '__main__':
    try:
        port = 8000
        # Start up the server to expose the metrics.
        start_http_server(port, registry=setupRegistry())
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt: exit from program")
    except Exception as ex:
        print("Unexpected error occurred, exiting program\n%s", ex)
