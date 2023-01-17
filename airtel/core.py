import requests
import json
from os import environ as env


from dotenv import load_dotenv

load_dotenv()


class Airtel:
    def __init__(
        self,
        production: bool = False,
        client_id: str = env.get("AIRTEL_CLIENT_ID"),
        client_secret: str = env.get("AIRTEL_CLIENT_SECRET"),
    ) -> None:
        self.url = (
            "https://openapi.airtel.africa/"
            if production
            else "https://openapiuat.airtel.africa/"
        )

    @property
    def token(self):
        """Get the token from the routes of the API"""
