import kivy
import wmi
import subprocess
import atexit
from kivy.app import App
from kivy.uix.widget import Widget
import kivy.properties as properties
from kivy.clock import Clock


datalist = []

sensors = wmi.WMI(namespace='root\OpenHardwareMonitor')

def HardwareMonitorOpen():
    return subprocess.Popen(['c:\\Users\\ccrai\\Downloads\\Finalproj\\Temps\\OpenHardwareMonitor\\OpenHardwareMonitor.exe'])

def HardWareMonitorClose(process_):
    process_.kill()

class ScoreDef(Widget):
    score = properties.NumericProperty(0)

# root widget along with the temp detection
class TempRead(Widget):
    cputemp = properties.ObjectProperty(None)
    gputemp = properties.ObjectProperty(None)
  
    def update(self, dt):
        #temps
        for sensor in sensors.Sensor():
            formattedname = (sensor.Name + ' ' + sensor.SensorType)
            datatuple = (formattedname, sensor.Value)
            datalist.append(datatuple)
            if 'Temperature' in datatuple[0]:
                if 'CPU' in datatuple[0]:
                    self.cputemp.score = int(datatuple[1])
                elif 'GPU' in datatuple[0]:
                    self.gputemp.score = int(datatuple[1])
        
class TempApp(App):
    def build(self):
        temps = TempRead()
        Clock.schedule_interval(temps.update, 1.0)
        return temps
      
if __name__ == '__main__':
    HardwareMonitor = HardwareMonitorOpen()
    atexit.register(HardWareMonitorClose, HardwareMonitor)
    TempApp().run()