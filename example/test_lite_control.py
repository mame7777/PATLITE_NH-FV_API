import socket
import sys

HOST = '192.168.x.x'  # IPアドレスを指定
PORT = 10000          # ポート番号を指定

def send_signal(send_type, send_size, send_data):
    # ソケットを作成
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # サーバに接続
    sock.connect((HOST, PORT))
    # データを受信
    data = sock.send(b'\x58\x58' + send_type + b'\x00' + send_size + send_data)
    # # データを表示
    # print(data)
    # ソケットを閉じる
    sock.close()
    return data



def main():
    # send_signalの第三引数を操作したい内容に変更してください
    return_data = send_signal(b'\x53', b'\x00\x06', b'\x09\x09\x09\x09\x09\x09')
    return {"result": return_data}

if __name__ == '__main__':
    main()