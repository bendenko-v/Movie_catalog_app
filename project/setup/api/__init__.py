from flask_restx import Api

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Movie catalog App",
    description='Movies catalog REST API backend',
    doc="/docs",
)
