# Colombo Stock Exchange API - User Documentation

**Version:** CSE=V1.0

Welcome to the Colombo Stock Exchange API documentation. This guide will help you understand and use all available endpoints to access real-time market data, company information, and announcements from the Colombo Stock Exchange.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Base URL](#base-url)
3. [API Endpoints](#api-endpoints)
   - [Health Check](#health-check)
   - [Company Information](#company-information)
   - [Market Data](#market-data)
   - [Market Indices](#market-indices)
   - [Market Summary](#market-summary)
   - [Sectors](#sectors)
   - [Announcements](#announcements)
4. [Response Format](#response-format)
5. [Error Handling](#error-handling)
6. [Examples](#examples)

## Getting Started

### Base URL

If running locally:
```
http://localhost:8000
```

If deployed:
```
https://your-domain.com
```

### Interactive Documentation

Once the API is running, you can access interactive documentation at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Health Check

#### Check API Health Status

**Endpoint:** `GET /health`

**Description:** Verify that the API is running and accessible.

**Request:**
```bash
GET http://localhost:8000/health
```

**Response:**
```json
{
  "status": "ok"
}
```

---

### Company Information

#### Get Company Information

**Endpoint:** `GET /company-info`

**Description:** Retrieve detailed information about a specific company including prices, volumes, market capitalization, and historical data.

**Parameters:**
- `symbol` (required, query parameter): Company stock symbol
  - Example: `JKH.N0000`, `COMB.N0000`, `HNB.N0000`

**Request:**
```bash
GET http://localhost:8000/company-info?symbol=JKH.N0000
```

**Response Fields:**
- `symbol`: Stock symbol
- `name`: Company name
- `isin`: International Securities Identification Number
- `issue_date`: Date when shares were issued
- `par_value`: Par value of the stock
- `price`: Price information (last_traded, previous_close, change, change_percentage, high, low, closing_price)
- `volume`: Volume information (today_share_volume, today_trade_count, today_turnover)
- `market_cap`: Market capitalization (value, market_percentage)
- `high_low`: High and low prices (week_52_high, week_52_low, all_time_high, all_time_low)
- `logo`: Company logo path

**Example Response:**
```json
{
  "symbol": "JKH.N0000",
  "name": "JOHN KEELLS HOLDINGS PLC",
  "isin": "LK0092N00003",
  "issue_date": "23/OCT/1986",
  "par_value": 1.0,
  "price": {
    "last_traded": 21.2,
    "previous_close": 21.0,
    "change": 0.2,
    "change_percentage": 0.95,
    "high": 21.5,
    "low": 21.0,
    "closing_price": 21.2
  },
  "volume": {
    "today_share_volume": 6155799,
    "today_trade_count": 471,
    "today_turnover": 130655544.0
  },
  "market_cap": {
    "value": 374992441430.8,
    "market_percentage": 4.73
  },
  "high_low": {
    "week_52_high": 26.1,
    "week_52_low": 18.3,
    "all_time_high": 430.25,
    "all_time_low": 8.75
  },
  "logo": {
    "path": "upload_logo/508_1601461779.jpeg"
  }
}
```

---

### Market Data

#### Get Trade Summary

**Endpoint:** `GET /trade-summary`

**Description:** Get a comprehensive summary of all trades for all companies listed on the exchange.

**Request:**
```bash
GET http://localhost:8000/trade-summary
```

**Response:** Returns a list of trade summary items for all companies.

**Response Fields (per item):**
- `symbol`: Stock symbol
- `name`: Company name
- `price`: Current price
- `previous_close`: Previous closing price
- `change`: Price change
- `change_percentage`: Percentage change
- `high`: Highest price
- `low`: Lowest price
- `closing_price`: Closing price
- `turnover`: Total turnover
- `share_volume`: Share volume
- `trade_volume`: Trade volume
- `market_cap`: Market capitalization

---

#### Get Today's Share Price

**Endpoint:** `GET /today-share-price`

**Description:** Retrieve today's share prices for all companies.

**Request:**
```bash
GET http://localhost:8000/today-share-price
```

**Response Fields (per item):**
- `symbol`: Stock symbol
- `open`: Opening price
- `high`: Highest price
- `low`: Lowest price
- `last_traded`: Last traded price
- `change`: Price change
- `change_percentage`: Percentage change
- `crossing_volume`: Crossing volume
- `quantity`: Quantity

---

#### Get Top Gainers

**Endpoint:** `GET /top-gainers`

**Description:** Get a list of stocks with the highest percentage gains for the day.

**Request:**
```bash
GET http://localhost:8000/top-gainers
```

**Response Fields (per item):**
- `symbol`: Stock symbol
- `price`: Current price
- `change`: Price change
- `change_percentage`: Percentage change
- `trade_date`: Trade date timestamp

---

#### Get Top Losers

**Endpoint:** `GET /top-losers`

**Description:** Get a list of stocks with the highest percentage losses for the day.

**Request:**
```bash
GET http://localhost:8000/top-losers
```

**Response Fields (per item):**
- `symbol`: Stock symbol
- `price`: Current price
- `change`: Price change
- `change_percentage`: Percentage change
- `trade_date`: Trade date timestamp

---

#### Get Most Active Trades

**Endpoint:** `GET /most-active-trades`

**Description:** Retrieve information about the most actively traded stocks.

**Request:**
```bash
GET http://localhost:8000/most-active-trades
```

**Response Fields (per item):**
- `symbol`: Stock symbol
- `trade_volume`: Trade volume
- `share_volume`: Share volume
- `turnover`: Total turnover
- `percentage_share_volume`: Percentage of share volume

---

#### Get Detailed Trades

**Endpoint:** `GET /detailed-trades`

**Description:** Get detailed trade information for all companies.

**Request:**
```bash
GET http://localhost:8000/detailed-trades
```

**Response Fields (per item):**
- `symbol`: Stock symbol
- `name`: Company name
- `price`: Current price
- `quantity`: Quantity traded
- `trades`: Number of trades
- `change`: Price change
- `change_percentage`: Percentage change

---

### Market Indices

#### Get ASPI Index Data

**Endpoint:** `GET /index/aspi`

**Description:** Retrieve All Share Price Index (ASPI) data, which represents the overall performance of the stock market.

**Request:**
```bash
GET http://localhost:8000/index/aspi
```

**Response Fields:**
- `value`: Current index value
- `low`: Lowest value
- `high`: Highest value
- `change`: Change in index value
- `percentage`: Percentage change
- `timestamp`: Timestamp of the data

**Example Response:**
```json
{
  "value": 12345.67,
  "low": 12200.00,
  "high": 12400.00,
  "change": 145.67,
  "percentage": 1.19,
  "timestamp": 1765530000000
}
```

---

#### Get S&P 20 Index Data

**Endpoint:** `GET /index/snp20`

**Description:** Retrieve S&P Sri Lanka 20 Index data, which tracks the performance of the top 20 companies.

**Request:**
```bash
GET http://localhost:8000/index/snp20
```

**Response Fields:**
- `value`: Current index value
- `low`: Lowest value
- `high`: Highest value
- `change`: Change in index value
- `percentage`: Percentage change
- `timestamp`: Timestamp of the data

---

### Market Summary

#### Get Market Status

**Endpoint:** `GET /market-status`

**Description:** Get the current status of the market (open/closed, trading hours, etc.).

**Request:**
```bash
GET http://localhost:8000/market-status
```

**Response:** Returns market status information.

---

#### Get Market Summary

**Endpoint:** `GET /market-summary`

**Description:** Get a summary of market activity including trade volume and share volume.

**Request:**
```bash
GET http://localhost:8000/market-summary
```

**Response Fields:**
- `trade_volume`: Total trade volume
- `share_volume`: Total share volume
- `trade_date`: Trade date

---

#### Get Daily Market Summary

**Endpoint:** `GET /daily-market-summary`

**Description:** Retrieve comprehensive daily market summary including market capitalization, indices, and key ratios.

**Request:**
```bash
GET http://localhost:8000/daily-market-summary
```

**Response Fields:**
- `trade_date`: Trade date
- `market_turnover`: Total market turnover
- `market_trades`: Total number of trades
- `market_cap`: Market capitalization
- `asi`: All Share Index value
- `s_and_p_20`: S&P 20 Index value
- `per`: Price to Earnings Ratio
- `pbv`: Price to Book Value
- `dy`: Dividend Yield

---

### Sectors

#### Get All Sectors

**Endpoint:** `GET /sectors`

**Description:** Retrieve information about all market sectors with their performance metrics.

**Request:**
```bash
GET http://localhost:8000/sectors
```

**Response Fields (per sector):**
- `name`: Sector name
- `index_value`: Sector index value
- `change`: Change in index value
- `percentage`: Percentage change
- `turnover`: Sector turnover
- `volume`: Sector volume

---

### Announcements

#### Get New Listings Related Announcements

**Endpoint:** `GET /announcements/new-listings`

**Description:** Retrieve announcements related to new listings on the exchange.

**Request:**
```bash
GET http://localhost:8000/announcements/new-listings
```

**Response Fields (per announcement):**
- `announcement_id`: Unique announcement ID
- `created_date`: Date when announcement was created
- `category`: Announcement category
- `company`: Company name
- `title`: Announcement title
- `remarks`: Announcement details/remarks
- `file_path`: Path to announcement file (if available)

---

#### Get Buy-In Board Announcements

**Endpoint:** `GET /announcements/buy-in-board`

**Description:** Get announcements related to buy-in board activities.

**Request:**
```bash
GET http://localhost:8000/announcements/buy-in-board
```

---

#### Get Approved Announcements

**Endpoint:** `GET /announcements/approved`

**Description:** Retrieve all approved announcements from listed companies.

**Request:**
```bash
GET http://localhost:8000/announcements/approved
```

---

#### Get Financial Announcements

**Endpoint:** `GET /announcements/financial`

**Description:** Get financial announcements including financial results, reports, and disclosures.

**Request:**
```bash
GET http://localhost:8000/announcements/financial
```

---

#### Get Circular Announcements

**Endpoint:** `GET /announcements/circular`

**Description:** Retrieve circular announcements from the exchange.

**Request:**
```bash
GET http://localhost:8000/announcements/circular
```

---

#### Get Directive Announcements

**Endpoint:** `GET /announcements/directive`

**Description:** Get directive announcements issued by the exchange.

**Request:**
```bash
GET http://localhost:8000/announcements/directive
```

---

#### Get Non-Compliance Announcements

**Endpoint:** `GET /announcements/non-compliance`

**Description:** Retrieve announcements related to non-compliance issues.

**Request:**
```bash
GET http://localhost:8000/announcements/non-compliance
```

---

## Response Format

All endpoints return JSON responses. The API uses structured data models to ensure consistent response formats.

### Success Response

All successful requests return HTTP status code `200 OK` with a JSON body containing the requested data.

### List Responses

Endpoints that return multiple items will have the following structure:
```json
{
  "items": [
    {
      // Item 1 data
    },
    {
      // Item 2 data
    }
  ]
}
```

### Single Object Responses

Endpoints that return a single object will return the object directly:
```json
{
  "field1": "value1",
  "field2": "value2"
}
```

## Error Handling

The API uses standard HTTP status codes to indicate the result of a request:

### Status Codes

- **200 OK**: Request was successful
- **404 Not Found**: The requested resource was not found
  - Example: Company symbol doesn't exist
- **502 Bad Gateway**: The CSE API is not reachable or returned an error

### Error Response Format

When an error occurs, the API returns a JSON object with an error message:

```json
{
  "detail": "Error message description"
}
```

### Common Error Scenarios

1. **Company Not Found**
   ```json
   {
     "detail": "Company not found"
   }
   ```
   - **Status Code:** 404
   - **Cause:** Invalid or non-existent stock symbol

2. **CSE API Not Reachable**
   ```json
   {
     "detail": "CSE API not reachable"
   }
   ```
   - **Status Code:** 502
   - **Cause:** Connection issue with the Colombo Stock Exchange API

3. **Resource Not Found**
   ```json
   {
     "detail": "Resource not found"
   }
   ```
   - **Status Code:** 404
   - **Cause:** Requested data is not available

## Examples

### Example 1: Get Company Information

**Request:**
```bash
curl "http://localhost:8000/company-info?symbol=JKH.N0000"
```

**Response:**
```json
{
  "symbol": "JKH.N0000",
  "name": "JOHN KEELLS HOLDINGS PLC",
  "price": {
    "last_traded": 21.2,
    "previous_close": 21.0,
    "change": 0.2,
    "change_percentage": 0.95
  }
}
```

### Example 2: Get Top Gainers

**Request:**
```bash
curl "http://localhost:8000/top-gainers"
```

**Response:**
```json
{
  "gainers": [
    {
      "symbol": "ASPH.N0000",
      "price": 0.5,
      "change": 0.1,
      "change_percentage": 25.0,
      "trade_date": 1765530063000
    }
  ]
}
```

### Example 3: Get Market Summary

**Request:**
```bash
curl "http://localhost:8000/market-summary"
```

**Response:**
```json
{
  "trade_volume": 12345,
  "share_volume": 67890,
  "trade_date": "2025-01-12"
}
```

### Example 4: Get ASPI Index

**Request:**
```bash
curl "http://localhost:8000/index/aspi"
```

**Response:**
```json
{
  "value": 12345.67,
  "low": 12200.00,
  "high": 12400.00,
  "change": 145.67,
  "percentage": 1.19,
  "timestamp": 1765530000000
}
```

### Example 5: Get Financial Announcements

**Request:**
```bash
curl "http://localhost:8000/announcements/financial"
```

**Response:**
```json
{
  "announcements": [
    {
      "announcement_id": 34836,
      "created_date": "12 Dec 2025",
      "category": "FINANCIAL",
      "company": "ABC COMPANY PLC",
      "title": "Quarterly Results",
      "remarks": "Financial results for Q3 2025",
      "file_path": "path/to/file.pdf"
    }
  ]
}
```

## Using the API

### With cURL

All endpoints can be accessed using cURL:

```bash
# Get company info
curl "http://localhost:8000/company-info?symbol=JKH.N0000"

# Get top gainers
curl "http://localhost:8000/top-gainers"

# Get market summary
curl "http://localhost:8000/market-summary"
```

### With JavaScript (Fetch API)

```javascript
// Get company information
fetch('http://localhost:8000/company-info?symbol=JKH.N0000')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// Get top gainers
fetch('http://localhost:8000/top-gainers')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### With Python (requests library)

```python
import requests

# Get company information
response = requests.get('http://localhost:8000/company-info?symbol=JKH.N0000')
data = response.json()
print(data)

# Get top gainers
response = requests.get('http://localhost:8000/top-gainers')
data = response.json()
print(data)
```

## Notes

- All timestamps are in milliseconds (Unix timestamp)
- Prices are in Sri Lankan Rupees (LKR)
- Volumes are in shares/units
- Market capitalization values are in LKR
- The API caches responses from the CSE API, but data is fetched in real-time
- Some endpoints may return empty arrays if no data is available
- Market data is only available during trading hours

## Support

For technical support or questions about the API, please contact:

**Developer:** Nithilan Pahirathan  
**Email:** nithilan32@gmail.com

---

**Last Updated:** December 2025
**API Version:** CSE=V1.0
