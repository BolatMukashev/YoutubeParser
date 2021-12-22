from youtube_parser import YoutubeVideo

# example = {'start': '00:18:26.0', 'end': '00:20:24.0', 'x_offset': 0, 'vertical': True}


if __name__ == '__main__':
    video = YoutubeVideo('https://www.youtube.com/watch?v=tzdcCa56OTw&ab_channel=varlamov')
    parts_for_cuts = [
        {'start': '00:17:03.8', 'end': '00:17:43.6', 'x_offset': 0, 'vertical': True}
    ]
    # video.cut_do_vertical_and_save(output_name='cutted_clip', times=parts_for_cuts)
    video.concatenate_clips_and_save(output_name='fin_3', ending='tyan')
