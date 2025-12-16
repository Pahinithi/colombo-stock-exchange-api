from pydantic import BaseModel


class Price(BaseModel):
    last_traded: float | None
    previous_close: float | None
    change: float | None
    change_percentage: float | None
    high: float | None
    low: float | None
    closing_price: float | None


class Volume(BaseModel):
    today_share_volume: int | None
    today_trade_count: int | None
    today_turnover: float | None


class MarketCap(BaseModel):
    value: float | None
    market_percentage: float | None


class HighLow(BaseModel):
    week_52_high: float | None
    week_52_low: float | None
    all_time_high: float | None
    all_time_low: float | None


class Logo(BaseModel):
    path: str | None


class CompanyInfoResponse(BaseModel):
    symbol: str
    name: str
    isin: str | None
    issue_date: str | None
    par_value: float | None

    price: Price
    volume: Volume
    market_cap: MarketCap
    high_low: HighLow
    logo: Logo


class TradeSummaryItem(BaseModel):
    symbol: str
    name: str
    price: float | None
    previous_close: float | None
    change: float | None
    change_percentage: float | None
    high: float | None
    low: float | None
    closing_price: float | None
    turnover: float | None
    share_volume: int | None
    trade_volume: int | None
    market_cap: float | None


class TradeSummaryResponse(BaseModel):
    trades: list[TradeSummaryItem]


class TodaySharePriceItem(BaseModel):
    symbol: str
    open: float | None
    high: float | None
    low: float | None
    last_traded: float | None
    change: float | None
    change_percentage: float | None
    crossing_volume: int | None
    quantity: int | None


class TodaySharePriceResponse(BaseModel):
    prices: list[TodaySharePriceItem]


class TopGainerItem(BaseModel):
    symbol: str
    price: float | None
    change: float | None
    change_percentage: float | None
    trade_date: int | None  # timestamp in milliseconds


class TopGainersResponse(BaseModel):
    gainers: list[TopGainerItem]


class TopLoserItem(BaseModel):
    symbol: str
    price: float | None
    change: float | None
    change_percentage: float | None
    trade_date: int | None


class TopLosersResponse(BaseModel):
    losers: list[TopLoserItem]


class MostActiveTradeItem(BaseModel):
    symbol: str
    trade_volume: float | None
    share_volume: float | None
    turnover: float | None
    percentage_share_volume: float | None


class MostActiveTradesResponse(BaseModel):
    trades: list[MostActiveTradeItem]


class AnnouncementItem(BaseModel):
    announcement_id: int | None
    created_date: str | int | None
    category: str | None
    company: str | None
    # title: str | None
    remarks: str | None
    # file_path: str | None


class AnnouncementsResponse(BaseModel):
    announcements: list[AnnouncementItem]

class MarketStatusResponse(BaseModel):
    status: str

class MarketSummaryResponse(BaseModel):
    trade_volume: float | None
    share_volume: int | None
    trade_date: int | None


class IndexResponse(BaseModel):
    value: float | None
    low: float | None
    high: float | None
    change: float | None
    percentage: float | None
    timestamp: int | None


class SectorItem(BaseModel):
    name: str
    index_value: float | None
    change: float | None
    percentage: float | None
    turnover: float | None
    volume: int | None


class SectorsResponse(BaseModel):
    sectors: list[SectorItem]


class DetailedTradeItem(BaseModel):
    symbol: str
    name: str
    price: float | None
    quantity: int | None
    trades: int | None
    change: float | None
    change_percentage: float | None


class DetailedTradesResponse(BaseModel):
    trades: list[DetailedTradeItem]


class DailyMarketSummary(BaseModel):
    trade_date: int | None
    market_turnover: float | None
    market_trades: int | None
    market_cap: float | None
    asi: float | None
    s_and_p_20: float | None
    per: float | None
    pbv: float | None
    dy: float | None


class DailyMarketSummaryResponse(BaseModel):
    summary: DailyMarketSummary
