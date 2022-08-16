from lib.exceptions import LogException


def parse_log_to_dict(log: str) -> dict:
    """
    Parse log string to dictionary
    """
    try:
        return dict((s.split('=') for s in log.split(' ')))
    except:
        raise LogException('Input log improperly formatted')

