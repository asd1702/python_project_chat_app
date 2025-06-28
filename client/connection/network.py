import socket

class ChatConnection:
    """클라이언트와 서버 간의 연결을 관리하는 클래스"""
    def __init__(self, host='127.0.0.1', port=12345):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host, self.port = host, port
        self.connected = False

    """서버에 연결을 시도하고 성공 여부를 반환"""
    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
            self.connected = True
            return True
        except ConnectionRefusedError:
            return False
        except Exception as e:
            print(f"연결 오류: {e}")
            return False

    """메시지를 서버로 전송하고 성공 여부를 반환"""
    def send(self, message: str):
        try:
            if self.connected:
                self.sock.sendall(message.encode('utf-8'))
                return True
            return False
        except Exception as e:
            self.connected = False
            print(f"전송 오류: {e}")
            return False

    """서버로부터 메시지를 수신하고 디코딩하여 반환"""
    def receive(self, bufsize=1024) -> str:
        try:
            if not self.connected:
                return ''
            data = self.sock.recv(bufsize)
            if not data:
                self.connected = False
                return ''
            return data.decode('utf-8')
        except Exception as e:
            self.connected = False
            print(f"수신 오류: {e}")
            return ''

    """소켓을 닫고 연결 상태를 False로 설정"""
    def close(self):
        try:
            self.sock.close()
        except:
            pass
        finally:
            self.connected = False