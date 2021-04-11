from kivy.app import App
from kivy.uix.widget import Widget
import wmi
import subprocess

datalist = []
def HardwareMonitorOpen():
    return subprocess.Popen(['c:\\Users\\ccrai\\Downloads\\Finalproj\\Temps\\OpenHardwareMonitor\\OpenHardwareMonitor.exe']) 

class PongGame(Widget):
    pass

class PongTwoApp(App):
    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongTwoApp().run()
    HardwareMonitorOpen()
    sensors = wmi.WMI(namespace='root\OpenHardwareMonitor')

    while(True):
        for sensor in sensors.Sensor():
            #print("{} {}: {}".format(sensor.Name, sensor.SensorType, sensor.Value))
            formattedname = (sensor.Name + ' ' + sensor.SensorType)
            datatuple = (formattedname, sensor.Value)
            datalist.append(datatuple
            #print(datalist)
            for namevalue in datalist:
                if 'Temperature' in namevalue[0]:
                    if 'CPU' in namevalue[0]:
                        cputemp = ('CPU Temperature: ' + str(namevalue[1]))
                    elif 'GPU' in namevalue[0]:
                        gputemp = ('GPU Temperature: ' + str(namevalue[1]))