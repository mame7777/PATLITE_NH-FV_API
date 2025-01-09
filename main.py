import os
import socket

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
HOST = os.getenv("PATLITE_IP")
PORT = int(os.getenv("PATLITE_PORT", "0"))


def send_signal(send_type, send_size, send_data):
    # ソケットを作成
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # サーバに接続
    sock.connect((HOST, PORT))
    # データを受信
    data = sock.send(b"\x58\x58" + send_type + b"\x00" + send_size + send_data)
    # ソケットを閉じる
    sock.close()
    return data


app = FastAPI()


@app.post("/api/lights_buzer/{lights_and_buzzer}")
def control_lights_and_buzzer(lights_and_buzzer: str):
    if len(lights_and_buzzer) != 6:
        return {"error": "Invalid argument"}
    lights = lights_and_buzzer[:5]
    buzzer = lights_and_buzzer[5]

    send_data = b""

    for light in lights:
        if light == "0":
            send_data += b"\x00"
        elif light == "1":
            send_data += b"\x01"
        elif light == "2":
            send_data += b"\x02"
        elif light == "3":
            send_data += b"\x03"
        elif light == "9":
            send_data += b"\x09"
        else:
            return {"error": "Invalid light mode"}

    if buzzer == "0":
        send_data += b"\x00"
    elif buzzer == "1":
        send_data += b"\x01"
    elif buzzer == "2":
        send_data += b"\x02"
    elif buzzer == "3":
        send_data += b"\x03"
    elif buzzer == "4":
        send_data += b"\x04"
    elif buzzer == "9":
        send_data += b"\x09"
    else:
        return {"error": "Invalid buzzer mode"}

    return_data = send_signal(
        send_type=b"\x53", send_size=b"\x00\x06", send_data=send_data
    )
    return {"send_data": send_data, "result": return_data}
