import requests
from django.conf import settings


def remove_bg(file_path):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg'
        ,
        files={'image_file': open(settings.MEDIA_ROOT + file_path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'kymktHC8MLgrLRx9nbGyzYE9'},
    )
    if response.status_code == requests.codes.ok:
        with open(settings.MEDIA_ROOT + file_path, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)