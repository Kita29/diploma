import glob
import wmi
import subprocess, sys

DISK_NAME = glob.glob("C:\*.vhd") + glob.glob("C:\*.vhdx")

if DISK_NAME != []:
    POLICY_ROOT_DIR_STATUS = "Disabled"
else:
    POLICY_ROOT_DIR_STATUS = "Enabled"

c=wmi.WMI()
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


print("\nStatus of security policies:\n")
print("Prohibiting the storage of files in the root directory : ", POLICY_ROOT_DIR_STATUS)
print("Prohibit operations with the clipboard : ", POLICY_CLIPBOARD_STATUS)
print("Time synchronization policy : ", POLICY_TIME_STATUS)
p = subprocess.Popen(["powershell.exe","C:\Check.ps1"], stdout=sys.stdout)
p.communicate()

print("\n----Recommendations----")
if POLICY_CLIPBOARD_STATUS == "Disabled":
    print("Turn off the following services: Hyper-V Guest Service Interface and Hyper-V Data Exchange Service")
if POLICY_TIME_STATUS == "Disabled":
    print("Turn on the service: Hyper-V Time Synchronization Service")
if POLICY_ROOT_DIR_STATUS == "Disabled":
    print("Virtual machine disks are located in the root directory!")
    print("You need to change the file storage path")

