from tabulate import tabulate

from database.models import Crypto, News
from database.db import session

from logger import get_logger

logger = get_logger(__name__)

a = session.query(Crypto).filter(Crypto.id == 1).first()


def get_coin_by_name(name):
    try:
        headers = ['Name', 'Price', '24h %']
        rows = []
        coin_rows = session.query(Crypto).filter(Crypto.name.like(f'{name}%')).order_by(Crypto.id)
        if coin_rows:
            for row in coin_rows:
                rows.append([row.name, row.price, row.percent_change_24h])
            table = tabulate(rows, headers=headers)
            return True, table
        else:
            return False, ""
    except Exception as err:
        logger.error(f'[ERROR] {err}')
        return False, ""


def rising_coins():
    try:
        headers = ['Name', 'Price', '24h %']
        rows = []
        coin_rows = session.query(Crypto).order_by(Crypto.percent_change_24h.desc()).limit(5)
        if coin_rows:
            for row in coin_rows:
                rows.append([row.name, row.price, row.percent_change_24h])
            table = tabulate(rows, headers=headers)
            return True, table
        else:
            return False, ""
    except Exception as err:
        logger.error(f'[ERROR] {err}')
        return False, ""


def decreasing_coins():
    try:
        headers = ['Name', 'Price', '24h %']
        rows = []
        coin_rows = session.query(Crypto).order_by(Crypto.percent_change_24h).limit(5)
        if coin_rows:
            for row in coin_rows:
                rows.append([row.name, row.price, row.percent_change_24h])
            table = tabulate(rows, headers=headers)
            return True, table
        else:
            return False, ""
    except Exception as err:
        logger.error(f'[ERROR] {err}')
        return False, ""


def get_news():
    try:
        news = []
        news_rows = session.query(News).limit(5)
        for new in news_rows:
            news.append(f"{new.title}\n\n{new.text}\n\nSource: {new.source} ({new.link}) \n {new.date}")
        return news
    except Exception as err:
        logger.error(f'[ERROR] {err}')
        return False, ""


def crypto_exchanges():
    exchanges = [
        f"Binance\nScore: 9.9\nAbout\nBinance is the world’s largest crypto exchange by trading volume, with $76 billion daily trading volume on Binance exchange as of August 2022, and 90 million customers worldwide. The platform has established itself as a trusted member of the crypto space, where users can buy, sell and store their digital assets, as well as access over 350 cryptocurrencies listed and thousands of trading pairs. The Binance ecosystem now comprises of Binance Exchange, Labs, Launchpad, Info, Academy, Research, Trust Wallet, Charity, NFT and more.\n\nhttps://www.binance.com/",
        f"Coinbase Exchange\nScore: 8.5\nAbout\nCoinbase Exchange is a US-based crypto trading and investment platform where users can easily buy, sell, exchange and store cryptocurrencies. The platform is intuitive and beginner-friendly with support for basic transactions, digital wallet, and PayPal withdrawals. For more advanced traders, Coinbase Pro offers more professional trade execution and lower fees. However, in June 2022, the company announced that Coinbase Pro will be phased out and all users will have access to the “Advanced Trade” feature on the main app.\n\nhttps://exchange.coinbase.com",
        f"Kraken\nScore: 8.1\nAbout\nKraken is a US-based cryptocurrency exchange where users can buy, sell and trade various assets with relatively low commissions. Clients can also earn rewards through coin staking. The exchange has a leading level euro volume and liquidity and allows users to trade over 100 crypto assets and 7 fiat currencies, including USD, CAD, EUR, GBP, JPY, CHF and AUD, on-the-go with a web platform and mobile apps.\n\nhttps://www.kraken.com",
        f"KuCoin\nScore: 7.4\nAbout\nKuCoin is a cryptocurrency exchange built with the mission to “facilitate the global free flow of digital value.” It claims to have an emphasis on intuitive design, simple registration process and high level of security. The platform supports futures trading, a built-in P2P exchange, the ability to purchase cryptocurrencies with a credit or debit card, and instant exchange services.\nAlso known as “people's exchange”, the platform facilitated 1.2 trillion in lifetime trading volume and supports over 20 million users worldwide. The company claims to offer technology-driven trading products and the KuCoin ecosystem, which encompasses the KuCoin community and is built around the KuCoin token (KCS).\n\nhttps://www.kucoin.com",
        f"Bybit\nScore: 7.1\nAbout\nBybit is a cryptocurrency centralized exchange (CEX) that offers a professional platform featuring an ultra-fast matching engine, quality customer service and multilingual community support for crypto traders of all levels. Established in March 2018, Bybit currently serves more than 10 million users and institutions offering access to over 100 assets and contracts across Spot and crypto derivatives like Futures and Options, launchpad projects, earn products, an NFT Marketplace and more. Bybit is a proud partner of Formula One racing team, Oracle Red Bull Racing, esports teams NAVI, Astralis, Alliance, Virtus.pro, Made in Brazil (MIBR), City Esports, and Oracle Red Bull Racing Esports, and association football (soccer) teams Borussia Dortmund and Avispa Fukuoka.\n\nhttp://www.bybit.com/", ]
    return exchanges


def about_author():
    linkdin = "https://www.linkedin.com/in/andrii-svitelskyi-2a4775262/"
    github = "https://github.com/andriyseeker22856"
    author = f"Hi, I am Andii\nHere you can learn more about me: {linkdin}\n\nMy portfolio: {github}"
    return author


def about_bot():
    bot = f"Crypto Analytics\nHere you can get information about cryptocurrency rates, their fall and rise; " \
          f"and last news"
    return bot
