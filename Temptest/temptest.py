import kivy
import wmi
import subprocess
import atexit
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import kivy.properties as properties
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager

datalist = []

sensors = wmi.WMI(namespace='root\OpenHardwareMonitor')

def HardwareMonitorOpen():
    return subprocess.Popen(['c:\\Users\\ccrai\\Downloads\\Finalproj\\Temps\\OpenHardwareMonitor\\OpenHardwareMonitor.exe'])

def HardWareMonitorClose(process_):
    process_.kill()

class NumDef(Widget):
    numdef = properties.NumericProperty(0)

class MainWindow(Screen):
    cputemp = properties.ObjectProperty(None)
    gputemp = properties.ObjectProperty(None)
    cpupercent = properties.ObjectProperty(None)
    gpupercent = properties.ObjectProperty(None)

    def update(self, dt):
        #temps
        for sensor in sensors.Sensor():
            formattedname = (sensor.Name + ' ' + sensor.SensorType)
            datatuple = (formattedname, sensor.Value)
            datalist.append(datatuple)
            if 'Temperature' in datatuple[0]:
                if 'CPU' in datatuple[0]:
                    self.cputemp.numdef = int(datatuple[1])
                elif 'GPU' in datatuple[0]:
                    self.gputemp.numdef = int(datatuple[1])
            if 'Load' in datatuple[0]:
                if 'CPU' and 'Total' in datatuple[0]:
                    self.cpupercent.numdef = int(datatuple[1])
                elif 'GPU Core Load' in datatuple[0]:
                    self.gpupercent.numdef = int(datatuple[1])

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass
        
kv = Builder.load_file('temptest.kv')

class TempApp(App):
    def build(self):
        temps = MainWindow()
        Clock.schedule_interval(temps.update, 1.0)
        #kv.MainWindow = temps
        #kv.mainscreen = temps
        return kv
        
if __name__ == '__main__':
    HardwareMonitor = HardwareMonitorOpen()
    atexit.register(HardWareMonitorClose, HardwareMonitor)
    TempApp().run()