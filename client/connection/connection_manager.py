import threading
from client.connection.network import ChatConnection

class ConnectionManager:
    """서버 연결 및 메시지 송수신 관리 클래스"""
    def __init__(self, host, port, on_message_received, on_connection_closed):
        self.conn = ChatConnection(host, port)
        self.running = False
        self.receive_thread = None
        self.on_message_received = on_message_received
        self.on_connection_closed = on_connection_closed
    
    def connect(self):
        """서버에 연결"""
        return self.conn.connect()
    
    def send_nickname(self, nickname):
        """닉네임 전송"""
        return self.conn.send(nickname)
    
    def start_receiving(self):
        """메시지 수신 스레드 시작"""
        self.running = True
        self.receive_thread = threading.Thread(target=self._receive_loop, daemon=True)
        self.receive_thread.start()
    
    def send_message(self, message):
        """메시지 전송"""
        return self.conn.send(message)
    
    def disconnect(self):
        """연결 종료"""
        self.running = False
        self.conn.close()
    
    def _receive_loop(self):
        """메시지 수신 루프"""
        while self.running:
            try:
                msg = self.conn.receive()
                if not msg:
                    if self.running:
                        self.on_connection_closed()
                    break
                self.on_message_received(msg)
            except Exception as e:
                if self.running:
                    self.on_connection_closed(str(e))
                break