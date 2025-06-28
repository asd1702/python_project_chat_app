import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class ChatLogDisplay:
    """채팅 로그를 표시하는 컴포넌트"""
    def __init__(self, parent):
        self.log_widget = ScrolledText(
            parent,
            state='disabled',
            wrap='word',
            height=20,
            bg="#f0f0f0",
            borderwidth=1,
            relief="solid"
        )
        self.log_widget.pack(fill='both', expand=True, padx=5, pady=5)
    
    def append_message(self, msg):
        """채팅 로그에 새 메시지를 추가"""
        try:
            self.log_widget.configure(state='normal')
            self.log_widget.insert('end', msg + '\n')
            self.log_widget.configure(state='disabled')
            self.log_widget.yview('end')    # 스크롤 맨 아래로
            return True
        except Exception:
            return False
    
    def clear(self):
        """채팅 로그를 비움"""
        try:
            self.log_widget.configure(state='normal')
            self.log_widget.delete(1.0, 'end')
            self.log_widget.configure(state='disabled')
            return True
        except Exception:
            return False
