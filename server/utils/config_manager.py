import json
import os
import argparse

"""서버 설정 파일 로드"""
def load_config():

    # server/utils/ -> server/ -> server/config/
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "config.json")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        # 설정 파일 로드 실패 시 기본값 설정 후 config 디렉토리 생성 시도
        print(f"설정 파일을 찾을 수 없습니다: {e}")
        default_config = {
            "server": {
                "host": "0.0.0.0",
                "port": 12345,
                "max_workers": 20
            },
            "logging": {
                "log_directory": "logs",
                "console_level": "NONE"
            }
        }
        
        # 설정 디렉토리 자동 생성 (없는 경우)
        config_dir = os.path.dirname(config_path)
        try:
            if not os.path.exists(config_dir):
                os.makedirs(config_dir)
                # 기본 설정 파일 생성
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(default_config, f, indent=2)
                print(f"기본 설정 파일이 생성되었습니다: {config_path}")
        except Exception:
            pass
            
        return default_config


"""명령줄 인자 파싱"""
def parse_arguments():
    parser = argparse.ArgumentParser(description='채팅 서버 시작')
    parser.add_argument('--host', help='서버 호스트 주소')
    parser.add_argument('--port', type=int, help='서버 포트')
    parser.add_argument('--workers', type=int, help='최대 작업자 수')
    return parser.parse_args()


"""설정 파일과 명령줄 인자를 통합한 설정 반환"""
def get_server_config():

    # 설정 로드
    config = load_config()
    server_config = config.get("server", {})
    
    # 명령줄 인자 파싱
    args = parse_arguments()
    
    # 설정 적용 (명령줄 인자 우선)
    host = args.host or server_config.get("host", "0.0.0.0")
    port = args.port or server_config.get("port", 12345)
    max_workers = args.workers or server_config.get("max_workers", 20)
    
    return {
        "host": host,
        "port": port, 
        "max_workers": max_workers
    }