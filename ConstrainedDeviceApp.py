# ConstrainedDeviceApp.py
#Stavia Allwood

import logging
from time import sleep #import the sleep function

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ConstrainedDeviceApp:
    def __init__(self):
        # Initialization code
        pass

    def startApp(self):
        logging.info("App has been started.")

    def stopApp(self):
        logging.info("App has been stopped.")

    def some_method(self):
        # Example method
        print("This is a method in the ConstrainedDeviceApp class.")


def main():
    cda =ConstrainedDeviceApp()
    cda.startApp()

    sleep(65) # Wait for 65 seconds

    cda.stopApp()


if __name__ == "__main__":
   main()

