from utils.logging.logger import ChatLogger
from utils.messaging.message_formatter import MessageFormatter

class ChatManager:
    """채팅 관리 클래스"""
    def __init__(self):
        self.logger = ChatLogger()
        self.formatter = MessageFormatter()
    

    """사용자가 채팅에 입장할 때 처리, 로그 기록 및 브로드캐스트 메시지 반환"""
    def handle_user_entry(self, nickname, ip_address=None):
        self.logger.log_entry(nickname, ip_address)
        return self.formatter.format_entry_message(nickname)
    
    """사용자가 채팅 메시지를 보낼 때 처리, 로그 기록 및 브로드캐스트 메시지 반환"""
    def handle_chat_message(self, nickname, message, ip_address=None):
        self.logger.log_message(nickname, message, ip_address)
        return self.formatter.format_chat_message(nickname, message)
    

    """사용자가 채팅에서 퇴장할 때 처리, 로그 기록 및 브로드캐스트 메시지 반환"""
    def handle_user_exit(self, nickname, ip_address=None):
        self.logger.log_exit(nickname, ip_address)
        return self.formatter.format_exit_message(nickname)