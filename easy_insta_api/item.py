from collections import defaultdict


def get_media_candidates(item):
    candidates = []
    if item['media_type'] == 1:  # PHOTO
        candidates = {'pk': item['pk'], 'id': item['id'], 'imgs': item['image_versions2']['candidates'], 'vids': None}
        # print(candidates)

    if item['media_type'] == 2:  # VIDEO
        candidates = {'pk': item['pk'], 'id': item['id'], 'imgs': item['image_versions2']['candidates'], 'vids': item['video_versions']}

    if item['media_type'] == 8:  # CAROUSEL
        for i, element in enumerate(item['carousel_media']):
            if element['media_type'] == 1:  # PHOTO
                candidates.append({'pk': item['pk'], 'id': element['id'], 'imgs': element['image_versions2']['candidates'], 'vids': None})

            if item['media_type'] == 2:  # VIDEO
                candidates.append({'pk': item['pk'], 'id': element['id'], 'imgs': element['image_versions2']['candidates'], 'vids': element['video_versions']})

    return candidates
