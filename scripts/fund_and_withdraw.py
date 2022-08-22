from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEnteranceFee()
    print(f"current entrance fee{entrance_fee}")
    print("Funding...")
    fund_me.fund(
        {
            "from": account,
            "value": 10 * 10**18,
            "allow_revert": True,
            "gas_limit": 2074044,
        }
    )


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
