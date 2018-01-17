import pytz
from datetime import datetime

# def time_deadline():
#     today = datetime.today()
#     end = {
#         'forenoon': '11:59:59',
#         'afternoon': '17:59:59',
#         'evening': '23:59:59'
#     }
#     forenoon = '{}-{}-{} {}'.format(today.year, today.month, today.day, end.get('forenoon'))
#     afternoon = '{}-{}-{} {}'.format(today.year, today.month, today.day, end.get('afternoon'))
#     evening = '{}-{}-{} {}'.format(today.year, today.month, today.day, end.get('evening'))
#     return [datetime.strptime(t, "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.timezone('Asia/Shanghai')) for t in
#             [forenoon, afternoon, evening]]
#
#
# if __name__ == '__main__':
#     print(time_deadline())

import math


def a(m):
    hour = int(m / 60)
    minutes = m % 60
    return hour, minutes


if __name__ == '__main__':
    a = a(0)
    print(a)
