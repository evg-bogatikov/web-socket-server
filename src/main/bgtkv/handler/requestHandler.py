from src.main.bgtkv.service import webSocketService
from src.main.bgtkv.util import requestPars


def handle_request_handshake(request):
    key = requestPars.get_sec_web_socket_key(request)
    return webSocketService.generate_handshake_response(key)


def handler_request_message(request):
    return requestPars.decode_websocket_frame(request)
