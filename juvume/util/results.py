FAKER_RESULTS = dict(
    name = "Barney",
    date_label = "Feburary 20 - 24",
    treatment = "Massage Therapy",
    day_labels = dict(
        d0="mon 2/20",
        d1="tue 2/21",
        d2="wed 2/22",
        d3="thu 2/23",
        d4="fri 2/24",
        ),
    results = dict(
        morning_1 = [
            dict(time='9:30 am', price=123),
            dict(time='12:00 am', price=12),
            ],
        morning_2 = [],
        morning_3 = [],
        morning_4 = [],
        morning_5 = [],

        afternoon_1 = [
            dict(time='9:30 am', price=123),
            dict(time='12:00 am', price=12),
            ],
        afternoon_2 = [
                             {'price': 52, 'time': '12:15 pm'},
                             {'price': 52, 'time': '12:30 pm'},
                             {'price': 52, 'time': '12:45 pm'},
                             {'price': 52, 'time': '01:00 pm'},
                             {'price': 52, 'time': '01:15 pm'},
                             {'price': 52, 'time': '01:30 pm'},
                             {'price': 52, 'time': '01:45 pm'},
            ],
        afternoon_3 = [],
        afternoon_4 = [],
        afternoon_5 = [],

        evening_1 = [
            dict(time='9:30 am', price=123),
            dict(time='12:00 am', price=12),
            ],
        evening_2 = [
                           {'price': 52, 'time': '03:00 pm'},
                           {'price': 52, 'time': '03:15 pm'},
                           {'price': 52, 'time': '03:30 pm'},
                           {'price': 52, 'time': '04:15 pm'},
                           {'price': 52, 'time': '04:30 pm'},
                           {'price': 52, 'time': '04:45 pm'},
                           {'price': 52, 'time': '05:00 pm'},
                           {'price': 52, 'time': '05:15 pm'},
                           {'price': 52, 'time': '04:00 pm'},
            ],
        evening_3 = [],
        evening_4 = [],
        evening_5 = [],
        ),
    )

FAKE_RESULTS = {
    '03-05-2012': [
        {'name': "Greg's Hair Salon",
                 'results': [{'discount': 120,
                              'name': 'The SUper Awesome Cut',
                              'price': '1170'},
                             {'discount': 1110,
                              'name': 'The SUper Awesome Cut II',
                              'price': '1145'}]},
        {'name': 'Hair Salon',
                 'results': [
                             {'discount': 1110,
                              'name': 'The SUper Awesome Cut II',
                              'price': '1145'}]},
                             ]}
