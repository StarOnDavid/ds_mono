import datetime


def filter_duration(video_list, min_duration=None, max_duration=None):
    def duration_longer(vid_duration):
        min_d = datetime.strptime(min_duration + ':00', '%M:%S')
        vid_d = datetime.strptime(vid_duration, '%M:%S')
        return vid_d > min_d

    def duration_shorter(vid_duration):
        max_d = datetime.strptime(max_duration + ':00', '%M:%S')
        vid_d = datetime.strptime(vid_duration, '%M:%S')
        return vid_d < max_d

    if min_duration:
        video_list = [v for v in video_list if duration_longer(v['video']['duration'])]
    if max_duration:
        video_list = [v for v in video_list if duration_shorter(v['video']['duration'])]
    return video_list


def filter_free_premium(video_list):
    return [v for v in video_list if v['free_premium'] is True]
