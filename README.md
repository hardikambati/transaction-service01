# Transaction System | Microservice 01
`v1.x.x`

## Description

This microservice imitates to process data.
`processing` can be :
- a heavy computation task
- processing done on other microservice
<br></br>

## Prerequisites
- Create a file `.env`, and add the following in it
    ```
    MS_SECRET_KEY = '<found_in_backend_database>'
    MS_ACCESS_KEY = '<found_in_backend_database>'
    MODE = 'debug'
    BROKER_URL = 'amqp://rabbitmq'
    BACKEND_BASE_URL = 'http://localhost:8000/api/'
    ```
- Make sure the [backend](https://github.com/hardikambati/transaction-backend?tab=readme-ov-file) server is up and running.
<br></br>

## Spinning up the microservice using Docker
1. Run the following command.
    ```
    docker-compose up --build
    ```
2. It will connect to `main_realtime-transaction-nextwork` network bridge, that was created in the backend's docker container.
<br></br>

## Functioning
- Altogether, there are 7 processing states.

    ```txt
    (task_name, time_in_sec)

    ('scheduled'   , 5)
    ('started'     , 2)
    ('verifying'   , 3)
    ('transacting' , 5)
    ('completed'   , 2)
    ('closed'      , 0)
    ('failed'      , 0)
    ```

- The microservice listens to a queue.
- Once a transaction is created in the backend, and a message is pushed to the queue, the microservice reads and validates the data.
- It runs the above processes, and consumes variable amount of time (as specified).
- After each process is completed, it sends a webhook message to backend.
- Incase of failure, it will send an error message with the exception.
<br></br>
