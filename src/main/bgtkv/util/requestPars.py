
def get_sec_web_socket_key(request):
    headers = request.split("\r\n")
    for header in headers:
        if header.startswith("Sec-WebSocket-Key:"):
            return header.split(":")[1].strip()
    return None

def decode_websocket_frame(frame):
    payload_length = frame[1] & 0x7F
    mask_start = 2
    if payload_length == 126:
        payload_length = int.from_bytes(frame[2:4], byteorder='big')
        mask_start = 4
    elif payload_length == 127:
        payload_length = int.from_bytes(frame[2:10], byteorder='big')
        mask_start = 10

    masks = frame[mask_start:mask_start+4]
    data_start = mask_start + 4

    decoded_data = bytearray()
    for i in range(data_start, data_start + payload_length):
        decoded_byte = frame[i] ^ masks[(i - data_start) % 4]
        decoded_data.append(decoded_byte)

    return decoded_data.decode()
