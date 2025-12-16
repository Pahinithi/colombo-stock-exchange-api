from fastapi import FastAPI, HTTPException
import requests

from .settings import settings
from .utlits.schemas import (
    AnnouncementsResponse,
    CompanyInfoResponse,
    DailyMarketSummaryResponse,
    DetailedTradesResponse,
    IndexResponse,
    MarketStatusResponse,
    MarketSummaryResponse,
    MostActiveTradesResponse,
    SectorsResponse,
    TodaySharePriceResponse,
    TopGainersResponse,
    TopLosersResponse,
    TradeSummaryResponse,
)
from .utlits.mappers import (
    map_announcements,
    map_cse_company_info,
    map_cse_most_active_trades,
    map_cse_today_share_price,
    map_cse_top_gainers,
    map_cse_top_losers,
    map_cse_trade_summary,
    map_daily_market_summary,
    map_detailed_trades,
    map_index_data,
    map_market_summary,
    map_sectors,
)

app = FastAPI(
    title="Colombo Stock Exchange API",
    version="CSE=V1.0"
)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/company-info", response_model=CompanyInfoResponse)
def get_company_info(symbol: str):
    url = f"{settings.CSE_BASE_URL}/companyInfoSummery"

    try:
        res = requests.post(url, data={"symbol": symbol}, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Company not found")

    return map_cse_company_info(data)


@app.get("/trade-summary", response_model=TradeSummaryResponse)
def get_trade_summary():
    url = f"{settings.CSE_BASE_URL}/tradeSummary"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data or "reqTradeSummery" not in data:
        raise HTTPException(status_code=404, detail="Trade summary not found")

    return map_cse_trade_summary(data)


@app.get("/today-share-price", response_model=TodaySharePriceResponse)
def get_today_share_price():
    url = f"{settings.CSE_BASE_URL}/todaySharePrice"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Today share price not found")

    return map_cse_today_share_price(data)


@app.get("/top-gainers", response_model=TopGainersResponse)
def get_top_gainers():
    url = f"{settings.CSE_BASE_URL}/topGainers"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Top gainers not found")

    return map_cse_top_gainers(data)


@app.get("/top-losers", response_model=TopLosersResponse)
def get_top_losers():
    url = f"{settings.CSE_BASE_URL}/topLooses"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Top losers not found")

    return map_cse_top_losers(data)


@app.get("/most-active-trades", response_model=MostActiveTradesResponse)
def get_most_active_trades():
    url = f"{settings.CSE_BASE_URL}/mostActiveTrades"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Most active trades not found")

    return map_cse_most_active_trades(data)


@app.get("/announcements/new-listings", response_model=AnnouncementsResponse)
def new_listings_announcements():
    url = f"{settings.CSE_BASE_URL}/getNewListingsRelatedNoticesAnnouncements"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    return map_announcements(data.get("newListingRelatedAnnouncements", []))


@app.get("/announcements/buy-in-board", response_model=AnnouncementsResponse)
def buy_in_board_announcements():
    url = f"{settings.CSE_BASE_URL}/getBuyInBoardAnnouncements"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    return map_announcements(data.get("buyInBoardAnnouncements", []))


@app.get("/announcements/approved", response_model=AnnouncementsResponse)
def approved_announcements():
    url = f"{settings.CSE_BASE_URL}/approvedAnnouncement"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    return map_announcements(data.get("approvedAnnouncements", []))


# @app.get("/announcements/covid", response_model=AnnouncementsResponse)
# def covid_announcements():
#     url = f"{settings.CSE_BASE_URL}/getCOVIDAnnouncements"

#     try:
#         res = requests.post(url, timeout=10)
#         res.raise_for_status()
#         data = res.json()
#     except requests.exceptions.RequestException:
#         raise HTTPException(status_code=502, detail="CSE API not reachable")

#     return map_announcements(data.get("covidAnnouncements", []))


@app.get("/announcements/financial", response_model=AnnouncementsResponse)
def financial_announcements():
    url = f"{settings.CSE_BASE_URL}/getFinancialAnnouncement"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    return map_announcements(data.get("reqFinancialAnnouncemnets", []))


@app.get("/announcements/circular", response_model=AnnouncementsResponse)
def circular_announcements():
    url = f"{settings.CSE_BASE_URL}/circularAnnouncement"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    return map_announcements(data.get("reqCircularAnnouncement", []))


@app.get("/announcements/directive", response_model=AnnouncementsResponse)
def directive_announcements():
    url = f"{settings.CSE_BASE_URL}/directiveAnnouncement"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    return map_announcements(data.get("reqDirectiveAnnouncement", []))


@app.get("/announcements/non-compliance", response_model=AnnouncementsResponse)
def non_compliance_announcements():
    url = f"{settings.CSE_BASE_URL}/getNonComplianceAnnouncements"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    return map_announcements(data.get("nonComplianceAnnouncements", []))


@app.get("/market-status", response_model=MarketStatusResponse)
def market_status():
    url = f"{settings.CSE_BASE_URL}/marketStatus"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Market status not found")

    return data


@app.get("/market-summary", response_model=MarketSummaryResponse)
def market_summary():
    url = f"{settings.CSE_BASE_URL}/marketSummery"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Market summary not found")

    return map_market_summary(data)


@app.get("/index/aspi", response_model=IndexResponse)
def aspi_index():
    url = f"{settings.CSE_BASE_URL}/aspiData"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="ASPI index data not found")

    return map_index_data(data)


@app.get("/index/snp20", response_model=IndexResponse)
def snp_index():
    url = f"{settings.CSE_BASE_URL}/snpData"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="S&P 20 index data not found")

    return map_index_data(data)


@app.get("/sectors", response_model=SectorsResponse)
def all_sectors():
    url = f"{settings.CSE_BASE_URL}/allSectors"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Sectors not found")

    return map_sectors(data)


@app.get("/detailed-trades", response_model=DetailedTradesResponse)
def detailed_trades():
    url = f"{settings.CSE_BASE_URL}/detailedTrades"

    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Detailed trades not found")

    return map_detailed_trades(data)


@app.get("/daily-market-summary", response_model=DailyMarketSummaryResponse)
def daily_market_summary():
    url = f"{settings.CSE_BASE_URL}/dailyMarketSummery"
    try:
        res = requests.post(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="CSE API not reachable")

    if not data:
        raise HTTPException(status_code=404, detail="Daily market summary not found")

    return map_daily_market_summary(data)
