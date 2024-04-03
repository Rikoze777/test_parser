import json
import pprint


def main():
    with open("olimpbet.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    result = {}
    for item in data:
        for elements in item["payload"]["competitionsWithEvents"]:
            if elements["competition"]["sportName"] == "Футбол":
                for events in elements["events"]:
                    result[events["name"]] = {}
                    result[events["name"]]["team1Name"] = events["team1Name"]
                    result[events["name"]]["team2Name"] = events["team2Name"]
                    for outcome in events["outcomes"]:
                        if outcome["shortName"] == "П1":
                            result[events["name"]]["team1Score"] = outcome[
                                "probability"
                            ]
                        if outcome["shortName"] == "П2":
                            result[events["name"]]["team2Score"] = outcome[
                                "probability"
                            ]
                        if outcome["shortName"] == "Х":
                            result[events["name"]]["draw"] = outcome["probability"]

    pprint.pprint(result)


if __name__ == "__main__":
    main()
