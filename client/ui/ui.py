import threading
import time

class ChatUI:
    """채팅 UI 클래스"""
    def __init__(self, connection):
        self.conn = connection
        self.running = True

    """채팅 UI를 시작하는 메서드"""
    def start_receiving(self):
        # 메시지 수신을 위한 스레드 시작
        def _recv_loop():
            while self.running:
                # 메시지 수신 시도
                try:
                    msg = self.conn.receive()
                    if not msg:
                        print("\n[알림] 서버와의 연결이 끊겼습니다.")
                        self.running = False
                        break
                    print(msg)
                #  예외 발생 시 처리
                except Exception as e:
                    print(f"\n[오류] 서버 연결 문제: {e}")
                    self.running = False
                    break
                time.sleep(0.1)
        # 스레드 생성 및 시작
        t = threading.Thread(target=_recv_loop, daemon=True)
        t.start()

    """메시지 전송을 위한 입력 처리"""
    def start_sending(self):
        try:
            # 사용자 입력을 받아 메시지 전송
            while self.running:
                text = input()
                if text.lower() == '/quit':
                    self.running = False
                    self.conn.close()
                    print("채팅 종료")
                else:
                    if not self.conn.send(text):
                        print("[알림] 메시지를 전송할 수 없습니다. 서버와의 연결이 끊겼습니다.")
                        self.running = False
        # 예외 발생 시 처리
        except (KeyboardInterrupt, EOFError):
            self.running = False
            self.conn.close()