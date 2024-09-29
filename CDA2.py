import logging
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

class ConstrainedDeviceApp:
    def __init__(self):
        logging.info("Initializing CDA...")
        self.sysPerfManager = SystemPerformanceManager()

    def startApp(self):
        logging.info("Starting CDA...")
        self.sysPerfManager.startManager()
        logging.info("CDA started.")

    def stopApp(self, code: int):
        logging.info("CDA stopping...")
        self.sysPerfManager.stopManager()
        logging.info("CDA stopped with exit code %s.", str(code))
