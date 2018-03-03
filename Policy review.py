# #import getpass
# import subprocess, sys
#
# # def __init__(self, serviceName):
# #     self.c = wmi.WMI()
# #     self.serviceName = serviceName
# #
# # def setServiceName(selfself, serviceName):
# #     self.serviceName = serviceName
# #
# # def getStatus(self):
# #     srv = c.Win32_Service(name=self.serviceName)
# #     if srv != []:
# #         return c.Status
# #     return False
# #
# # print(getStatus("vmicguestinterface"))
#
# p = subprocess.Popen(["powershell.exe","C:\Check.ps1"], stdout=sys.stdout)
# p.communicate()

# import tkinter as tk
# from module import *

# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Main(root)
#     app.pack()
#     root.title("balbal")
#     root.geometry("650x450+300+200")
#     root.resizable(False, False)
#     root.mainloop()

from tkinter import *
import glob
import wmi
import subprocess, sys




root = Tk()
root.title("Policy review")
# root["bg"] = '#009900'
root.geometry("720x640+490+170")

def click_button():
    label_height = 15
    coor_x = 20
    coor_y = 90
    n = 0

    DISK_NAME = glob.glob("C:\*.vhd") + glob.glob("C:\*.vhdx")

    if DISK_NAME != []:
        POLICY_ROOT_DIR_STATUS = "Disabled"
    else:
        POLICY_ROOT_DIR_STATUS = "Enabled"

    c = wmi.WMI()
    for service in c.Win32_Service(Caption="Hyper-V Guest Service Interface"):
        if service.State == "Stopped":
            POLICY_CLIPBOARD_STATUS = "Enabled"
        else:
            POLICY_CLIPBOARD_STATUS = "Disabled"
    for service in c.Win32_Service(Caption="Hyper-V Data Exchange Service"):
        if service.State == "Running":
            if POLICY_CLIPBOARD_STATUS == "Enabled":
                POLICY_CLIPBOARD_STATUS = "Disabled"
    for service in c.Win32_Service(Caption="Hyper-V Time Synchronization Service"):
        if service.State == "Running":
            POLICY_TIME_STATUS = "Enabled"
        else:
            POLICY_TIME_STATUS = "Disabled"

        Label(root, text="\n----Status of security policies----\n").place(x=coor_x, y=coor_y, height=label_height)
        coor_y += label_height
        Label(root, text="Prohibiting the storage of files in the root directory : " + POLICY_ROOT_DIR_STATUS).place(x=coor_x, y=coor_y, height=label_height)
        coor_y += label_height
        Label(root, text="Prohibit operations with the clipboard : " + POLICY_CLIPBOARD_STATUS).place(x=coor_x, y=coor_y, height=label_height)
        coor_y += label_height
        Label(root, text="Time synchronization policy : " + POLICY_TIME_STATUS).place(x=coor_x, y=coor_y, height=label_height)
        coor_y += label_height

        p = subprocess.Popen(["powershell.exe", "C:\Check.ps1"], stdout=subprocess.PIPE)
        date = p.communicate()
        ret = date[0]
        Label(root, text=(str(ret))).place(x=coor_x, y=coor_y, height=label_height)
        coor_y += label_height

        Label(root, text="----Recommendations----").place(x=coor_x, y=coor_y, height=label_height)
        coor_y += label_height
        if POLICY_CLIPBOARD_STATUS == "Disabled":
            Label(root, text="Turn off the following services: Hyper-V Guest Service Interface and Hyper-V Data Exchange Service").place(x=coor_x, y=coor_y, height=label_height)
            coor_y += label_height
        if POLICY_TIME_STATUS == "Disabled":
            Label(root, text="Turn on the service: Hyper-V Time Synchronization Service").place(x=coor_x, y=coor_y, height=label_height)
            coor_y += label_height
        if POLICY_ROOT_DIR_STATUS == "Disabled":
            Label(root, text="Virtual machine disks are located in the root directory!").place(x=coor_x, y=coor_y, height=label_height)
            coor_y += label_height
            Label(root, text="You need to change the file storage path").place(x=coor_x, y=coor_y, height=label_height)
            coor_y += label_height




Label(root, text="Helloooooooooooooooooooooooooooooooooooooooooooooo", font=("Courier", 0, "bold")).place(relx=.5, rely=.05, anchor="c")
HOSTIP = StringVar()
HOSTIP_label = Label(root, text="Enter the IP address of the target host").place(relx=.2, rely=.1, anchor="c")
HOSTIP_entry = Entry(textvariable=HOSTIP)
HOSTIP_entry.place(relx=.5, rely=.1, anchor="c")

btn = Button(text="Start a host check", padx="20", pady="8", command = click_button).place(relx=.7, rely=.1, anchor="c")




root.mainloop()