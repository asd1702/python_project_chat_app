import datetime

class MessageFormatter:
    """메시지 포맷터 클래스"""

    """사용자가 채팅에 입장할 때 메시지 포맷"""
    @staticmethod
    def format_entry_message(nickname):
        timestamp = datetime.datetime.now().strftime('%H:%M')
        return f"[{timestamp}] [{nickname}]님이 입장했습니다."
    

    """사용자가 채팅 메시지를 보낼 때 메시지 포맷"""
    @staticmethod
    def format_chat_message(nickname, message):
        timestamp = datetime.datetime.now().strftime('%H:%M')
        return f"[{timestamp}] {nickname}: {message}"
    

    """사용자가 채팅에서 퇴장할 때 메시지 포맷"""
    @staticmethod
    def format_exit_message(nickname):
        timestamp = datetime.datetime.now().strftime('%H:%M')
        return f"[{timestamp}] [{nickname}]님이 퇴장했습니다."