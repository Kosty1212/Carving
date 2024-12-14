import asyncio
from modules import *


async def withdraw_okx(wallet_info):
    """
    Withdraw ETH from OKX

    ______________________________________________________
    min_amount - min amount (ETH)
    max_amount - max_amount (ETH)
    chains - ['zksync', 'arbitrum', 'linea', 'base', 'optimism']
    terminate - if True - terminate program if money is not withdrawn
    skip_enabled - If True, the skip_threshold check will be applied; otherwise, it will be ignored
    skip_threshold - If skip_enabled is True and the wallet balance is greater than or equal to this threshold,
                     skip the withdrawal
    """
    token = 'ETH'
    chains = ['arbitrum', 'zksync', 'linea', 'base', 'optimism']

    min_amount = 0.0070
    max_amount = 0.0072

    terminate = False

    skip_enabled = False
    skip_threshold = 0.00327

    wait_unlimited_time = False
    sleep_between_attempts = [10, 20]  # min, max

    okx_exchange = Okx(wallet_info, chains)
    await okx_exchange.okx_withdraw(
        min_amount, max_amount, token, terminate, skip_enabled, skip_threshold,
        wait_unlimited_time, sleep_between_attempts
    )


async def transfer_to_okx(wallet_info):
    from_chains = ["optimism"]

    min_amount = 0.0012
    max_amount = 0.0012
    decimal = 4

    all_amount = True

    min_percent = 100
    max_percent = 100

    save_funds = [0.0001, 0.00012]
    min_required_amount = 0.002

    bridge_from_all_chains = False
    sleep_between_transfers = [1, 1]

    transfer_inst = Transfer(wallet_info)
    await transfer_inst.transfer_eth(
        from_chains, min_amount, max_amount, decimal, all_amount, min_percent,
        max_percent, save_funds, False, 0, min_required_amount,
        bridge_from_all_chains=bridge_from_all_chains,
        sleep_between_transfers=sleep_between_transfers
    )


async def carv_claim(wallet_info):

    chains = ["ronin", "opbnb"]

    sleep_from = 20
    sleep_to = 50

    carv_inst = Carv(wallet_info)
    await carv_inst.mint_soul(chains, sleep_from, sleep_to)


async def custom_routes(wallet_info):

    use_modules = [automatic_routes]

    sleep_from = 120
    sleep_to = 300

    random_module = False

    routes_ = Routes(wallet_info)
    await routes_.start(use_modules, sleep_from, sleep_to, random_module)


async def automatic_routes(wallet_info):

    transaction_count = 15
    cheap_ratio = 1

    sleep_from = 30000
    sleep_to = 70000

    use_none = True
    cheap_modules = []
    expensive_modules = []

    routes_inst = Routes(wallet_info)
    await routes_inst.start_automatic(transaction_count, cheap_ratio,
                                      sleep_from, sleep_to,
                                      cheap_modules, expensive_modules,
                                      use_none)


# -------------------------------------------- NO NEED TO SET UP MODULES
