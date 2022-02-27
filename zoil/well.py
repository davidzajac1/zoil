from random import randint, uniform
from datetime import datetime, timedelta
from math import e


def __exponential(qi, d, t):
    return qi * (e ** (-d * t))


def __rand_offset(num, percent):
    return round(num + uniform(-percent * num, percent * num), 1)


def get_production_data(granularity='monthly'
    , start_date=datetime(year=1950,month=1,day=1)
    , end_date=datetime.now()
    , qio_min=100,qio_max=2500
    , qig_min=500,qig_max=5000
    , qiw_min=100,qiw_max=2500):

    """
    get_production_data generates a dictionary containing random production data.

    :param granularity: 'monthly' | 'daily' Granularity of data
    :param start_date: The start date of the production history
    :param end_date: The end date of the production history
    :param qio_min: The minimum initial oil production rate
    :param qio_max: The maximum initial oil production rate
    :param qig_min: The minimum initial gas production rate
    :param qig_max: The maximum initial gas production rate
    :param qiw_min: The minimum initial water production rate
    :param qiw_max: The maximum initial water production rate
    :return: A dictionary containing random production data
    """

    data = {'date': [],
            'oil': [],
            'gas': [],
            'water': []}

    length = randint(20, 50) * 365

    qio = randint(qio_min, qio_max)
    qig = randint(qig_min, qig_max)
    qiw = randint(qiw_min, qiw_max)

    do = randint(25,75)/100000
    dg = do + randint(-10,10)/100000
    dw = do + randint(-10,10)/100000

    date = timedelta(randint(0,(end_date - start_date).days)) \
        + start_date

    shut_in = False
    shut_in_count = 0
    for day in range(length):

        if shut_in is True:
            if randint(0,20) == 0:
                shut_in = False
                shut_in_count = 20

        if randint(0,400) == 0:
            shut_in = True

        qfo = __exponential(qio, do, day)
        qfg = __exponential(qig, dg, day)
        qfw = __exponential(qiw, dw, day)

        if shut_in is False:

            qo = __rand_offset(qfo, 0.1) * (1 + shut_in_count / 100)
            qg = __rand_offset(qfg, 0.1) * (1 + shut_in_count / 100)
            qw = __rand_offset(qfw, 0.1) * (1 + shut_in_count / 100)

            if shut_in_count != 0:
                shut_in_count -= 1
        else:
            qo = 0
            qg = 0
            qw = 0

        if granularity == 'daily' or date.day == 1:
            data['date'].append(date)
            data['oil'].append(qo)
            data['gas'].append(qg)
            data['water'].append(qw)

        date += timedelta(1)

        if date > end_date or (qfo < 5 and qfg < 50):
            break

    return data
