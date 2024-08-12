import os
from pydub import AudioSegment
import numpy as np

def calculate_db(input_file):
    # 오디오 파일 불러오기
    audio = AudioSegment.from_file(input_file)
    
    # 오디오 데이터를 numpy 배열로 변환
    samples = np.array(audio.get_array_of_samples())

    # RMS 계산
    rms = np.sqrt(np.mean(samples**2))

    # 데시벨로 변환
    db = 20 * np.log10(rms)
    
    return db

def calculate_db_for_all_mp3_files(directory):
    results = {}
    # 디렉토리 내의 모든 파일 탐색
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            filepath = os.path.join(directory, filename)
            try:
                db_level = calculate_db(filepath)
                results[filename] = db_level
            except Exception as e:
                results[filename] = f"Error: {e}"
    return results

# 현재 디렉토리 설정
current_directory = "."

# 모든 MP3 파일의 데시벨 계산 함수 호출
db_levels = calculate_db_for_all_mp3_files(current_directory)

# 결과 출력
for filename, db in db_levels.items():
    print(f"{filename}: {db} dB")
