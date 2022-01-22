from youtube_parser import YoutubeVideo

# example = {'start': '00:18:26.0', 'end': '00:20:24.0', 'x_offset': 0, 'vertical': True}


if __name__ == '__main__':
    video: YoutubeVideo = YoutubeVideo('https://youtu.be/9wd0Z9jaqPU')
    parts_for_cuts = [
        {'start': '00:00:02.0', 'end': '00:00:41.8', 'x_offset': 0, 'vertical': False},
    ]
    # video.cut_do_vertical_and_save(times=parts_for_cuts)
    # video.concatenate_clips_and_save()
