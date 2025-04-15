import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def info_list():
    return [{'id': 41428829, 'state': 'EXECUTED',
             'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED',
             'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED',
             'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED',
             'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize("state, expected", [
    ('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
])
def test_filter_by_state(info_list, state, expected):
    assert filter_by_state(info_list, state) == expected


def test_filter_by_state_executed(info_list):
    with pytest.raises(ValueError):
        filter_by_state([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                        state='EXECUTED')


def test_filter_by_state_canceled(info_list):
    with pytest.raises(ValueError):
        filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
                        state='CANCELED')


def test_filter_by_state_typo_in_state(info_list):
    with pytest.raises(ValueError):
        filter_by_state([{'id': 41428829, 'stete': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
                        state='EXECUTED')


@pytest.fixture
def data():
    return [[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
            ]


@pytest.mark.parametrize("data, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
])
def test_sort_by_date(data, expected):
    assert sort_by_date(data) == expected


def test_sort_by_date_wrong_distribution(data):
    with pytest.raises(TypeError):
        sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': 12345},  # Некорректный формат
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])


def test_sort_by_date_same_data(data):
    with pytest.raises(ValueError):
        sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}])
