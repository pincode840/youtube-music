# 모듈 설치: !pip install moviepy
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_file_path, audio_file_path):
    # mp4 등 비디오 파일 불러오기
    video = VideoFileClip(video_file_path)
    
    # 오디오를 추출하여 mp3 파일로 저장
    video.audio.write_audiofile(audio_file_path)

video_file = '신나는 신나는 트로트  KPOP [ TROT ]  PLAYLIST🎶( 꽃길상사화여인의 눈물회룡포바람길).mp4'  # 변환하고 싶은 비디오 파일의 경로
audio_file = '신나는 신나는 트로트  KPOP.mp3'  # 저장할 오디오 파일의 경로, 이름 지정

extract_audio_from_video(video_file, audio_file)