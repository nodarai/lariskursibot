import os
from dataclasses import dataclass

from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


@dataclass
class KursiSettings:
    TOKEN: str = os.getenv("TOKEN", "")
    DB_FILENAME: str = os.getenv("DB_FILENAME", "sqlite:///lariskursi.db")
    PLOT_NAME: str = os.getenv("PLOT_NAME", "plot.png")


settings = KursiSettings()
