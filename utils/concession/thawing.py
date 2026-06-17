from ..now_time_func import GetToday
from ..decorate_log import log_decorator
import math

class Thawing:
    def __init__(self, loaf, sausage):
        self.loaf = loaf
        self.sausage = sausage
        self.loaf_bags = 0
        self.sausage_bags = 0


    def thawing(self):
        # 入力値が割り切れないときは、解凍数が目安を上回るために整数値+1袋する
        number_of_loaf_bags = math.ceil(self.loaf / 6)
        number_of_sausage_bags = math.ceil(self. sausage / 10)

        self.loaf_bags = number_of_loaf_bags
        self.sausage_bags = number_of_sausage_bags

    @log_decorator
    def show_log(self):
        """
        it prints out the today's thawing and sausage bags
        :return: None
        """
        thaw_dict = {"sausage": self.sausage, "sausage_bags": self.sausage_bags, "loaf": self.loaf, "loaf_bags": self.loaf_bags}
        print(GetToday.get_today_date_str())
        for key, value in thaw_dict.items():
            print(f"{format(key, '^12')} : {value}")

    def save(self):
        """
        We save the number of preparation of loaves and sausages by the day on database
        :return:
        """



