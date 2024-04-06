from telegram.client import Telegram
from telegram.text import Spoiler
from environs import Env


def rewrite_env(message):
    with open(".env", "r+") as f:
        new_file = []
        for line in f.readlines():
            if line.startswith("COM_URL="):
                line = f'COM_URL="{message}"'
            new_file.append(line)
        str_list = "".join(new_file)
    with open(".env", "w") as f:
        f.write(str_list)


def new_message_handler(update):
    try:
        message_content = update["message"]["content"].get("text", {})
        message_text = message_content.get("text", "").lower()
        message = "".join(message_text.split("\n\n")[1])
        message = message.replace("/casino", "")
        rewrite_env(message)
    except Exception as e:
        raise e


def main():
    env = Env()
    env.read_env()

    com_bot_chat_id = 230479887
    message = "/mirror"
    tg = Telegram(
        api_id=env("API_ID"),
        api_hash=env("API_HASH"),
        phone=env("PHONE"),
        database_encryption_key="changekey123",
        files_directory="/tmp/.tdlib_files/",
    )
    tg.login()

    result = tg.get_chats()
    result.wait()

    result = tg.send_message(com_bot_chat_id, Spoiler(message))
    result.wait()
    tg.add_message_handler(new_message_handler)

    tg.idle()


if __name__ == "__main__":
    main()
