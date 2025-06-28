import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from utils.messaging.chat_manager import ChatManager

class ChatServer:
    """멀티스레드 채팅 서버 클래스"""
    def __init__(self, host='0.0.0.0', port=12345, max_workers=10):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = {}
        self.lock = threading.Lock()
        self.pool = ThreadPoolExecutor(max_workers=max_workers)
        self.chat_manager = ChatManager()


    """서버 시작 메소드"""
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"서버 시작: {self.host}:{self.port}")
        try:
            while True:
                client_sock, addr = self.server_socket.accept()
                print(f"클라이언트 연결됨: {addr[0]}:{addr[1]}")
                self.pool.submit(self.handle_client, client_sock)
        except (KeyboardInterrupt, OSError):
            print("서버 종료 중...")
        finally:
            self.shutdown()


    """클라이언트 연결 처리 메소드"""
    def handle_client(self, client_sock):
        try:
            client_ip = client_sock.getpeername()[0]
            nickname = client_sock.recv(1024).decode('utf-8').strip()
            
            with self.lock:
                self.clients[client_sock] = nickname
            
            entry_message = self.chat_manager.handle_user_entry(nickname, client_ip)
            self.broadcast(entry_message)

            while True:
                msg = client_sock.recv(1024)
                if not msg:
                    break
                text = msg.decode('utf-8').strip()
                
                broadcast_message = self.chat_manager.handle_chat_message(nickname, text, client_ip)
                self.broadcast(broadcast_message)
        except ConnectionResetError:
            pass
        finally:
            self.remove_client(client_sock)


    """메시지 브로드캐스트 메소드"""
    def broadcast(self, message):
        with self.lock:
            for sock in list(self.clients.keys()):
                try:
                    sock.sendall(message.encode('utf-8'))
                except Exception:
                    self.remove_client(sock)


    """클라이언트 제거 메소드"""
    def remove_client(self, client_sock):
        with self.lock:
            nickname = self.clients.pop(client_sock, None)
        
        if nickname:
            try:
                client_ip = client_sock.getpeername()[0]
            except OSError:
                client_ip = "알 수 없음"
            
            exit_message = self.chat_manager.handle_user_exit(nickname, client_ip)
            self.broadcast(exit_message)
        
        try:
            client_sock.close()
        except Exception:
            pass


    """서버 종료 메소드"""
    def shutdown(self):
        with self.lock:
            for sock in self.clients.keys():
                sock.close()
            self.clients.clear()
        
        if self.server_socket:
            self.server_socket.close()
        
        self.pool.shutdown(wait=True)
        print("서버가 완전히 종료되었습니다.")