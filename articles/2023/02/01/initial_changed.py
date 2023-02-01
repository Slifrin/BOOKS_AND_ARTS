import statistics
from dataclasses import dataclass
from typing import Callable
from functools import partial, partialmethod

from exchange import Exchange


TraidingStrategyFunction = Callable[[list[int]], bool]


def shoudl_buy_avg_closure(window_size: int) -> TraidingStrategyFunction:
    def should_buy_avg(prices: list[int]) -> bool:
        list_window = prices[-window_size:]
        return prices[-1] < statistics.mean(list_window)
    return should_buy_avg

def should_sell_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] > statistics.mean(list_window)


def should_buy_min_max(prices: list[int], minimum_price: int) -> bool:
    return prices[-1] < minimum_price


def shoudl_sell_min_max_closure(max_price: int) -> TraidingStrategyFunction:
    def should_sell_min_max(prices: list[int]) -> bool:
        return prices[-1] > max_price
    return should_sell_min_max


@dataclass
class TradingBot:

    exchange: Exchange
    buy_strategy: TraidingStrategyFunction
    sell_strategy: TraidingStrategyFunction

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy =  self.buy_strategy(prices)
        should_sell = self.sell_strategy(prices)
        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}.")



def main() -> None:
    print(f'Hello main from : {__file__}')
    exchange = Exchange()
    exchange.connect()


    bot = TradingBot(exchange, shoudl_buy_avg_closure(4), shoudl_sell_min_max_closure(35_000_00))
    bot.run("BTC/USD")

    # neet thing :)
    buy_strategy = partial(should_buy_min_max, minimum_price=31_000_00)
    sell_strategy = partial(should_sell_avg, window_size=4)

    bot = TradingBot(exchange, buy_strategy, sell_strategy)
    bot.run("BTC/USD")

if __name__ == '__main__':
    main()



