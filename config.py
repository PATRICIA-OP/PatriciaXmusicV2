# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith 

from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAZSF2cBMRd4gKlbbPLj9Pns2srhmGDwSfgOkdlcQLND26U6TCeQnxtvsRvOpoFNTtZZk9pYc1k-E0ZDRa-z0xqGRFacuxdh6nzY-Hpeg4xZtj4P_5ZVBUdjrTHMy4JJsFRXo4cFy08w0zvMefvFJe7Pvy4yO7dCzEv8ZzV4sPHqG3tCHq-WD7SVqXLGqEzkCXxRGSpnQLpacoxQrfA5Tk3zQ91mSZQm9HC7L8TQEsJ0WClO2xv8CQcT-3dtig6s6bPdIbTRkC7ceMVJlrZB6g9MzCU7CyiRYxECavoselYvtgdlVwfCDrogKwb03RPN-KPY7fTu8SVR8WD9ixH8fv4L7y8qgA")
BOT_TOKEN = getenv("BOT_TOKEN", "1706083159:AAHAnJLE7DS2-4F82wX7OA9m1eQXMy-WVGM")
BOT_NAME = getenv("BOT_NAME", "patriciaXmusic")
admins = {}
API_ID = int(getenv("API_ID", "3088812"))
API_HASH = getenv("API_HASH", "d51f13802ef40ccb115e333a5f9dc9e7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607847356").split()))
