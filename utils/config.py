import os

# env
MS_SECRET_KEY = os.environ.get('MS_SECRET_KEY')
MS_ACCESS_KEY = os.environ.get('MS_ACCESS_KEY')
MODE = os.environ.get('MODE', 'debug')
BROKER_URL = os.environ.get('BROKER_URL', 'amqp://localhost')
# BACKEND_BASE_URL = os.environ.get('BACKEND_BASE_URL')
BACKEND_BASE_URL = 'https://cc4d-2401-4900-1c16-8fff-00-53-a393.ngrok-free.app/api/'

WEBHOOK_PATH = 'webhook/update-transaction/'

# status
# format - (status, time_delay_in_sec)
STATUS = (
    ('scheduled', 5),
    ('started', 5),
    ('verifying', 5),
    ('transacting', 7),
    ('completed', 5),
    ('closed', 0),
)