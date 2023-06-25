import base64
import hashlib

def generate_handshake_response(sec_websocket_key):
    if sec_websocket_key is not None:
        return build_frame_handshake(sec_websocket_key)


def build_frame_handshake(key):
    response_key = base64.b64encode(hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()).decode()

    # Формируем отклик
    response = "HTTP/1.1 101 Switching Protocols\r\n"
    response += "Upgrade: websocket\r\n"
    response += "Connection: Upgrade\r\n"
    response += "Sec-WebSocket-Accept: " + response_key + "\r\n"
    response += "\r\n"
    return response
