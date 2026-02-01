"""ВНИМАНИЕ!!! ЧТОБЫ ЗАКРЫТЬ ОКНО ПЕРЕД ЗАПУСКОМ ПРОГРАМЫ ВЫБИРИТЕ АНГЛИЙСКУЮ РАСКЛАТКУ И КОГДА ВЫБЬЕТ ОКНО НАЖМИТЕ БУКВУ q МАЛЕНЬКУЮ ИНАЧЕ ПРИЙДЕТСЯ ПЕРЕЗАПУСТИТЬ КОМПЬЮТЕР"""
import pyautogui
from rich.progress import track
from rich.console import Console
# from rich.panel import Panel
import tkinter as tk 
import time
import sys

console = Console()
"""ВНИМАНИЕ!!! ЧТОБЫ ЗАКРЫТЬ ОКНО ПЕРЕД ЗАПУСКОМ ПРОГРАМЫ ВЫБИРИТЕ АНГЛИЙСКУЮ РАСКЛАТКУ И КОГДА ВЫБЬЕТ ОКНО НАЖМИТЕ БУКВУ q МАЛЕНЬКУЮ ИНАЧЕ ПРИЙДЕТСЯ ПЕРЕЗАПУСТИТЬ КОМПЬЮТЕР"""

def open_full_screen_error():
     pyautogui.hotkey('win', 'd') 
     time.sleep(1)
     root = tk.Tk()

     root.attributes("-fullscreen", True)

     root.attributes("-topmost", True)

     root.protocol("WM_DELETE_WINDOW", lambda: None)

     root.configure(background='red')
     root.config(cursor="none")
     root.lift()
     root.focus_force()
     label = tk.Label(
        root, 
        text="СИСТЕМА УНИЧТОЖЕНА", 
        fg="white", 
        bg="red", 
        font=("Courier New", 60, "bold")
    )
     label.pack(expand=True)

     sub_label = tk.Label(
        root, 
        text="ALL DATA HAS BEEN ERASED\nREBOOT IMPOSSIBLE", 
        fg="white", 
        bg="red", 
        font=("Courier New", 20)
    )
     sub_label.pack(expand=True)

     root.bind("q", lambda event: root.destroy())
     root.mainloop()
     

"""ВНИМАНИЕ!!! ЧТОБЫ ЗАКРЫТЬ ОКНО ПЕРЕД ЗАПУСКОМ ПРОГРАМЫ ВЫБИРИТЕ АНГЛИЙСКУЮ РАСКЛАТКУ И КОГДА ВЫБЬЕТ ОКНО НАЖМИТЕ БУКВУ q МАЛЕНЬКУЮ ИНАЧЕ ПРИЙДЕТСЯ ПЕРЕЗАПУСТИТЬ КОМПЬЮТЕР"""


def proga():
    console.clear()
    lines = [
            (r"INITIALIZING SYSTEM PURGE...", 0.01),
            (r"ACCESSING ROOT DIRECTORY: C:\WINDOWS\...", 0.008),
            (r"BYPASSING KERNEL SECURITY...", 0.009),
            (r"ADMIN PRIVILEGES GRANTED.", 0.01),
            (r"SCANNING FOR CONNECTED DRIVES...", 0.005),
            (r"DRIVE C:\ [NTFS] FOUND.", 0.005),
            (r"DRIVE D:\ [FAT32] FOUND.", 0.005),
            (r"INFECTING BOOT SECTOR...", 0.007),
            (r"OVERRIDING BIOS PERMISSIONS...", 0.008),
            (r"SHUTDOWN PROTECTION: DISABLED.", 0.006),

            (r"delete windows\C:\Windows\System32\drivers\tcpip.sys", 0.0001),
            (r"delete windows\C:\Windows\System32\drivers\ntfs.sys", 0.0001),
            (r"delete windows\C:\Windows\System32\drivers\volsnap.sys", 0.0001),
            (r"delete windows\C:\Windows\System32\drivers\pci.sys", 0.0001),
            (r"delete windows\C:\Windows\System32\drivers\usbhub.sys", 0.0001),
            (r"delete windows\C:\Windows\System32\hal.dll", 0.0001),
            (r"delete windows\C:\Windows\System32\winload.exe", 0.0001),
            (r"delete windows\C:\Windows\System32\ntoskrnl.exe", 0.0001),
            (r"delete windows\C:\Windows\System32\config\SAM", 0.0001),
            (r"delete windows\C:\Windows\System32\config\SECURITY", 0.0001),
            (r"delete windows\C:\Windows\System32\config\SOFTWARE", 0.0001),
            (r"delete windows\C:\Windows\System32\config\SYSTEM", 0.0001),

            (r"delete windows\C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default\History", 0.0001),
            (r"delete windows\C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default\Cookies", 0.0001),
            (r"delete windows\C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default\Login Data", 0.0001),
            (r"delete windows\C:\Users\Admin\AppData\Roaming\Telegram Desktop\tdata\key_datas", 0.0001),
            (r"delete windows\C:\Users\Admin\AppData\Roaming\Discord\Local Storage\leveldb", 0.0001),
            (r"delete windows\C:\Users\Admin\Documents\passwords.txt", 0.0001),
            (r"delete windows\C:\Users\Admin\Documents\bank_details.pdf", 0.0001),
            (r"delete windows\C:\Users\Admin\Pictures\Private\backup.zip", 0.0001),

            (r"delete windows\C:\Windows\SysWOW64\kernel32.dll", 0.0001),
            (r"delete windows\C:\Windows\SysWOW64\user32.dll", 0.0001),
            (r"delete windows\C:\Windows\SysWOW64\gdi32.dll", 0.0001),
            (r"delete windows\C:\Windows\SysWOW64\shell32.dll", 0.0001),
            (r"delete windows\C:\Windows\SysWOW64\ole32.dll", 0.0001),
            (r"delete windows\C:\Windows\SysWOW64\advapi32.dll", 0.0001),
            (r"delete windows\C:\Windows\SysWOW64\ws2_32.dll", 0.0001),

            (r"delete windows\C:\Program Files\Common Files\microsoft shared\OFFICE16\mso.dll", 0.0001),
            (r"delete windows\C:\Program Files\NVIDIA Corporation\Display.Driver\nvlddmkm.sys", 0.0001),
            (r"delete windows\C:\Program Files\Steam\steam.exe", 0.0001),
            (r"delete windows\C:\Program Files\Adobe\Adobe Photoshop\Photoshop.exe", 0.0001),
            (r"delete windows\C:\Program Files\Java\jre\bin\java.dll", 0.0001),

            (r"WIPING: C:\Windows\Logs\CBS\...", 0.0001),
            (r"WIPING: C:\Windows\Temp\...", 0.0001),
            (r"WIPING: C:\Windows\SoftwareDistribution\...", 0.0001),
            (r"WIPING: C:\Windows\Prefetch\...", 0.0001),
            (r"WIPING: C:\Windows\Installer\...", 0.0001),

            (r"TERMINATING: svchost.exe", 0.0001),
            (r"TERMINATING: explorer.exe", 0.0001),
            (r"TERMINATING: spoolsv.exe", 0.0001),
            (r"TERMINATING: lsass.exe", 0.0001),
            (r"TERMINATING: csrss.exe", 0.0001),
            (r"ERASING REGISTRY: HKEY_LOCAL_MACHINE\SOFTWARE", 0.0001),
            (r"ERASING REGISTRY: HKEY_CURRENT_USER\Console", 0.0001),
            (r"ERASING REGISTRY: HKEY_CLASSES_ROOT\*", 0.0001),

            (r"delete windows\C:\Users\Admin\Videos\Movies\trip_2023.mp4", 0.0001),
            (r"delete windows\C:\Users\Admin\Music\Library\track_01.mp3", 0.0001),
            (r"delete windows\C:\Users\Admin\Music\Library\track_02.mp3", 0.0001),
            (r"delete windows\C:\Users\Admin\Music\Library\track_03.mp3", 0.0001),
            (r"delete windows\C:\Users\Admin\Downloads\installer.exe", 0.0001),
            (r"delete windows\C:\Users\Admin\Desktop\Work\report_v1.docx", 0.0001),
            (r"delete windows\C:\Users\Admin\Desktop\Work\report_v2.docx", 0.0001),
            (r"delete windows\C:\Users\Admin\Desktop\Work\final_final.docx", 0.0001),

            (r"OVERCLOCKING CPU VOLTAGE: 1.55V... CRITICAL", 0.0001),
            (r"FAN SPEED: 0 RPM (LOCKED)", 0.0001),
            (r"GPU TEMPERATURE: 105°C", 0.0001),
            (r"MOTHERBOARD BUS ERROR: 0x0000005", 0.0001),

            (r"CORRUPTING: sector 0x80001...", 0.0001),
            (r"CORRUPTING: sector 0x80002...", 0.0001),
            (r"CORRUPTING: sector 0x80003...", 0.0001),
            (r"CORRUPTING: sector 0x80004...", 0.0001),
            (r"CORRUPTING: sector 0x80005...", 0.0001),
            (r"CORRUPTING: sector 0x80006...", 0.0001),
            (r"CORRUPTING: sector 0x80007...", 0.0001),
            (r"CORRUPTING: sector 0x80008...", 0.0001),
            (r"CORRUPTING: sector 0x80009...", 0.0001),
            (r"CORRUPTING: sector 0x80010...", 0.0001),

            (r"delete windows\C:\ProgramData\Microsoft\Search\Data\Applications\Windows\windows.edb", 0.0001),
            (r"delete windows\C:\ProgramData\Microsoft\Windows\WER\ReportArchive\...", 0.0001),
            (r"delete windows\C:\ProgramData\Package Cache\{691a-45c1-9022}\...", 0.0001),
            (r"delete windows\C:\$Recycle.Bin\S-1-5-21-34...", 0.0001),
            (r"delete windows\C:\System Volume Information\_restore{...}", 0.0001),

            (r"DECRYPTING PRIVATE KEYS...", 0.0001),
            (r"SENDING DATA TO REMOTE SERVER [192.168.1.1]...", 0.0001),
            (r"DATA TRANSFER: 4.2 GB SENT.", 0.0001),
            (r"ERASING TRACES...", 0.0001),
            (r"DUMPING SYSTEM LOGS...", 0.0001),
            (r"REMOVING RECOVERY PARTITION...", 0.0001),
            (r"DANGER: MBR CORRUPTED.", 0.0001),
            (r"DANGER: KERNEL PANIC.", 0.0001),
            (r"CRITICAL FAILURE.", 0.0001),
        ]
    for step in track(range(100), description="[green]Удаление Windows..."):
                time.sleep(0.02)
    
    delays = [0.001] * len(lines)
    #24
    for i, (line, char_delay) in enumerate(lines):
            for char in line:
                if line == "Rock your body":
                    console.print(f"[orange4]{char}[/orange4]", end="")
                else:
                    console.print(char, style="bold green", end="", highlight=False)
                sys.stdout.flush()
                time.sleep(char_delay)
            console.print()
            time.sleep(delays[i])


    time.sleep(1)
    console.clear()

input("> ")
print("Я думаю что-то не так...")
time.sleep(1)
proga()
open_full_screen_error()

"""ВНИМАНИЕ!!! ЧТОБЫ ЗАКРЫТЬ ОКНО ПЕРЕД ЗАПУСКОМ ПРОГРАМЫ ВЫБИРИТЕ АНГЛИЙСКУЮ РАСКЛАТКУ И КОГДА ВЫБЬЕТ ОКНО НАЖМИТЕ БУКВУ q МАЛЕНЬКУЮ ИНАЧЕ ПРИЙДЕТСЯ ПЕРЕЗАПУСТИТЬ КОМПЬЮТЕР"""
