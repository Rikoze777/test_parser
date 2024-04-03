import aiohttp
import asyncio
import json


async def main():
    async with aiohttp.ClientSession() as session:
        user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"

        com_url = "https://fyvixisq.olimpmagt.xyz/index.php?page=line&action=2&sel[]="
        com_url2 = "https://fyvixisq.olimpmagt.xyz/ajax_index.php?page=line_page"
        com_url3 = "https://fyvixisq.olimpmagt.xyz/betting/soccer/index.php?page=line&action=1&sel[]=40"
        com_headers = {
            "Accept": "text/html, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "User-Agent": user_agent,
        }
        async with session.get(com_url3, headers=com_headers) as response:
            html = await response.text()
            print(html)
            # response_json = json.loads(html)

            # with open("olimp_com.json", "w", encoding="utf-8") as file:
            #     json.dump(response_json, file, ensure_ascii=False)
            # with open("saved_page.html", "w", encoding="utf-8") as file:
            #     file.write(html)
            #     print("HTML page saved successfully.")


if __name__ == "__main__":
    asyncio.run(main())
