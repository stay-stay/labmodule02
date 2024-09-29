# BaseSystemUtilTask.py

import logging

class BaseSystemUtilTask:
    def __init__(self, name: str, typeID: int):
        self.name = name
        self.typeID = typeID
        logging.info("BaseSystemUtilTask initialized with name: %s and typeID: %d", self.name, self.typeID)

    def getTelemetryValue(self) -> float:
        raise NotImplementedError("Subclasses must implement this method.")


# SystemCpuUtilTask.py

import logging
import psutil
import programmingtheiot.common.ConfigConst as ConfigConst

class SystemCpuUtilTask(BaseSystemUtilTask):
    def __init__(self):
        super(SystemCpuUtilTask, self).__init__(name=ConfigConst.CPU_UTIL_NAME, typeID=ConfigConst.CPU_UTIL_TYPE)

    def getTelemetryValue(self) -> float:
        return psutil.cpu_percent()


# SystemMemUtilTask.py

import logging
import psutil
import programmingtheiot.common.ConfigConst as ConfigConst

class SystemMemUtilTask(BaseSystemUtilTask):
    def __init__(self):
        super(SystemMemUtilTask, self).__init__(name=ConfigConst.MEM_UTIL_NAME, typeID=ConfigConst.MEM_UTIL_TYPE)

    def getTelemetryValue(self) -> float:
        return psutil.virtual_memory().percent


# SystemPerformanceManager.py

import logging
from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask

class SystemPerformanceManager:
    def __init__(self):
        logging.info("Initializing SystemPerformanceManager...")
        self.cpuTask = SystemCpuUtilTask()
        self.memTask = SystemMemUtilTask()

    def startMonitoring(self):
        logging.info("Starting system performance monitoring...")
        # Here you can start monitoring logic, like setting up threads or loops.

    def stopMonitoring(self):
        logging.info("Stopping system performance monitoring...")
        # Here you can stop monitoring logic.

    def getCpuUtilization(self) -> float:
        return self.cpuTask.getTelemetryValue()

    def getMemoryUtilization(self) -> float:
        return self.memTask.getTelemetryValue()
