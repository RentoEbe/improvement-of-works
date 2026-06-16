# We get the present year, month, and day(date).
#Also there are various function about time in module
import datetime
class GetToday:
    today = datetime.datetime.now() # This is object. print(today) result is 2026-06-16 00:13:41.525251
    date_list = today.__str__().split(" ")

    @classmethod
    def get_today_date_int(cls):
        """
        get today's date:
        :return: today's date which type is integer ex)20261023
        """
        today_date = int(cls.date_list[0].replace("-", ""))
        return today_date

    @classmethod
    def get_today_date_str(cls):
        """
        get today's day:
        :return: ex) if today is 6/15, result is "2026/6/15"
        """
        date_str = ("{0.year}{1}{0.month}{1}{0.day}/{2}".format(cls.today, "/", cls.get_week_day_ja()))
        return date_str

    @classmethod
    def get_week_day_ja(cls):
        """
        get today's day of week:
        :return: today's day of week which type is integer
                 0 -> Monday
                 1 -> Tuesday
                 2 -> Wednesday
                 3 -> Thursday
                 4 -> Friday
                 5 -> Saturday
                 6 -> Sunday
        """
        week_day_list_ja = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return week_day_list_ja[cls.today.weekday()]

    