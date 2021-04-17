import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

import kivy
import wmi
import subprocess
import atexit
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import kivy.properties as properties
from kivy.clock import Clock
from kivy.lang import Builder
import kivy.properties as properties
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button

datalist = []

sensors = wmi.WMI(namespace='root\OpenHardwareMonitor')


def HardwareMonitorOpen():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)
    hardware_monitor_path = os.path.join(parent_directory,"thirdparty","openhardwaremonitor-v0.9.6\OpenHardwareMonitor\OpenHardwareMonitor.exe")
    return subprocess.Popen([hardware_monitor_path])


def HardWareMonitorClose(process_):
    process_.kill()
    process_.terminate()

class NumDef(Widget):
    numdef = properties.NumericProperty(0)

class TempRead(GridLayout):
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
                    
class TempApp(App):
    def build(self):
        temps = TempRead()
        Clock.schedule_interval(temps.update, 1.0)
        return temps
      
if __name__ == '__main__':
    if not is_admin():
        exit()
    HardwareMonitor = HardwareMonitorOpen()
    atexit.register(HardWareMonitorClose, HardwareMonitor)
    TempApp().run()
