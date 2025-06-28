import datetime
import os
import json

class ChatLogger:
    """채팅 로그를 기록하는 클래스"""
    def __init__(self):
        # 로깅 설정 로드
        self.config = self._load_logging_config()
    

    """로깅 설정 로드"""
    @staticmethod
    def _load_logging_config():
        try:
            # server/utils/logging -> server/utils -> server -> server/config
            config_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 
                "config", 
                "config.json"
            )
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get("logging", {})
        except Exception:
            return {"log_directory": "logs", "console_level": "NONE"}
    

    """로그 파일 경로를 현재 날짜에 맞춰 반환"""
    @staticmethod
    def _get_log_file():
        log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "logs")
        os.makedirs(log_dir, exist_ok=True)
        
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        log_file = os.path.join(log_dir, f"chat_log_{today}.txt")
        return log_file


    """로그 파일에 메시지 기록"""
    @staticmethod
    def _write_to_log(message):
        try:
            with open(ChatLogger._get_log_file(), 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
        except Exception as e:
            print(f"로그 저장 오류: {e}")   # 예외발생 시 터미널에 출력


    """사용자가 채팅에 입장할 때 로그 기록"""
    @staticmethod
    def log_entry(nickname, ip_address=None):
        timestamp = datetime.datetime.now().strftime('%H:%M')
        ip_info = f" (IP: {ip_address})" if ip_address else ""
        message = f"사용자 [{nickname}]{ip_info}님이 {timestamp}에 입장했습니다."
        ChatLogger._write_to_log(message)
        return message
    

    """사용자가 채팅 메시지를 보낼 때 로그 기록"""
    @staticmethod
    def log_message(nickname, message, ip_address=None):
        timestamp = datetime.datetime.now().strftime('%H:%M')
        ip_info = f" (IP: {ip_address})" if ip_address else ""
        log_message = f"채팅 기록: {timestamp} - {nickname}{ip_info}: {message}"
        ChatLogger._write_to_log(log_message)
        return log_message
    

    """사용자가 채팅에서 퇴장할 때 로그 기록"""
    @staticmethod
    def log_exit(nickname, ip_address=None):
        timestamp = datetime.datetime.now().strftime('%H:%M')
        ip_info = f" (IP: {ip_address})" if ip_address else ""
        message = f"사용자 [{nickname}]{ip_info}님이 {timestamp}에 퇴장했습니다."
        ChatLogger._write_to_log(message)
        return message
