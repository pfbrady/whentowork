import requests
import requests.packages
import logging
from json import JSONDecodeError
import settings
from whentowork.models import Result
from exceptions.w2w_bad_request import W2WBadRequestException
from typing import List, Dict


class RestAdapter:
    def __init__(self, hostname: str, api_key: str, ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Constructor for RestAdapter

        :param hostname: WhenToWork Host
        :param api_key: API key provided by W2W, used for authentication
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: If your app has a logger, pass it in here.
        """
        self.url = f"https://{hostname}/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()
        self._logger = logger or logging.getLogger(__name__)

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None) -> Result:
        full_url = self.url + endpoint
        ep_params.update({'key': self._api_key})
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify,
                                        params=ep_params)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise W2WBadRequestException("Request failed") from e
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError, requests.exceptions.JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise W2WBadRequestException("Bad JSON in response") from e
        is_success = 299 >= response.status_code >= 200  # 200 to 299 is OK
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:  # OK
            self._logger.debug(msg=log_line)
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=log_line)
        raise W2WBadRequestException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)
