from lib.logs import parse_log_to_dict


def test_parse_log_to_dict():
    assert parse_log_to_dict('a=1 b=2') == {'a': '1', 'b': '2'}