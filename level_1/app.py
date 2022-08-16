from flask import (
    Flask, 
    request
)

from lib.exceptions import LogException
from lib.logs import (
    parse_log_to_dict,
    save_log
)


PARSED_DIR = 'parsed'

app = Flask(__name__)

@app.post('/')
def handle_log():
    try:
        log = parse_log_to_dict(log=request.json['log'])
        save_log(log, destination_dir=PARSED_DIR)
        return (request.json, 201)
    except LogException as e:
        return (f'LogException: {e}', 400)

if __name__ == '__main__':
    app.run(debug=True)