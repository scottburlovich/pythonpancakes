import unittest
from src.pythonpancakes import PancakeSwapAPI


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.ps = PancakeSwapAPI()

    def test_summary(self):
        """Verify that valid data is returned from the summary() request"""
        response = self.ps.summary()
        self.assertIn('updated_at', response.keys())
        self.assertIn('data', response.keys())

    def test_tokens_without_address(self):
        """Verify that valid data is returned from the tokens() request when called without an address parameter"""
        response = self.ps.tokens()
        self.assertIn('updated_at', response.keys())
        self.assertIn('data', response.keys())

    def test_tokens_with_address(self):
        """Verify that valid data is returned from the tokens() request when called with an address parameter"""
        # Use pancakeswap-token (CAKE) for test
        token = "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
        response = self.ps.tokens(token)
        self.assertIn('updated_at', response.keys())
        self.assertIn('data', response.keys())
        self.assertEqual(response['data']['name'], "PancakeSwap Token")
        self.assertEqual(response['data']['symbol'], "Cake")

    def test_pairs(self):
        """Verify that valid data is returned from the pairs() request"""
        response = self.ps.pairs()
        self.assertIn('updated_at', response.keys())
        self.assertIn('data', response.keys())


if __name__ == '__main__':
    unittest.main()
