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
SESSION_NAME = getenv("SESSION_NAME", "BQBBsWKYGVMMaPQCT6AWC9-Zau_hOTp6Fq5pfI67pZ-VSmFvtvVs4Zx5c8LNC3ABUsfjxBDAQzhVsNAMrvnbIEZ19Kt-loT7OngL0uWnZE1po5ffotJ4WS7YYyCW2Q8g8PhGpPqn8GBSnVE04p_RcjJzNWIgkSXn2AvwcAkTWOQA0JnkebCuDk7m4MTUIAAjIwz6AtmQgY8gIeXPO6cbH9jTwjvBVgj4pfTsnw7LVRRZ8y-f9YoVQRlEnQPvGAFuHEOPy083tq5Y6XkZrk32QLp5-0dGaDprpvzPNGg74225olX83XsQiPkVWig416owuAb2P3le7MHZg2TWE_DJYA-ZX9XNvAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1706513392:AAGAvq53BHLW4ywfcGClNbEiflZnS-tevgg")
BOT_NAME = getenv("BOT_NAME", "patriciaXmusic")
admins = {}
API_ID = int(getenv("API_ID", "3898418"))
API_HASH = getenv("API_HASH", "5a82313211da04d63297bd4de436228c")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607847356").split()))
