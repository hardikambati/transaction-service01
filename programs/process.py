import time
from datetime import datetime

from utils.communication import (
    change_status_api_call,
)
from utils import (
    config,
)


def core_process(body: dict):
    
    for item in config.STATUS:

        try:
            tag = item[0]
            seconds = item[1]

            print(f'[{tag}] approx {seconds} seconds...')
            time.sleep(seconds)
            print(f'[{tag}] done')

            # make api call to update status
            body['payload']['extra_data'].update(
                {'status': tag}
            )
            
            change_status_api_call(data=body)
    
        except Exception as e:        
            # make api call to send error message
            body['payload']['extra_data'].update(
                {
                    'status': tag,
                    'log': {
                        'status': tag,
                        'error': str(e),
                        'timestamp': str(datetime.now())
                    }
                }
            )
    
            change_status_api_call(data=body)
            print('[CORE PROCESS] stopping process...')
            break