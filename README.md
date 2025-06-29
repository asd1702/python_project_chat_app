# Python 채팅 애플리케이션

본 프로젝트는 Python으로 제작된 클라이언트-서버 채팅 애플리케이션입니다.

## 주요 기능

*   GUI 기반의 채팅 클라이언트
*   멀티스레드를 이용한 다중 사용자 동시 접속 지원
*   채팅 내용 파일 로깅으로 관리

## 실행 방법

### 요구사항

*   Docker (서버 실행용)
*   Python 3.10.12 (클라이언트 실행용)

### 1. Docker 설치

#### Linux (Ubuntu/Debian)
```bash
# 필요한 패키지 설치
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Docker 공식 GPG 키 추가
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Docker 저장소 추가
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Docker 설치
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

# 사용자를 docker 그룹에 추가 (sudo 없이 실행 가능)
sudo usermod -aG docker ${USER}
# 변경사항을 적용하기 위해 로그아웃 후 다시 로그인
```

#### Windows
1. [Docker Desktop](https://www.docker.com/products/docker-desktop)을 다운로드하여 설치
2. 설치 후 Docker Desktop 애플리케이션을 실행

### 2. 서버 실행 (Docker 사용)

Docker Hub에서 이미지를 다운로드하고 실행합니다:

```bash
# Linux
sudo docker run -it -p 12345:12345 asd1702/python_project_chat_app:latest

# Windows (PowerShell)
docker run -it -p 12345:12345 asd1702/python_project_chat_app:latest
```

서버가 `0.0.0.0:12345`에서 실행되며, 다른 클라이언트의 접속을 기다립니다.

### 3. 클라이언트 실행

서버가 실행된 상태에서, **별도의 터미널**을 열고 다음 명령어를 실행하여 클라이언트를 시작합니다.

```bash
python3 -m client.index
```

GUI 창이 나타나면 닉네임을 입력하고 채팅을 시작할 수 있습니다.

> **참고:** 클라이언트의 `client/config/config.json` 파일에서 서버 접속 주소(`host`)를 변경할 수 있습니다. 현재는 `127.0.0.1`로 설정되어 있습니다.

### 4. 종료 방법

*   **서버:** Docker 컨테이너 실행 터미널에서 `Ctrl + C`를 누릅니다.
*   **클라이언트:** GUI 창을 닫습니다.

## 프로젝트 구조

```
.
├── client/                      # 클라이언트 애플리케이션
│   ├── config/                  # 클라이언트 설정 (서버 주소, UI 등)
│   ├── connection/              # 서버 연결 및 통신 관리
│   ├── ui/                      # GUI 관련 모듈
│   ├── utils                    # 서버 접속 주소 관리
│   └── index.py                 # 클라이언트 실행 파일   
|  
├── server/                      # 서버 애플리케이션
│   ├── config/                  # 서버 설정 (포트, 최대 연결 수 등)
│   ├── core/                    # 클라이언트 연결 및 데이터 처리
│   ├── logs/                    # 채팅 로그 저장 디렉토리
│   ├── utils/                   # 로깅, 설정 관리 등 유틸리티 모듈
│   ├── Dockerfile               # 서버용 Docker 이미지 설정
│   └── main.py                  # 서버 실행 파일
│
├── docker-compose.yml           # Docker Compose 설정 파일
└── README.md                    # 프로젝트 설명서
```