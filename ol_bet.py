import aiohttp
import asyncio
from fake_useragent import UserAgent
import pprint
import json


async def main():
    async with aiohttp.ClientSession() as session:
        UA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "User-Agent": UA,
        }
        url = "https://www.olimp.bet/api/v4/0/line/sports-with-competitions-with-events?vids[]=1:"
        async with session.get(url, headers=headers) as response:
            html = await response.text()
            response_json = json.loads(html)

            with open("olimpbet.json", "w", encoding="utf-8") as file:
                json.dump(response_json, file, ensure_ascii=False)
            # pprint.pprint(html)


if __name__ == "__main__":
    asyncio.run(main())
