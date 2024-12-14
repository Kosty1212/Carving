import json

from loguru import logger
from settings import RETRY_COUNT
from utils.sleeping import sleep
import traceback
from config import USER_AGENTS_PATH
import os
from fake_useragent import UserAgent


def retry(func):
    async def wrapper(*args, **kwargs):
        retries = 0
        while retries <= RETRY_COUNT:
            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Error | {e}")
                traceback.print_exc()
                await sleep(10, 20)
                retries += 1

    return wrapper


def setup_user_agent(wallet_data):
    user_agents = {}
    if os.path.exists(USER_AGENTS_PATH):
        with open(USER_AGENTS_PATH, 'r') as f:
            user_agents = json.load(f)
    for wallet in wallet_data:
        if wallet not in user_agents:
            user_agents[wallet] = UserAgent().chrome
        wallet_data[wallet]['user_agent'] = user_agents[wallet]
    with open(USER_AGENTS_PATH, 'w') as f:
        json.dump(user_agents, f)
