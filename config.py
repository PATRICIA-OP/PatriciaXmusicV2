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
SESSION_NAME = getenv("SESSION_NAME", "AQC3PT0KhhM2zXlMh0sfjJoKbFQG9K8bpzSl_2baYf7UbAlhw5GzoNqm9DPJbjFRejY1xAoHb3kcwcyDF2CP9_lf_V_IkGioE0jwdNgq_XC7Ha46x5qS9AquAzPz1irdX1s3W4nyUj2SeKtkG0YEBoVAsGsNFlMiS6A4WYBtUNi34eWgFnq4PC6pXeQ7TRlYy2dlAOhEpw-GzV5AlL6EmgfD9J9vN5h4ekalHgpT9eeXefZCot8UoYZdL5hcR9CZi-qGrohV0AoQaxOxyfp9ExGxNAe_HFz8GgQ3B23wa8bTaglakvM8IBBA5tLjkMLlNCZ3yUIUCi5M3a1RL6tgzW_KL7y8qgA")
BOT_TOKEN = getenv("BOT_TOKEN", "1706083159:AAHAnJLE7DS2-4F82wX7OA9m1eQXMy-WVGM")
BOT_NAME = getenv("BOT_NAME", "patriciaXmusic")
admins = {}
API_ID = int(getenv("API_ID", "3088812"))
API_HASH = getenv("API_HASH", "d51f13802ef40ccb115e333a5f9dc9e7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607847356").split()))
