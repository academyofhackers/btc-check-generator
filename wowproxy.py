import socket
import requests
from datetime import datetime

class WowProxy:
    def __init__(self, ip, port, max_connect, buffer_size, logging):
        s = ""
        try:
            s = int(port)
        except:
            raise "TypeError: \"port\" must be int"
        try:
            s = int(max_connect)
        except:
            raise "TypeError: \"max_connect\" must be int"
        try:
             s = int(buffer_size)
        except:
            raise "TypeError: \"buffer_size\" must be int"
        try:
            s = bool(logging)
        except:
            raise "TypeError: \"logging\" must be bool"
        del s
        self.ip = str(ip)
        self.port = int(port)
        self.max_connect = int(max_connect)
        self.buffer_size = int(buffer_size)
        self.logging = bool(logging)
    def __str__(self):
        return {"ip": self.ip, "port": self.port, "max_connect": self.max_connect, "buffer_size": self.buffer_size, "logging": self.logging}
    def start(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((self.ip, self.port))
        if self.logging == True:
                print("[+] " + str(datetime.now()) + ": Server binded")
        else:
            pass
        self.__server.listen(self.max_connect)
        if self.logging == True:
            print("[+] " + str(datetime.now()) + ": Server listening")
        else:
            pass
        while True:
            self.__conn, self.__addr = self.__server.accept()
            if self.logging == True:
                print("[+] " + str(datetime.now()) + ": Recieved new connection from user " + self.__addr[0] + ":" + str(self.__addr[1]))
            while True:
                self.__data = self.__conn.recv(self.buffer_size)
                if self.logging == True:
                    print("[+] " + str(datetime.now()) + ": Recieved data from user " + self.__addr[0] + ":" + str(self.__addr[1]))
                else:
                    pass
                try:
                    self.__host = self.__data.split("Host: ")[1].split("\n")[0].split(" ")[0]
                    self.__get = self.__data.split("\n\n")[1]
                    self.__url = self.__host + self.__data.split(" ")[1] + "?" + self.__geta
                    self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    try:
                        self.__client.connect("http://" + url, 80)
                        self.__target_port=80
                    except:
                        self.__client.connect("https://" + url, 443)
                        self.__target_port = 443
                    if self.logging == True:
                        print("[+] " + str(datetime.now()) + ": Connected to " + self.__host + ":" + self.__target_port)
                    else:
                        pass
                    self.__client.send(self.__data)
                    if self.logging == True:
                        print("[+] " + str(datetime.now()) + ": Sent data to " + self.__host + ":" + self.__target_port)
                    self.__data2 = self.__client.recv(self.buffer_size)
                    if self.logging == True:
                        print("[+] " + str(datetime.now()) + ": Recieved data from "+ self.__host + ":" + self.__target_port)
                    else:
                        pass
                    self.__conn.send(self.__data2)
                    if self.logging == True:
                        print("[+] " + str(datetime.now()) + ": Sent data to user " + self.__addr[0] + ":" + self.__addr[0])
                    else:
                        pass
                except:
                    self.__conn.send("Error!")
                    self.__conn.close()
                    if self.logging == True:
                        print("[+] " + str(datetime.now()) + ": Error for user " + self.__addr[0] + ":" + self.__addr[1] + ". Connection closed")
                    else:
                        pass

if __name__ == "__main__":
    proxy = WowProxy(socket.gethostname(), 8080, 1, 10000, True)
    self_ip = requests.get("https://api.ipify.org/").text
    print("[+] Creating proxy on " + self_ip + ":" + "8080")
    proxy.start()
