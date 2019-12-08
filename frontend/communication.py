import socket

HOST = "127.0.0.1"
PORT = 8080

def createConnection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    print(sock)
    return sock


def receivePacket(conn):
    packet_type = conn.recv(1)
    packet_type = int.from_bytes(packet_type, byteorder='big')
    payload_length = conn.recv(1)
    payload_length = int.from_bytes(payload_length, byteorder='big')
    payload = conn.recv(payload_length)
    payload = payload.decode('utf-8')
    return packet_type, payload

def sendPacket(conn, packet_type, payload):
    payload_length = len(payload.encode('utf-8'))
    packet = bytes([packet_type]) + bytes([payload_length]) + payload.encode('utf-8')
    conn.sendall(packet)








