from fastapi import FastAPI

def create_app() -> FastAPI:
    return FastAPI(
        title='Example chat with Kafka',
        docs_url='/api/docs',
        description='Chat with Kafka',
        debug=True,
    )

