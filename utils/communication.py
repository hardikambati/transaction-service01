import json
import requests

from utils import (
    config,
)


def change_status_api_call(data: dict):
    connect_timeout, read_timeout = 5.0, 30.0
    
    response = requests.post(
        url=config.BACKEND_BASE_URL + config.WEBHOOK_PATH,
        data=json.dumps(
            data
        ),
        headers={
            'Content-Type': 'application/json',
            'MS_ACCESS_KEY': config.MS_ACCESS_KEY
        },
        timeout=(connect_timeout, read_timeout),
    )

    if response.status_code in [200, 201]:
        print('[WEBHOOK] success')
    else:
        print(f"[WEBHOOK] server responded with status code {response.status_code}")