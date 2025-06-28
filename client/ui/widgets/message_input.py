import tkinter as tk

class MessageInputArea:
    """메시지 입력 및 전송 컴포넌트"""
    def __init__(self, parent, send_callback):
        self.send_callback = send_callback
        
        # 프레임 생성
        self.frame = tk.Frame(parent)
        self.frame.pack(fill='x', pady=5)
        
        # 텍스트 입력
        self.entry = tk.Entry(self.frame)
        self.entry.pack(side='left', expand=True, fill='x', padx=(0,5))
        self.entry.bind('<Return>', lambda event: self.send_message())
        
        # 전송 버튼
        self.send_btn = tk.Button(self.frame, text="전송", command=self.send_message)
        self.send_btn.pack(side='right')
    
    def send_message(self):
        """메시지 전송 처리"""
        text = self.entry.get().strip()
        if text:
            self.send_callback(text)
            self.entry.delete(0, 'end')
    
    def focus(self):
        """입력 필드에 포커스"""
        self.entry.focus_set()
    
    def get_frame(self):
        """프레임 위젯 반환"""
        return self.frame
