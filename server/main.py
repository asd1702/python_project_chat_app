from core.server_handler import ChatServer
from utils.config_manager import get_server_config
from utils.management.admin_console import AdminConsole

if __name__ == '__main__':
    # 통합 설정 가져오기
    server_config = get_server_config()
    
    # 설정 출력
    print(f"서버를 {server_config['host']}:{server_config['port']}에서 시작합니다. (최대 작업자: {server_config['max_workers']}명)")
    
    # 서버 생성
    server = ChatServer(
        host=server_config['host'], 
        port=server_config['port'], 
        max_workers=server_config['max_workers']
    )
    
    # 관리자 콘솔 시작
    console = AdminConsole(server)
    console.start()
    
    # 서버 시작
    try:
        server.start()
    except KeyboardInterrupt:
        print("\n인터럽트 감지됨. 서버를 종료합니다...")
        server.shutdown()
    