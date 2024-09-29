# system_performance_manager.py

import logging
import psutil
import programmingtheiot.common.ConfigConst as ConfigConst

# Base class for system utility tasks
class BaseSystemUtilTask:
    def __init__(self, name: str, typeID: int):
        self.name = name
        self.typeID = typeID
        logging.info("BaseSystemUtilTask initialized with name: %s and typeID: %d", self.name, self.typeID)

    def getTelemetryValue(self) -> float:
        raise NotImplementedError("Subclasses must implement this method.")

# Class for CPU utilization
class SystemCpuUtilTask(BaseSystemUtilTask):
    def __init__(self):
        super(SystemCpuUtilTask, self).__init__(name=ConfigConst.CPU_UTIL_NAME, typeID=ConfigConst.CPU_UTIL_TYPE)

    def getTelemetryValue(self) -> float:
        return psutil.cpu_percent()

# Class for memory utilization
class SystemMemUtilTask(BaseSystemUtilTask):
    def __init__(self):
        super(SystemMemUtilTask, self).__init__(name=ConfigConst.MEM_UTIL_NAME, typeID=ConfigConst.MEM_UTIL_TYPE)

    def getTelemetryValue(self) -> float:
        return psutil.virtual_memory().percent

# Manager class for system performance tasks
class SystemPerformanceManager:
    def __init__(self):
        logging.info("Initializing SystemPerformanceManager...")
        self.cpuTask = SystemCpuUtilTask()
        self.memTask = SystemMemUtilTask()

    def startMonitoring(self):
        logging.info("Starting system performance monitoring...")
        # Logic to start monitoring tasks (could be threads or timers)

    def stopMonitoring(self):
        logging.info("Stopping system performance monitoring...")
        # Logic to stop monitoring tasks

    def getCpuUtilization(self) -> float:
        return self.cpuTask.getTelemetryValue()

    def getMemoryUtilization(self) -> float:
        return self.memTask.getTelemetryValue()

# Main application class
class GDAApplication:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.performanceManager = SystemPerformanceManager()

    def start(self):
        logging.info("Starting GDA Application...")
        self.performanceManager.startMonitoring()

    def stop(self):
        logging.info("Stopping GDA Application...")
        self.performanceManager.stopMonitoring()

# Entry point for the application
if __name__ == '__main__':
    app = GDAApplication()
    app.start()
    # Simulating a running application
    try:
        while True:
            cpu_usage = app.performanceManager.getCpuUtilization()
            mem_usage = app.performanceManager.getMemoryUtilization()
            logging.info("CPU Usage: %s%%, Memory Usage: %s%%", cpu_usage, mem_usage)
    except KeyboardInterrupt:
        app.stop()
