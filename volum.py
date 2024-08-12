from pydub import AudioSegment

def adjust_volume(input_file, output_file, change_in_dB):
    # 오디오 파일 불러오기
    audio = AudioSegment.from_file(input_file)
    
    # 볼륨 조절
    adjusted_audio = audio + change_in_dB
    
    # 새로운 파일로 저장
    adjusted_audio.export(output_file, format='mp3')

# 입력 파일과 출력 파일 경로, 그리고 볼륨 변경 값(dB)을 설정
input_file = "감성 트로트 모음  KPOP.mp3"
output_file = "감성 트로트 모음  KPOP.mp3"
change_in_dB = 10  # 볼륨을 5dB 증가시킴

# 볼륨 조절 함수 호출
adjust_volume(input_file, output_file, change_in_dB)
