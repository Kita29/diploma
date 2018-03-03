import os, socket, platform

HOST_FQDN = socket.getfqdn()
HOST_NAME = socket.gethostname()
LOGGIN_USER = os.getlogin()
PORT = 50007
OS = platform.system() + " " + platform.release() + " Version:" + platform.version()
INFO_PROCESSOR = platform.processor()
IP_ADDRESS = socket.gethostbyname(socket.gethostname())

print("Basic information about the system\n")
print("Operating system: ", OS)
print("Loggin in as^ ", LOGGIN_USER)
print("Information about the processor: ", INFO_PROCESSOR)
print("Host name: ", HOST_NAME)
print("FQDN: ", HOST_FQDN)
print("Host IP address: ", IP_ADDRESS)


# It can be useful
# print("Operating system name: ", os.name)
# print("Information about the operating system ", os.uname())
# print(socket.gethostbyname_ex(socket.gethostname()))
# print(socket.getaddrinfo(HOST_NAME, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM))
# print(socket.getnameinfo(("172.28.81.15", 80),0))
# print(socket.getaddrinfo(socket.gethostname(), None))
# print(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
# print(platform.node())
# print(platform.uname())
# print(platform.platform())
