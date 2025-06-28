# 1. 베이스 이미지 선택
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
# 컨테이너 안에서 코드가 위치할 경로를 지정
WORKDIR /app

# 3. 의존성 설치
# requirements.txt를 먼저 복사하여 패키지를 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
# 현재 폴더(server/)의 모든 파일을 컨테이너의 /app 폴더로 복사
COPY . .

# 5. 서버 실행 명령어
CMD ["python3", "main.py"]
