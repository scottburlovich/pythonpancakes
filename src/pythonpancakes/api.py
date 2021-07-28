import json
import re
import requests


class PancakeSwapAPI:
    __BASE_URL = "https://api.pancakeswap.info/api/v2/"

    """
    Basic API request wrapper for PancakeSwap
    Scott Burlovich (github.com/scottburlovich)
    Last Update: Jul 28, 2021
    """

    def __init__(self, base_url=__BASE_URL):
        self.base_url = base_url
        self.request_timeout = 60

    def __get(self, request_url: str):
        """
        GET request wrapper
        :param request_url: str
        """
        with requests.Session() as session:
            response = session.get(request_url, timeout=self.request_timeout)
            response.raise_for_status()
            return json.loads(response.content.decode('utf-8'))

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
            # Trim any whitespace from address
            address = address.replace(' ', '')
            # Validate provided address matches ERC20 format - does not check if the address is valid on chain!
            if not re.match("^0x([A-Fa-f0-9]{40})$", address):
                raise ValueError(f"Provided address hash ({address}) is not in a valid format.")

        url = f"{self.base_url}tokens{'/' + address if address is not None else ''}"
        return self.__get(url)

    def pairs(self):
        """
        Returns data for the top ~1000 PancakeSwap pairs, sorted by reserves.
        :return: Dict
        """
        url = f"{self.base_url}pairs"
        return self.__get(url)
