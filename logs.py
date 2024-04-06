import logging


async def log_bets(com_result: dict, bet_result: dict) -> None:
    logging.basicConfig(level=logging.INFO, filename="bets.log", filemode="w")
    logging.info("Information about bets")
    for key, value in bet_result.items():
        if value in com_result.values():
            try:
                com_id = com_result[key]["id"]
                bet_id = bet_result[key]["id"]
                p1_com = com_result[key]["team1Score"]
                p2_com = com_result[key]["team2Score"]
                draw_com = com_result[key]["draw"]
                p1_bet = bet_result[key]["team1Score"]
                p2_bet = bet_result[key]["team2Score"]
                draw_bet = bet_result[key]["draw"]
            except TypeError as er:
                print(er)
                pass
            except KeyError as er:
                print(er)
                pass
            logging.info(f"olimp.com[{com_id} {key}] - olimp.bet[{bet_id} {key}] \n")
            if p1_com > p1_bet:
                logging.info(f"П1 - olimp.com {p1_com} > {p1_bet} olimp.bet \n")
            if p1_com < p1_bet:
                logging.info(f"П1 - olimp.com {p1_com} < {p1_bet} olimp.bet \n")
            if p1_com == p1_bet:
                logging.info(f"П1 - olimp.com {p1_com} = {p1_bet} olimp.bet \n")
            if p2_com > p2_bet:
                logging.info(f"П2 - olimp.com {p2_com} > {p2_bet} olimp.bet \n")
            if p2_com < p2_bet:
                logging.info(f"П2 - olimp.com {p2_com} < {p2_bet} olimp.bet \n")
            if p2_com == p2_bet:
                logging.info(f"П2 - olimp.com {p2_com} = {p2_bet} olimp.bet \n")
            if draw_com > draw_bet:
                logging.info(f"Х - olimp.com {draw_com} > {draw_bet} olimp.bet \n")
            if draw_com < draw_bet:
                logging.info(f"Х - olimp.com {draw_com} < {draw_bet} olimp.bet \n")
            if draw_com == draw_bet:
                logging.info(f"Х - olimp.com {draw_com} = {draw_bet} olimp.bet \n")
