from client.ui.gui import ChatGUI
from client.utils.config_manager import get_connection_config

if __name__ == '__main__':
    try:
        # 설정 파일에서 연결 정보 가져오기
        connection_config = get_connection_config()
        
        # GUI 시작
        gui = ChatGUI(
            host=connection_config['host'],
            port=connection_config['port']
        )
        gui.start()
    except Exception as e:
        print(f"프로그램 실행 중 오류가 발생했습니다: {e}")