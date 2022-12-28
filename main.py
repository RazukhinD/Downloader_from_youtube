from pytube import YouTube

file_name=input('Введи URL видео которое надо скачать: ')



def format_resolution():
    while True:
        try:
            reso = int(input('Выбери качество скачиваемоего видео: 1-360р, 2-720р60, 3-1080р60'))
            match reso:
                case 1:
                    return '360p'
                case 2:
                    return '720p'
                case 3:
                    return '1080p'
                case _:
                    print('Выбери один из параметров')
                    continue
        except:
            print('Введите число от 1 до 3')
reso=format_resolution()

yt_video = YouTube(file_name)

yt_video.streams.filter(resolution=reso,file_extension='mp4').first().download('new.mp4')
