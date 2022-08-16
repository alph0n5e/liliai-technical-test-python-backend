import json

from os import makedirs
from os.path import (
    dirname,
    exists,
    join
)

from lib.exceptions import LogException

BASE_DIR = dirname(dirname(__file__))

def parse_log_to_dict(log: str) -> dict:
    """
    Parse log string to dictionary
    """
    try:
        return dict((s.split('=') for s in log.split(' ')))
    except:
        raise LogException('Input log improperly formatted')


def save_log(
    log: dict, 
    destination_dir: str
):
    """
    Write log dictionary to destination directory
    """
    try:
        id = log['id']
    except KeyError:
        raise LogException('Expected log to contain an \'id\' field')
    
    dest_dir_path = join(BASE_DIR, destination_dir)
    if not exists(dest_dir_path):
        makedirs(dest_dir_path)
    
    with open(join(dest_dir_path, f'#{id}.json'), 'w+') as f:
        json.dump(log, f, indent=4)