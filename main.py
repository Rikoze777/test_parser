import asyncio
from ol_com import (
    get_live_url,
    get_full_live_response,
    parse_com_html,
    fetch_com_result,
)
from ol_bet import get_bet_response, get_bet_result
from logs import log_bets


async def gather_responses() -> tuple:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    }

    com_url = await get_live_url(headers)

    live_response = asyncio.create_task(get_full_live_response(headers, com_url))
    bet_response = asyncio.create_task(get_bet_response(headers))
    com_response, bet_response = await asyncio.gather(live_response, bet_response)

    return com_response, bet_response


async def main():
    com_response, bet_response = await gather_responses()
    bet_result = await get_bet_result(bet_response)
    koeffs, matches = await parse_com_html(com_response)
    com_result = await fetch_com_result(koeffs, matches)
    await log_bets(com_result, bet_result)
    print("Matches fetched successfully")


if __name__ == "__main__":
    asyncio.run(main())
