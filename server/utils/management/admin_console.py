import threading

class AdminConsole:
    """관리자 콘솔 클래스"""
    def __init__(self, server):
        self.server = server
        self.thread = None


    """관리자 콘솔 스레드 시작"""
    def start(self):
        self.thread = threading.Thread(target=self._console_loop, daemon=True)
        self.thread.start()
        return self.thread
    

    """관리자 콘솔 실행 루프"""
    def _console_loop(self):
        print("관리자 콘솔이 활성화되었습니다. 'quit' 또는 'exit'를 입력하여 서버를 종료할 수 있습니다.")
        print("Docker 컨테이너에서 실행 시 'Ctrl + C'를 눌러 서버를 종료할 수 있습니다.")
        while True:
            cmd = input(">> ").strip().lower()
            if cmd in ["quit", "exit", "shutdown"]:
                print("서버를 종료합니다...")
                self.server.shutdown()
                break
            elif cmd == "help":
                self._show_help()
            else:
                print(f"알 수 없는 명령어: {cmd}")
    

    """도움말 출력"""
    def _show_help(self):
        print("사용 가능한 명령어:")
        print("- quit, exit, shutdown: 서버 종료")
        print("- help: 도움말 표시")