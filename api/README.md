# StockDBWrapper Documentation

## Configure StockDBWrapper

```python
from stockdbwrapper import stockdb
```

## stockdb

```python
class stockdb(userid: Optional[str]=None, password: Optional[str]=None)
```

 stockdb must be initialized in order to establish connection to the database. A connection can be made with or without authentication (a connection without authentication will restrict certain api features)

### Initialization without authentication:
```python
stdb = stockdb()
```

### Initialization with authentication:
```python
stdb = stockdb(userid="userid",password="password")
```

```python
__init__(userid: Optional[str]=None, password: Optional[str]=None)
```
Initialize a stockdb instance

Parameters
1. userid: userid of the database
2. password: password to access the database

```python
stock_price(ticker: str, date: str, time_window: int) -> list
```
Return the day-to-day past price of a stock from a particular date going back a particular interval of time.

Parameters
1. ticker: the ticker name of the stock
2. date: most recent date in YYYY-MM-DD format, until which prices are needed
3. time_window: number of days of prices required

Note: API will only retrieve stock data until 3 months for unauthenticated users.