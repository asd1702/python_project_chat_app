FROM python:3.9-slim

# 작업 디렉토리 설정
# 컨테이너 안에서 코드가 위치할 경로를 지정
WORKDIR /app

#한글 폰트 패키지 설치
RUN apt-get update && apt-get install -y \
    fonts-nanum \
    fonts-noto-cjk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
# 현재 폴더(server/)의 모든 파일을 컨테이너의 /app 폴더로 복사
COPY . .

# 서버 실행 명령어
CMD ["python3", "main.py"]
