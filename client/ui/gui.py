import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import threading

from client.utils.config_manager import get_ui_config
from client.ui.widgets.chat_log import ChatLogDisplay
from client.ui.widgets.message_input import MessageInputArea
from client.connection.connection_manager import ConnectionManager

class ChatGUI:
    """채팅 애플리케이션의 메인 GUI 클래스"""
    def __init__(self, host='127.0.0.1', port=12345):
        # UI 기본 설정
        self.root = tk.Tk()
        self.root.title("Python Chat")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # UI 설정 로드
        ui_config = get_ui_config()
        
        # 한글 폰트 설정
        try:
            import tkinter.font as tkFont
            default_font = tkFont.Font(family=ui_config["font"], size=ui_config["font_size"])
            self.root.option_add("*Font", default_font)
        except:
            pass

        # 메인 프레임
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # 채팅 로그 영역
        self.chat_log = ChatLogDisplay(main_frame)
        
        # 메시지 입력 영역
        self.msg_input = MessageInputArea(main_frame, self.handle_send_message)
        
        # 연결 관리자
        self.connection = ConnectionManager(
            host, 
            port,
            on_message_received=lambda msg: self.root.after(0, self._append_log, msg),
            on_connection_closed=lambda err=None: self.root.after(0, self._handle_disconnect, err)
        )
    
    """서버에 연결하고 메시지를 전송하는 메서드"""
    def start(self):
        # 닉네임 입력 및 연결
        nickname = simpledialog.askstring("닉네임", "닉네임을 입력하세요:")
        if not nickname:
            self.root.destroy()
            return
        
        # 서버 연결 시도
        if not self.connection.connect():
            messagebox.showerror("연결 오류", "서버에 연결할 수 없습니다.")
            self._append_log("[오류] 서버에 연결할 수 없습니다. 프로그램을 종료합니다.")
            self.root.after(3000, self.root.destroy)
            self.root.mainloop()
            return
        
        # 닉네임 전송
        if not self.connection.send_nickname(nickname):
            messagebox.showerror("전송 오류", "닉네임을 서버에 전송할 수 없습니다.")
            self._append_log("[오류] 닉네임 전송 실패. 프로그램을 종료합니다.")
            self.root.after(3000, self.root.destroy)
            self.root.mainloop()
            return
        
        # 메시지 수신 시작
        self.connection.start_receiving()
        
        # 메시지 입력 필드에 포커스
        self.msg_input.focus()
        
        # 메인 루프 시작
        self.root.mainloop()
    
    """채팅 로그에 메시지를 추가"""
    def _append_log(self, msg):
        self.chat_log.append_message(msg)
    
    """메시지 전송 처리"""
    def handle_send_message(self, text):
        if text.lower() == '/quit':
            self.on_closing()
        else:
            success = self.connection.send_message(text)
            if not success:
                self._append_log("[알림] 메시지를 전송할 수 없습니다. 서버 연결이 끊겼습니다.")
    
    """연결 종료 처리"""
    def _handle_disconnect(self, error=None):
        if error:
            self._append_log(f"[오류] 메시지 수신 중 오류 발생: {error}")
        else:
            self._append_log("[알림] 서버 연결이 종료되었습니다.")
    
    """창 닫기 처리"""
    def on_closing(self):
        self.connection.disconnect()
        self.root.destroy()