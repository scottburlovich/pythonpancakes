# 🐍 Python Pancakes 🥞
A simple request wrapper for the Pancake-Swap API.

## Installation
Install package 
```bash
# Using pip
$ pip install pythonpancakes

# Or from source
$ git clone https://github.com/scottburlovich/pythonpancakes.git pythonpancakes
$ cd pythonpancakes
$ python3 setup.py install
```

Import module into your project and initialize API class
```python
from pythonpancakes import PancakeSwapAPI
ps = PancakeSwapAPI()
```

## Usage
Please note, the API functionality currently exposed by PancakeSwap is quite basic. This package will be updated 
as they add new functionality.

## `summary()`
Returns a dictionary containing data for the top ~1000 PancakeSwap pairs, sorted by reserves.

Example invocation:
```python
summary = ps.summary()
```
Example output:
```python
# output:
{
  "updated_at": 1234567,              // UNIX timestamp
  "data": {
    "0x..._0x...": {                  // BEP20 token addresses, joined by an underscore
      "price": "...",                 // price denominated in token1/token0
      "base_volume": "...",           // last 24h volume denominated in token0
      "quote_volume": "...",          // last 24h volume denominated in token1
      "liquidity": "...",             // liquidity denominated in USD
      "liquidity_BNB": "..."          // liquidity denominated in BNB
    },
    // ...
  }
}
```
---
## `tokens(address)`
If address parameter is specified, returns the token information, based on address. Otherwise, 
returns the tokens in the top ~1000 pairs on PancakeSwap, sorted by reserves.

Example invocation without address:
```python
tokens = ps.tokens()
```
Example output without address:
```python
{
  "updated_at": 1234567,              // UNIX timestamp
  "data": {
    "0x...": {                        // the address of the BEP20 token
      "name": "...",                  // not necessarily included for BEP20 tokens
      "symbol": "...",                // not necessarily included for BEP20 tokens
      "price": "...",                 // price denominated in USD
      "price_BNB": "...",             // price denominated in BNB
    },
    // ...
  }
}
```
Example invocation with address:
```python
token = ps.tokens('0x00000000000...')
```
Example output with address:
```python
# output
{
  "updated_at": 1234567,              // UNIX timestamp
  "data": {
    "name": "...",                    // not necessarily included for BEP20 tokens
    "symbol": "...",                  // not necessarily included for BEP20 tokens
    "price": "...",                   // price denominated in USD
    "price_BNB": "...",               // price denominated in BNB
  }
}
```
---
## `pairs()`
Returns data for the top ~1000 PancakeSwap pairs, sorted by reserves.

Example invocation:
```python
pairs = ps.pairs()
```
Example output
```python
{
  "updated_at": 1234567,              // UNIX timestamp
  "data": {
    "0x..._0x...": {                  // the asset ids of BNB and BEP20 tokens, joined by an underscore
      "pair_address": "0x...",        // pair address
      "base_name": "...",             // token0 name
      "base_symbol": "...",           // token0 symbol
      "base_address": "0x...",        // token0 address
      "quote_name": "...",            // token1 name
      "quote_symbol": "...",          // token1 symbol
      "quote_address": "0x...",       // token1 address
      "price": "...",                 // price denominated in token1/token0
      "base_volume": "...",           // volume denominated in token0
      "quote_volume": "...",          // volume denominated in token1
      "liquidity": "...",             // liquidity denominated in USD
      "liquidity_BNB": "..."          // liquidity denominated in BNB
    },
    // ...
  }
}
```
