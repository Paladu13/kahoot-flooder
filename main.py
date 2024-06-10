import os, re, sys, time, json, base64, random, string, ctypes, getpass, threading
import platform

try:
    import requests
    import uuid
    import datetime
    import colorama
    import pystyle
    import websocket
    import py_mini_racer
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install uuid")
    os.system("pip install datetime")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install websocket-client")
    os.system("pip install py_mini_racer")

from pystyle import Write, System, Colors, Colorate, Center
from colorama import Fore, Style, init
from datetime import datetime

class Output:
    def colored_text(hex_color):
        ansi_color = f"\033[38;2;{int(hex_color[1:3], 16)};{int(hex_color[3:5], 16)};{int(hex_color[5:], 16)}m"
        return ansi_color
    
    reset = colored_text("#ffffff")
    red = colored_text("#c1121f")
    pink = colored_text("#ffafcc")
    medium_dark_green = colored_text("#4f772d")
    dark_green = colored_text("#606c38")
    light_cyan = colored_text("#3bceac")
    green = colored_text("#70e000")
    magenta = colored_text("#662e9b")
    idk = colored_text("#ee6c4d")
    yellow = colored_text("#f0c808")
    strong_red = colored_text("#660708")
    gray = colored_text("#5f7470")
    light_blue = colored_text("#baf2d8")
    light_green = colored_text("#8ea604")
    cherry = colored_text("#b23a48")
    light_magenta = colored_text("#a663cc")
    dark_blue = colored_text("#0d00a4")
    pretty_green = colored_text("#9ef01a")
    turquesa = colored_text("#00916e")
    orange = colored_text("#f77f00")

class Console:
    def title():
        while Stats.working:
            elapsed_time = time.time() - Stats.start
            elapsed_days = int(elapsed_time // 86400)
            elapsed_hours = int((elapsed_time % 86400) // 3600)
            elapsed_minutes = int((elapsed_time % 3600) // 60)
            elapsed_seconds = int(elapsed_time % 60)

            title = f'𝓚𝓪𝓱𝓸𝓸𝓽 𝓕𝓵𝓸𝓸𝓭𝓮𝓻 | 𝓢𝓾𝓬𝓬𝓮𝓼𝓼: {Stats.flooded} - 𝓕𝓪𝓲𝓵𝓮𝓭: {Stats.failed} - 𝓔𝓵𝓪𝓹𝓼𝓮𝓭: {elapsed_days}𝓭 {elapsed_hours}𝓱 {elapsed_minutes}𝓶 {elapsed_seconds}𝓼 | .𝓰𝓰/𝓻𝓪𝓭𝓾𝓬𝓸𝓻𝓭'
            
            if platform.system() == "Windows":
                ctypes.windll.kernel32.SetConsoleTitleW(title)
            else:
                print(title)
            
            time.sleep(1)

class Stats:
    flooded = 0
    failed = 0
    start = time.time()
    working = True

class Websockets:
    def __init__(self) -> None:
        pass

    def __connect__(self) -> dict:
        return [
            {
                "id": "1",
                "version": "1.0",
                "minimumVersion": "1.0",
                "channel": "/meta/handshake",
                "supportedConnectionTypes": [
                    "websocket",
                    "long-polling",
                    "callback-polling"
                ],
                "advice": {
                    "timeout": 60000,
                    "interval": 0
                },
                "ext": {
                    "ack": True,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": 0,
                        "o": 0
                    }
                }
            }
        ]
    
    def __clientId__(self, clientId) -> dict:
        return [
            {
                "id": 2,
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "advice": {
                    "timeout": 0
                },
                "clientId": clientId,
                "ext": {
                    "ack": 0,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]
    
    def __clientId2__(self, clientId) -> dict:
        return [
            {
                "id": "3",
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "clientId": clientId,
                "ext": {
                    "ack": 1,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]
    
    def __connectID__(self, clientId, gameId, name) -> dict:
        return [
            {
                "channel": "/service/controller",
                "clientId": clientId,
                "data": {
                    "content": "{\"device\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0\",\"screen\":{\"width\":920,\"height\":974}}}",
                    "gameid": gameId,
                    "host": "kahoot.it",
                    "name": name,
                    "type": "login"
                },
                "ext": {},
                "id": "4"
            }
        ]
    
    def __keepInGame__(self, clientId, gameId) -> dict:
        return [
            {
                "id": "5",
                "channel": "/service/controller",
                "clientId": clientId,
                "data": {
                    "content": "{\"usingNamerator\":false}",
                    "gameid": gameId,
                    "host": "kahoot.it",
                    "id": 16,
                    "type": "message"
                },
                "ext": {}
            }
        ]
    
    def __metaConnect__(self, clientId) -> dict:
        return [
            {
                "id": "6",
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "clientId": clientId,
                "ext": {
                    "ack": 2,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]
    
    def __ezFlooder__(self, clientId, id, ack) -> dict:
        return [
            {
                "id": id,
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "clientId": clientId,
                "ext": {
                    "ack": ack,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]

class Solver:
    def __init__(self, challenge, token) -> None:
        self.challenge = challenge
        self.session_token = token

    def __xorStrings__(self, challenge, token) -> str:
        result = ""
        for c1, c2 in zip(challenge, base64.b64decode(token).decode('utf-8', 'strict')):
            result += chr(ord(c1) ^ ord(c2))

        return result

    def __solve__(self) -> str:
        text = re.split("[{};]", self.challenge.encode('ascii', 'ignore').decode('utf-8').replace('\t', '', -1))
        js_code = [text[1] + "{", text[2] + ";", "return message.replace(/./g, function(char, position) {", text[7] + ";})};", text[0]]
        js = py_mini_racer.MiniRacer()
        solved = js.eval("".join(js_code).replace('this', ''))
        result = self.__xorStrings__(solved, self.session_token)
        return result

class KahootFlooder:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def __flood__(self) -> None:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            }
            
            response = requests.get(f"https://kahoot.it/reserve/session/{self.id}/?{random.randint(100000, 999999)}", headers=headers)
            response.raise_for_status()

            data = response.json()
            if "twoFactorAuth" in data and data["twoFactorAuth"] is not None:
                print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.cherry}!{Output.reset}) {Output.gray}Two Factor Authentication is enabled for this session. Bot cannot join.{Output.reset}")
                Stats.failed += 1
                return
            
            solved = Solver(data["challenge"]["challenge"], data["session"]["token"]).__solve__()
            response = requests.post(
                f"https://kahoot.it/reserve/session/{self.id}/join/?{random.randint(100000, 999999)}",
                headers=headers,
                json={"challengeResponse": solved, "deviceId": str(uuid.uuid4())}
            )
            response.raise_for_status()
            data = response.json()
            if "error" in data:
                print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.cherry}!{Output.reset}) {Output.gray}Error: {data['error']}{Output.reset}")
                Stats.failed += 1
                return
            
            websocket.enableTrace(False)
            ws = websocket.WebSocket()
            ws.connect(data["session"]["webSocketUrl"].replace("wss://", "ws://"), http_proxy_host="127.0.0.1", http_proxy_port=8888)

            ws.send(json.dumps(Websockets().__connect__()))
            data = json.loads(ws.recv())[0]
            if "error" in data:
                print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.cherry}!{Output.reset}) {Output.gray}Error: {data['error']}{Output.reset}")
                Stats.failed += 1
                return

            clientId = data["clientId"]
            ws.send(json.dumps(Websockets().__clientId__(clientId)))
            data = json.loads(ws.recv())[0]
            if "error" in data:
                print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.cherry}!{Output.reset}) {Output.gray}Error: {data['error']}{Output.reset}")
                Stats.failed += 1
                return

            ws.send(json.dumps(Websockets().__clientId2__(clientId)))
            ws.send(json.dumps(Websockets().__connectID__(clientId, self.id, self.name)))
            data = json.loads(ws.recv())[0]
            if "error" in data:
                print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.cherry}!{Output.reset}) {Output.gray}Error: {data['error']}{Output.reset}")
                Stats.failed += 1
                return

            Stats.flooded += 1
            while Stats.working:
                ws.send(json.dumps(Websockets().__keepInGame__(clientId, self.id)))
                time.sleep(5)
                ws.send(json.dumps(Websockets().__metaConnect__(clientId)))
        except Exception as e:
            print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.cherry}!{Output.reset}) {Output.gray}Exception: {str(e)}{Output.reset}")
            Stats.failed += 1

    @staticmethod
    def __time__() -> str:
        return datetime.now().strftime("%H:%M:%S")

# Variables prédéfinies
PREDEFINED_THREADS = 10  # Remplacez par le nombre de bots souhaité
PREDEFINED_NAMES = "BotName"  # Remplacez par le nom des bots souhaité
PREDEFINED_KAHOOT_ID = "123456"  # Remplacez par le code du jeu Kahoot souhaité

if __name__ == "__main__":
    try:
        Write.Print(f'''
\t\t88888888ba                        88               88                                             
\t\t88      "8b                       88               88                                      ,d     
\t\t88      ,8P                       88               88                                      88     
\t\t88aaaaaa8P'  ,adPPYYba,   ,adPPYb,88  88       88  88,dPPYba,    ,adPPYba,    ,adPPYba,  MM88MMM  
\t\t88""""88'    ""     `Y8  a8"    `Y88  88       88  88P'    "8a  a8"     "8a  a8"     "8a   88     
\t\t88    `8b    ,adPPPPP88  8b       88  88       88  88       88  8b       d8  8b       d8   88     
\t\t88     `8b   88,    ,88  "8a,   ,d88  "8a,   ,a88  88       88  "8a,   ,a8"  "8a,   ,a8"   88,    
\t\t88      `8b  `"8bbdP"Y8   `"8bbdP"Y8   `"YbbdP'Y8  88       88   `"YbbdP"'    `"YbbdP"'    "Y888\n''', Colors.purple_to_red, interval=0.000)
        line = f"{Output.cherry}={Output.red}="
        print(line * 60)

        threading.Thread(target=Console.title).start()

        # Utilisation des variables prédéfinies
        threads = PREDEFINED_THREADS
        names = PREDEFINED_NAMES
        kahoot_id = PREDEFINED_KAHOOT_ID
        print(f"\n{Output.gray} {KahootFlooder.__time__()} {Output.reset}({Output.cherry}?{Output.reset}) {Output.gray}Bot Amount: {Output.light_cyan}{threads}")
        print(f"{Output.gray} {KahootFlooder.__time__()} {Output.reset}({Output.cherry}?{Output.reset}) {Output.gray}Bot Names: {Output.light_cyan}{names}")
        print(f"{Output.gray} {KahootFlooder.__time__()} {Output.reset}({Output.cherry}?{Output.reset}) {Output.gray}Kahoot Game ID: {Output.light_cyan}{kahoot_id}\n")

        while True:
            while threading.active_count() - 1 < int(threads) + 1:
                kahoot = KahootFlooder(
                    id = kahoot_id,
                    name = names
                )
                threading.Thread(target=kahoot.__flood__).start()
            time.sleep(1)
    except Exception as e:
        print(f"{Output.gray} {KahootFlooder.__time__()} {Output.reset}({Output.cherry}!{Output.reset}) {Output.gray}Exception: {str(e)}{Output.reset}")
