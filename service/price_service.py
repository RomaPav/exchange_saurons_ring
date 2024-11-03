import random


class PriceService:
    @staticmethod
    def get_price(gold_price, silver_price, bronze_price):
        return {
            "gold": PriceService.get_gold_price(gold_price),
            "silver": PriceService.get_silver_price(silver_price),
            "bronze": PriceService.get_bronze_price(bronze_price)
        }

    @staticmethod
    def get_gold_price(gold_price):
        max_price = 4400
        min_price = 3400
        if gold_price < min_price or gold_price > max_price:
            return random.randint(min_price, max_price)
        elif (gold_price - 10) > min_price and (gold_price + 10) < max_price:
            return random.randint(gold_price - 10, gold_price + 10)
        elif (gold_price - 10) <= min_price:
            return random.randint(min_price, gold_price + 10)
        elif (gold_price + 10) >= max_price:
            return random.randint(gold_price - 10, max_price)
        elif gold_price < min_price or gold_price > max_price:
            return random.randint(min_price, max_price)

    @staticmethod
    def get_silver_price(silver_price):
        max_price = 3400
        min_price = 2400
        if silver_price < min_price or silver_price > max_price:
            return random.randint(min_price, max_price)
        elif (silver_price - 10) > min_price and (silver_price + 10) < max_price:
            return random.randint(silver_price - 10, silver_price + 10)
        elif (silver_price - 10) <= min_price:
            return random.randint(min_price, silver_price + 10)
        elif (silver_price + 10) >= max_price:
            return random.randint(silver_price - 10, max_price)


    @staticmethod
    def get_bronze_price(bronze_price):
        max_price = 2400
        min_price = 1400
        if bronze_price < min_price or bronze_price > max_price:
            return random.randint(min_price, max_price)
        elif (bronze_price - 10) > min_price and (bronze_price + 10) < max_price:
            return random.randint(bronze_price - 10, bronze_price + 10)
        elif (bronze_price - 10) <= min_price:
            return random.randint(min_price, bronze_price + 10)
        elif (bronze_price + 10) >= max_price:
            return random.randint(bronze_price - 10, max_price)
