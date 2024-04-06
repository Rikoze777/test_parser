import aiohttp
from bs4 import BeautifulSoup
import collections
from environs import Env


async def get_live_url(headers: dict) -> str:
    async with aiohttp.ClientSession() as session:
        env = Env()
        env.read_env()
        com_url = env("COM_URL")
        bet_url = com_url + "/betting"
        async with session.get(bet_url, headers=headers) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            elements = soup.find_all(attrs={"data-s": "1"})
            base_live_url = f"{com_url}/index.php?page=line&action=2&currpage=live&time=0&live%5B%5D="
            end_element = "&line_nums=1"
            for element in elements:
                href = element.get("href")
                live_id = href.split("live[]=")[1]
                live_id = live_id.replace("sid[]=1", "live[]=")
                base_live_url = base_live_url + live_id
            live_url = base_live_url + end_element
            return live_url


async def get_full_live_response(headers: dict, live_url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(live_url, headers=headers) as response:
            response_text = await response.text()
            return response_text


async def parse_koefs(all_koeffs: BeautifulSoup) -> dict:
    koeffs = collections.defaultdict(dict)
    for koef in all_koeffs:
        try:
            type_koef = koef.find(class_="googleStatIssueName")
            type_koef = type_koef.text
        except AttributeError:
            continue
        type_list = ["П1", "Х", "П2"]
        if type_koef in type_list:
            bet_koef = koef.find(class_="bet_sel koefs")
            number = str(bet_koef).split('match="')[1]
            number = number.split('" d')[0]
            kef = str(bet_koef).split('"googleStatKef">')[1]
            kef = kef.split("</span>")[0]
            koeffs[number][type_koef] = kef
    return koeffs


async def parse_matches(all_matches: BeautifulSoup) -> dict:
    matches = collections.defaultdict(dict)
    for item in all_matches:
        number = str(item).split("name_")[1]
        number = number.split('"')[0]
        match = str(item).split("\xa0")[1]
        match = match.split("</span>")[0]
        matches[number] = match
    return matches


async def parse_com_html(response_text: str) -> tuple:
    soup = BeautifulSoup(response_text, "html.parser")
    elements = soup.find(id="champ_container_")

    all_matches = elements.find_all(class_="gameNameLine")
    all_koeffs = elements.find_all("nobr")

    koeffs = await parse_koefs(all_koeffs)
    matches = await parse_matches(all_matches)

    return koeffs, matches


async def fetch_com_result(koeffs: dict, matches: dict) -> dict:
    result_dict = collections.defaultdict(dict)
    for key, value in matches.items():
        if key in koeffs:
            match = matches[key]
            team1Name = match.split(" - ")[0]
            team2Name = match.split(" - ")[1]
            result_dict[value]["id"] = key
            result_dict[value]["team1Name"] = team1Name
            result_dict[value]["team2Name"] = team2Name
            result_dict[value]["team1Score"] = float(koeffs[key]["П1"])
            result_dict[value]["team2Score"] = float(koeffs[key]["П2"])
            result_dict[value]["draw"] = float(koeffs[key]["Х"])
    return result_dict
