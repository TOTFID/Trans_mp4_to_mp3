import moviepy.editor


def get_video(video_path='video', file_audio='file.mp3'):
   ed_video = moviepy.editor.VideoFileClip(video_path)
   audio = ed_video.audio
   audio.write_audiofile(file_audio)