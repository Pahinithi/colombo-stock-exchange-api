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


## Acknowledgments

- Colombo Stock Exchange (CSE) for providing the underlying API
- FastAPI community for the excellent framework


## Contact

For any questions or support, please contact:
- Developer: Nithilan Pahirathan
- Email: nithilan32@gmail.com