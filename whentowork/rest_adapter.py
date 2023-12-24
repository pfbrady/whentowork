import requests
import requests.packages
from json import JSONDecodeError
import settings
from whentowork.models import Result
from exceptions.w2w_bad_request import W2WBadRequestException
from typing import List, Dict


class RestAdapter:
    def __init__(self, hostname: str, api_key: str, ssl_verify: bool = True):
        self.url = f"https://{hostname}/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        full_url = self.url + endpoint
        headers = {'w2w-api-key': self._api_key}
        try:
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify,
                                        headers=headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            raise W2WBadRequestException("Request failed") from e
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError, requests.exceptions.JSONDecodeError) as e:
            raise W2WBadRequestException("Bad JSON in response") from e
        if 200 <= response.status_code <= 299:  # OK
            return Result(response.status_code, message=response.reason, data=data_out)
        raise W2WBadRequestException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)


a = RestAdapter(hostname='www3.whentowork.com/cgi-bin/w2wC4.dll', api_key=settings.W2W_TOKEN)

print(a.get(endpoint='/api/AssignedShiftList', ep_params={'start_date': '12/23/2023', 'end_date': '12/23/2023'}))
