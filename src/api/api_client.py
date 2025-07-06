import requests
from requests import Response
import logging
logger = logging.getLogger("APIClient")

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def post(self, payload: dict) -> Response:
        url = self.base_url
        logger.info(f"POST {url} | Payload: {payload}")
        response = requests.post(f"{url}", json=payload)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            logger.error(f"HTTPError: {e} | Response: {response.text}")
            raise
        logger.info(f"Response: {response.status_code} | Body: {response.text}")
        return response

    def get(self, object_id: str) -> Response:
        url = f"{self.base_url}/{object_id}"
        logger.info(f"GET {url}")
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            logger.error(f"HTTPError: {e} | Response: {response.text}")
            raise
        logger.info(f"Response: {response.status_code} | Body: {response.text}")
        return response

    def put(self, object_id: str, payload: dict) -> requests.Response:
        url = f"{self.base_url}/{object_id}"
        logger.info(f"PUT {url} | Payload: {payload}")
        response = requests.put(url, json=payload)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            logger.error(f"HTTPError: {e} | Response: {response.text}")
            raise
        logger.info(f"Response: {response.status_code} | Body: {response.text}")
        return response

    def delete(self, object_id: str) -> Response:
        url = f"{self.base_url}/{object_id}"
        logger.info(f"DELETE {url}")
        response = requests.delete(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            logger.error(f"HTTPError: {e} | Response: {response.text}")
            raise
        logger.info(f"Response: {response.status_code}")
        return response