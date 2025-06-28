import json
import os

"""클라이언트 설정 파일 로드"""
def load_config():
    # client/utils/ -> client/ -> client/config/
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "config.json")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        # 설정 파일 로드 실패 시 기본값 설정 후 config 디렉토리 생성 시도
        print(f"설정 파일을 찾을 수 없습니다: {e}")
        default_config = {
            "connection": {
                "host": "127.0.0.1",
                "port": 12345
            },
            "ui": {
                "font": "NanumGothic",
                "font_size": 12
            }
        }
        
        # 설정 디렉토리 없는 경우 자동 생성
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

""" 연결 설정을 가져오기"""
def get_connection_config():

    config = load_config()
    connection_config = config.get("connection", {})
    
    host = connection_config.get("host", "127.0.0.1")
    port = connection_config.get("port", 12345)
    
    return {
        "host": host,
        "port": port
    }
"""UI 설정 가져오기"""
def get_ui_config():
    
    config = load_config()
    ui_config = config.get("ui", {})
    
    return {
        "font": ui_config.get("font", "NanumGothic"),
        "font_size": ui_config.get("font_size", 12)
    }
