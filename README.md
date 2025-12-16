# Colombo Stock Exchange API (CSE_API)

A FastAPI-based REST API wrapper for the Colombo Stock Exchange (CSE) API, providing structured access to real-time market data, company information, trade summaries, announcements, and market indices.

**Version:** CSE=V1.0

## Features

-  **Company Information** - Get detailed company data including prices, volumes, market cap, and more
-  **Market Data** - Access trade summaries, today's share prices, top gainers/losers, and most active trades
-  **Announcements** - Retrieve various types of announcements (financial, circular, directive, etc.)
-  **Market Indices** - Get ASPI and S&P 20 index data
-  **Sectors** - Access sector-wise market information
-  **Market Summary** - Daily and real-time market summaries
-  **Detailed Trades** - Get detailed trade information

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/Pahinithi/colombo-stock-exchange-api.git
cd TA_SM_API
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
cp .env.example .env
```

5. Edit `.env` and set your configuration:
```env
CSE_BASE_URL=https://www.cse.lk/api
```

## Configuration

The API uses environment variables for configuration. Create a `.env` file in the root directory:

```env
CSE_BASE_URL=https://www.cse.lk/api
```

## Usage

### Running Locally

Start the development server:
```bash
fastapi dev app/main.py
```

Or Run in prod mode:
```bash
fastapi run app/main.py
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### Running with Docker

1. Build the container:
```bash
docker build -f containerfile -t cse-api:latest .
```

2. Run the container:
```bash
docker run -p 8000:8000 --env-file .env cse-api:latest
```

Or run in detached mode:
```bash
docker run -d -p 8000:8000 --env-file .env --name cse-api cse-api:latest
```

3. Stop the container:
```bash
docker stop cse-api
```

## API Endpoints

### Health Check

- **GET** `/health` - Check API health status

### Company Information

- **GET** `/company-info?symbol={symbol}` - Get detailed company information
  - **Parameters:**
    - `symbol` (required): Company stock symbol (e.g., `JKH.N0000`)

### Market Data

- **GET** `/trade-summary` - Get trade summary for all companies
- **GET** `/today-share-price` - Get today's share prices for all companies
- **GET** `/top-gainers` - Get top gaining stocks
- **GET** `/top-losers` - Get top losing stocks
- **GET** `/most-active-trades` - Get most actively traded stocks
- **GET** `/detailed-trades` - Get detailed trade information

### Market Indices

- **GET** `/index/aspi` - Get All Share Price Index (ASPI) data
- **GET** `/index/snp20` - Get S&P 20 index data

### Market Summary

- **GET** `/market-status` - Get current market status
- **GET** `/market-summary` - Get market summary
- **GET** `/daily-market-summary` - Get daily market summary

### Sectors

- **GET** `/sectors` - Get all sectors with their performance data

### Announcements

- **GET** `/announcements/new-listings` - Get new listings related announcements
- **GET** `/announcements/buy-in-board` - Get buy-in board announcements
- **GET** `/announcements/approved` - Get approved announcements
- **GET** `/announcements/financial` - Get financial announcements
- **GET** `/announcements/circular` - Get circular announcements
- **GET** `/announcements/directive` - Get directive announcements
- **GET** `/announcements/non-compliance` - Get non-compliance announcements

## Example Requests

### Get Company Information

```bash
curl "http://localhost:8000/company-info?symbol=JKH.N0000"
```

### Get Top Gainers

```bash
curl "http://localhost:8000/top-gainers"
```

### Get Market Summary

```bash
curl "http://localhost:8000/market-summary"
```

### Get ASPI Index

```bash
curl "http://localhost:8000/index/aspi"
```

## Testing with Postman or Testing Tools

You can test the CSE API endpoints directly using Postman or other API testing tools. Here's an example for testing the company information endpoint:

### Testing Company Information Endpoint

**Method:** `POST`

**URL:** `https://www.cse.lk/api/companyInfoSummery`

**Headers:**
```
Referer: https://www.cse.lk/
Origin: https://www.cse.lk
```

**Body (x-www-form-urlencoded):**
```
symbol: JKH.N0000
```

**Postman Setup:**
1. Set the request method to **POST**
2. Enter the URL: `https://www.cse.lk/api/companyInfoSummery`
3. Go to **Headers** tab and add:
   - Key: `Referer`, Value: `https://www.cse.lk/`
   - Key: `Origin`, Value: `https://www.cse.lk`
4. Go to **Body** tab
5. Select **x-www-form-urlencoded**
6. Add key-value pair:
   - Key: `symbol`, Value: `JKH.N0000`
7. Click **Send**

**Note:** Most CSE API endpoints require POST requests with form-encoded data and the Referer/Origin headers for proper authentication.

## Response Format

All endpoints return JSON responses with structured data. The API uses Pydantic models for response validation, ensuring consistent data formats.

Example response structure:
```json
{
  "symbol": "JKH.N0000",
  "name": "JOHN KEELLS HOLDINGS PLC",
  "price": {
    "last_traded": 21.2,
    "previous_close": 21.0,
    "change": 0.2,
    "change_percentage": 0.95
  },
  "volume": {
    "today_share_volume": 6155799,
    "today_trade_count": 471,
    "today_turnover": 130655544.0
  }
}
```

## Error Handling

The API returns standard HTTP status codes:

- **200** - Success
- **404** - Resource not found
- **502** - CSE API not reachable or error

Error response format:
```json
{
  "detail": "Error message description"
}
```

## Project Structure

```
TA_SM_API/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and routes
│   ├── settings.py          # Configuration settings
│   └── utlits/
│       ├── __init__.py
│       ├── mappers.py       # Data mapping functions
│       └── schemas.py       # Pydantic models
├── containerfile            # Docker/Containerfile
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables example
└── README.md               # This file
```

## Development

### Running in Development Mode

```bash
fastapi dev app/main.py
```

This will:
- Start the server with auto-reload
- Enable interactive API documentation
- Show detailed error messages


## Dependencies

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Pydantic Settings** - Settings management using Pydantic
- **Requests** - HTTP library for making API calls to CSE




## Acknowledgments

- Colombo Stock Exchange (CSE) for providing the underlying API
- FastAPI community for the excellent framework

