from .schemas import (
    AnnouncementItem,
    AnnouncementsResponse,
    CompanyInfoResponse,
    DailyMarketSummary,
    DailyMarketSummaryResponse,
    DetailedTradeItem,
    DetailedTradesResponse,
    IndexResponse,
    MarketSummaryResponse,
    MostActiveTradeItem,
    MostActiveTradesResponse,
    SectorItem,
    SectorsResponse,
    TodaySharePriceItem,
    TodaySharePriceResponse,
    TopGainerItem,
    TopGainersResponse,
    TopLoserItem,
    TopLosersResponse,
    TradeSummaryItem,
    TradeSummaryResponse,
)


def map_cse_company_info(data: dict) -> CompanyInfoResponse:
    # Extract nested data from API response
    symbol_info = data.get("reqSymbolInfo", {})
    logo_info = data.get("reqLogo", {})

    return CompanyInfoResponse(
        symbol=symbol_info.get("symbol"),
        name=symbol_info.get("name"),
        isin=symbol_info.get("isin"),
        issue_date=symbol_info.get("issueDate"),
        par_value=symbol_info.get("parValue"),
        price={
            "last_traded": symbol_info.get("lastTradedPrice"),
            "previous_close": symbol_info.get("previousClose"),
            "change": symbol_info.get("change"),
            "change_percentage": symbol_info.get("changePercentage"),
            "high": symbol_info.get("hiTrade"),
            "low": symbol_info.get("lowTrade"),
            "closing_price": symbol_info.get("closingPrice"),
        },
        volume={
            "today_share_volume": symbol_info.get("tdyShareVolume"),
            "today_trade_count": symbol_info.get("tdyTradeVolume"),
            "today_turnover": symbol_info.get("tdyTurnover"),
        },
        market_cap={
            "value": symbol_info.get("marketCap"),
            "market_percentage": symbol_info.get("marketCapPercentage"),
        },
        high_low={
            "week_52_high": symbol_info.get("p12HiPrice"),
            "week_52_low": symbol_info.get("p12LowPrice"),
            "all_time_high": symbol_info.get("allHiPrice"),
            "all_time_low": symbol_info.get("allLowPrice"),
        },
        logo={"path": logo_info.get("path")},
    )


def map_cse_trade_summary(data: dict) -> TradeSummaryResponse:
    trade_list = data.get("reqTradeSummery", [])
    trades = []

    for item in trade_list:
        trades.append(
            TradeSummaryItem(
                symbol=item.get("symbol"),
                name=item.get("name"),
                price=item.get("price"),
                previous_close=item.get("previousClose"),
                change=item.get("change"),
                change_percentage=item.get("percentageChange"),
                high=item.get("high"),
                low=item.get("low"),
                closing_price=item.get("closingPrice"),
                turnover=item.get("turnover"),
                share_volume=item.get("sharevolume"),
                trade_volume=item.get("tradevolume"),
                market_cap=item.get("marketCap"),
            )
        )
    return TradeSummaryResponse(trades=trades)


def map_cse_today_share_price(data: list[dict]) -> TodaySharePriceResponse:
    prices = []

    for item in data:
        prices.append(
            TodaySharePriceItem(
                symbol=item.get("symbol"),
                open=item.get("open"),
                high=item.get("high"),
                low=item.get("low"),
                last_traded=item.get("lastTradedPrice"),
                change=item.get("change"),
                change_percentage=item.get("changePercentage"),
                crossing_volume=item.get("crossingVolume"),
                quantity=item.get("quantity"),
            )
        )
    return TodaySharePriceResponse(prices=prices)


def map_cse_top_gainers(data: list[dict]) -> TopGainersResponse:
    gainers = []

    for item in data:
        gainers.append(
            TopGainerItem(
                symbol=item.get("symbol"),
                price=item.get("price"),
                change=item.get("change"),
                change_percentage=item.get("changePercentage"),
                trade_date=item.get("tradeDate"),
            )
        )
    return TopGainersResponse(gainers=gainers)



def map_cse_top_losers(data: list[dict]) -> TopLosersResponse:
    losers = []

    for item in data:
        losers.append(
            TopLoserItem(
                symbol=item.get("symbol"),
                price=item.get("price"),
                change=item.get("change"),
                change_percentage=item.get("changePercentage"),
                trade_date=item.get("tradeDate"),
            )
        )
    return TopLosersResponse(losers=losers)



def map_cse_most_active_trades(data: list[dict]) -> MostActiveTradesResponse:
    trades = []

    for item in data:
        trades.append(
            MostActiveTradeItem(
                symbol=item.get("symbol"),
                trade_volume=item.get("tradeVolume"),
                share_volume=item.get("shareVolume"),
                turnover=item.get("turnover"),
                percentage_share_volume=item.get("percentageShareVolume"),
            )
        )
    return MostActiveTradesResponse(trades=trades)



def map_announcements(data: list[dict]) -> AnnouncementsResponse:
    announcements = []

    for item in data:
        announcements.append(
            AnnouncementItem(
                announcement_id=item.get("announcementId") or item.get("id"),
                created_date=item.get("createdDate") or item.get("uploadedDate") or item.get("manualDate"),
                category=item.get("announcementCategory"),
                company=item.get("company"),
                title=item.get("title"),
                remarks=item.get("remarks") or item.get("fileText"),
                file_path=item.get("path"),
            )
        )
    return AnnouncementsResponse(announcements=announcements)




def map_market_summary(data: dict) -> MarketSummaryResponse:
    return MarketSummaryResponse(
        trade_volume=data.get("tradeVolume"),
        share_volume=data.get("shareVolume"),
        trade_date=data.get("tradeDate"),
    )




def map_index_data(data: dict) -> IndexResponse:
    return IndexResponse(
        value=data.get("value"),
        low=data.get("lowValue"),
        high=data.get("highValue"),
        change=data.get("change"),
        percentage=data.get("percentage"),
        timestamp=data.get("timestamp"),
    )




def map_sectors(data: list[dict]) -> SectorsResponse:
    sectors = []

    for item in data:
        sectors.append(
            SectorItem(
                name=item.get("name"),
                index_value=item.get("indexValue"),
                change=item.get("change"),
                percentage=item.get("percentage"),
                turnover=item.get("sectorTurnoverToday"),
                volume=item.get("sectorVolumeToday"),
            )
        )
    return SectorsResponse(sectors=sectors)



def map_detailed_trades(data: dict) -> DetailedTradesResponse:
    trades = []

    for item in data.get("reqDetailTrades", []):
        trades.append(
            DetailedTradeItem(
                symbol=item.get("symbol"),
                name=item.get("name"),
                price=item.get("price"),
                quantity=item.get("qty"),
                trades=item.get("trades"),
                change=item.get("change"),
                change_percentage=item.get("changePercentage"),
            )
        )
    return DetailedTradesResponse(trades=trades)




def map_daily_market_summary(data: list) -> DailyMarketSummaryResponse:
    row = data[0][0]

    return DailyMarketSummaryResponse(
        summary=DailyMarketSummary(
            trade_date=row.get("tradeDate"),
            market_turnover=row.get("marketTurnover"),
            market_trades=row.get("marketTrades"),
            market_cap=row.get("marketCap"),
            asi=row.get("asi"),
            s_and_p_20=row.get("spp"),
            per=row.get("per"),
            pbv=row.get("pbv"),
            dy=row.get("dy"),
        )
    )
