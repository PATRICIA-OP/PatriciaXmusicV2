from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "AQCm5AGigrfvAyuGzbiZZf5ZVDL5FanqzWwVWHdOhOS0xLQEhIFLa8lgJJKstEor_9pbVWlpUFv9UMhLKp3qajrdn0mtOqxhNk4Z6Hq41DcLLTJ9OBen2IaLCAjG2FyxTTGKgcfZyP-6GWZgetw9ytT5ButQHIRB_AeusyRuSxuSBAhn2oQ7rft90LdXEvxKzX0f-3FFU8fsqJL2A1L7Cy69ofoB7Bb5nGXlf55vOYnsuBTtQR5Xsp3POBf-zn2c0kSd46ouWGh2deEWhdciZQ5wq_lzKKNz49BVRq-QGVwvU4KDbBg4vmCBFCtWX2-yY37NSMUaEwK6EfbjAMa3HNWeL7y8qgA")

BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAG_qNWSYnl1jEUvAnhaqLrXUFONUKObIJM")

BOT_NAME = getenv("BOT_NAME", "patriciaXmusic")

API_ID = int(getenv("API_ID", "3088812"))

API_HASH = getenv("API_HASH", "d51f13802ef40ccb115e333a5f9dc9e7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1801516703").split()))
