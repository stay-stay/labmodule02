import logging
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager
import ConfigConst


class SystemPerformanceManager:
    def __init__(self, name: str = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE):
        self.name = name
        self.typeID = typeID

        logging.info("Initializing SystemPerformanceManager with name: %s and typeID: %d", self.name, self.typeID)

    def getName(self) -> str:
        return self.name

    def getTypeID(self) -> int:
        return self.typeID

    def getTelemetryValue(self) -> float:
        pass  # Placeholder for future implementation
