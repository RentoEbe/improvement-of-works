from ..now_time_func import GetToday
from ..decorate_log import log_decorator
import math
from datetime import date
from .save_thawingdata_in_database import save_data_of_thawing_in_database
from csv_operation import csv_operation_a, csv_operation_r

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
        print(GetToday.get_today_date_str(), "Today's thawing")
        for key, value in thaw_dict.items():
            print(f"{format(key, '^12')} : {value}")


    @classmethod
    def execution(cls):
        """
        This executes the thawing() , shaw_log() ,csv_operation    function.
        :return:
        """
        while True:
            today_date = date.today()
            weekday = today_date.weekday()
            int_date = int(today_date.strftime("%Y%m%d"))

            try:
                loaf = int(input("input the number of loafs:"))
                sausage = int(input("input the number of sausages:"))
                check = input(f"loafs:{loaf} sausages:{sausage}? y/n:")
                if check != "y":
                    raise SyntaxError # *******************いまはこうしているここもっといい書き方あるでしょう
            except ValueError:
                print("value error. try again")

            except SyntaxError:
                print("try again")
            else:
                thawing = cls(loaf, sausage)
                thawing.thawing()
                thawing.show_log()
                save_data_of_thawing_in_database(int_date, weekday, thawing.loaf, thawing.sausage)
                csv_operation_a(int_date, weekday, thawing.loaf, thawing.sausage)
                csv_operation_r()

                print("データベースへの登録が完了しました。")
                break





