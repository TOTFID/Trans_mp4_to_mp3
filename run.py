from main import get_video
from pathlib import Path


def main():
   enter_video_path = str(input('Choose video: '))
   video = f'videos/{enter_video_path}'
   check_path = Path(video)
   
   if check_path.exists():
      print('File exists')
   else: raise FileNotFoundError
   
	
   
   enter_name_audio = str(input('\nName for audio file: '))
   results_path = f'results/{enter_name_audio}'
   
   if '.mp3' in enter_name_audio:
      print('Name is correct')
   else: raise NameError
   
   
   get_video(video_path=video, file_audio=results_path)
   
   
if __name__=='__main__':
   main()
