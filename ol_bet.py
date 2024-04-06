import aiohttp
import json


async def get_bet_response(headers: dict) -> str:
    async with aiohttp.ClientSession() as session:
        bet_live_url = "https://www.olimp.bet/api/v4/0/live/sports-with-competitions-with-events?vids[]=1:"
        async with session.get(bet_live_url, headers=headers) as response:
            response_text = await response.text()
            return response_text


async def get_bet_result(response_text: str) -> dict:
    response_json = json.loads(response_text)
    result = {}
    for item in response_json:
        for elements in item["payload"]["competitionsWithEvents"]:
            if elements["competition"]["sportName"] == "Футбол":
                for events in elements["events"]:
                    result[events["name"]] = {}
                    result[events["name"]]["id"] = events["id"]
                    result[events["name"]]["team1Name"] = events["team1Name"]
                    result[events["name"]]["team2Name"] = events["team2Name"]
                    for outcome in events["outcomes"]:
                        if outcome["shortName"] == "П1":
                            result[events["name"]]["team1Score"] = float(
                                outcome["probability"]
                            )
                        if outcome["shortName"] == "П2":
                            result[events["name"]]["team2Score"] = float(
                                outcome["probability"]
                            )
                        if outcome["shortName"] == "Х":
                            result[events["name"]]["draw"] = float(
                                outcome["probability"]
                            )
    return result
