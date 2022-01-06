from youtube_parser import YoutubeVideo

# example = {'start': '00:18:26.0', 'end': '00:20:24.0', 'x_offset': 0, 'vertical': True}


if __name__ == '__main__':
    video: YoutubeVideo = YoutubeVideo('https://youtu.be/Nv-R4e7uBRQ', 'Как чиновники избавляются от пешеходов')
    parts_for_cuts = [
        {'start': '00:16:47.7', 'end': '00:17:31.2', 'x_offset': 0, 'vertical': True},
        {'start': '00:17:38.0', 'end': '00:17:44.0', 'x_offset': 0, 'vertical': True},
    ]
    # video.cut_do_vertical_and_save(times=parts_for_cuts)
    video.concatenate_clips_and_save()
