import wmi
import subprocess
import kivy
from kivy.app import App
from kivy.uix.label import Label

datalist = []
def HardwareMonitorOpen():
    return subprocess.Popen(['c:\\Users\\ccrai\\Downloads\\Finalproj\\Temps\\OpenHardwareMonitor\\OpenHardwareMonitor.exe'])

class AppTest(Widget):
    cputempdisplay = ''
    gputempdisplay = ''

class TempApp(App):
    def build(self):
        return AppTest

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
            for namevalue in datalist:
                if 'Temperature' in namevalue[0]:
                    if 'CPU' in namevalue[0]:
                        print('CPU Temperature: ' + str(namevalue[1]))
                    elif 'GPU' in namevalue[0]:
                        print('GPU Temperature: ' + str(namevalue[1]))
    
    TempApp().run()

