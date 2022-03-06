import json
import codecs
import datetime
import os.path
import logging

from easy_insta_api import api_loggin_settings as logger

log = logger.get(__name__)

try:
    from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version)
except ImportError:
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version)


def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def onlogin_callback(api, new_settings_file):
    cache_settings = api.settings
    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json)
        log.info(' SAVED: {0!s}'.format(new_settings_file))


def get(user, pw, credential_file_path):
    print(__name__)
    file_path = credential_file_path

    log.info('Instagram Private API - Client version: {0!s}'.format(client_version))

    device_id = None
    try:

        if not os.path.isfile(file_path):
            # settings file does not exist
            log.info('Unable to find file: {0!s}'.format(file_path))

            # login new
            api = Client(
                user, pw,
                on_login=lambda x: onlogin_callback(x, file_path))
        else:
            with open(file_path) as file_data:
                cached_settings = json.load(file_data, object_hook=from_json)
            log.info('Reusing settings: {0!s}'.format(file_path))

            device_id = cached_settings.get('device_id')
            # reuse auth settings
            api = Client(
                user, pw,
                settings=cached_settings)

    except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
        log.info('ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))

        # Login expired
        # Do relogin but use default ua, keys and such
        api = Client(
            user, pw,
            device_id=device_id,
            on_login=lambda x: onlogin_callback(x, file_path))

    except ClientLoginError as e:
        log.info('ClientLoginError {0!s}'.format(e))
        exit(9)
    except ClientError as e:
        log.info('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response))
        exit(9)
    except Exception as e:
        log.info('Unexpected Exception: {0!s}'.format(e))
        exit(99)

    cookie_expiry = api.cookie_jar.auth_expires
    log.info('Cookie Expiry: {0!s}'.format(
        datetime.datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ')))

    return api
