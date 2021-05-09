import json
import re
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class PancakeSwapAPI:
    __BASE_URL = "https://api.pancakeswap.info/api/v2/"
    """
    Basic API request wrapper for PancakeSwap
    Scott Burlovich (github.com/scottburlovich)
    Last Update: May 9, 2021
    """

    def __init__(self, base_url=__BASE_URL):
        self.base_url = base_url
        self.request_timeout = 60
        self.session = requests.session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def __exit__(self):
        self.session.close()

    def __get(self, request_url: str):
        """
        GET request wrapper
        :param request_url: str
        """
        try:
            response = self.session.get(request_url, timeout=self.request_timeout)
        except requests.exceptions.RequestException:
            raise

        try:
            response.raise_for_status()
            return json.loads(response.content.decode('utf-8'))
        except Exception as err:
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise ValueError(content)
            except json.decoder.JSONDecodeError:
                pass
            raise

    def summary(self):
        """
        Returns data for the top ~1000 PancakeSwap pairs, sorted by reserves.
        :return: Dict
        """
        url = f"{self.base_url}summary"
        return self.__get(url)

    def tokens(self, address: str = None):
        """
        If address parameter is specified, returns the token information, based on address.
        Otherwise, returns the tokens in the top ~1000 pairs on PancakeSwap, sorted by reserves.
        :type address: str
        :return: Dict
        """
        if address:
            try:
                # Trim any whitespace from address
                address = address.replace(' ', '')
                # Validate provided address matches ERC20 format - does not check if the address is valid on chain!
                if not re.match("^0x([A-Fa-f0-9]{40})$", address):
                    raise ValueError(address)
            except ValueError:
                return "Provided address hash is not in a valid format"

        url = f"{self.base_url}tokens{'/' + address if address is not None else ''}"
        return self.__get(url)

    def pairs(self):
        """
        Returns data for the top ~1000 PancakeSwap pairs, sorted by reserves.
        :return: Dict
        """
        url = f"{self.base_url}pairs"
        return self.__get(url)
