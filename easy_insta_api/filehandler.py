import os
from urllib import request
from easy_insta_api import api_loggin_settings as logger

log = logger.get(__name__)


def download_item(media_candidate, path, size='large'):
    if not os.path.exists(path):
        os.makedirs(path)

    if isinstance(media_candidate, list):
        for item in media_candidate:
            download_file(path, media_candidate, size)
    else:
        download_file(path, media_candidate, size)


def download_file(path, media_candidate, size):
    _size = {'large': 0, 'small': -1}
    print([_size.get(size)])
    download_if_not_exist(_size, media_candidate, path, size, 'imgs')

    if not media_candidate['vids'] is None:
        download_if_not_exist(_size, media_candidate, path, size, 'vids')


def download_if_not_exist(_size, media_candidate, path, size, file_type):
    filename_img = build_filename(media_candidate, _size, size, file_type)
    file_img = path / filename_img
    if not os.path.isfile(file_img):
        log.info('DOWNLOAD file: ' + filename_img)
        url = media_candidate[file_type][_size[size]: int]['url']
        request.urlretrieve(url, file_img)

    else:
        log.info('DOWNLOAD not necessary - file already exist: ' + filename_img)


def build_filename(media_candidate, _size, size, file_type):
    _file_type = {'imgs': 'jpg', 'vids': 'mp4'}
    file_name = media_candidate['id'] + '_{}x{}.{}'.format(media_candidate[file_type][_size[size]]['width'],
                                                           media_candidate[file_type][_size[size]]['height'],
                                                           _file_type[file_type])
    return file_name
