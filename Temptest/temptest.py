#templog = open('c:\\Users\\ccrai\\Downloads\\Finalproj\\Temps2\\OpenHardwareMonitor\\OpenHardwareMonitorLog-2021-02-26.csv', 'r')
import wmi
import subprocess

datalist = []
def HardwareMonitorOpen():
    return subprocess.Popen(['c:\\Users\\ccrai\\Downloads\\Finalproj\\Temps\\OpenHardwareMonitor\\OpenHardwareMonitor.exe'])

if __name__ == '__main__':
    HardwareMonitorOpen()
    sensors = wmi.WMI(namespace='root\OpenHardwareMonitor')

    while(True):
        for sensor in sensors.Sensor():
            #print("{} {}: {}".format(sensor.Name, sensor.SensorType, sensor.Value))
            formattedname = (sensor.Name + ' ' + sensor.SensorType)
            datatuple = (formattedname, sensor.Value)
            datalist.append(datatuple)
            #print(datalist)
            if 'Temperature' in datatuple[0]:
                if 'CPU' in datatuple[0]:
                    print('CPU Temperature: ' + str(datatuple[1]))
                elif 'GPU' in datatuple[0]:
                    print('GPU Temperature: ' + str(datatuple[1]))