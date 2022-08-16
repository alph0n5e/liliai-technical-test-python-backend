# Level 1

## Notes

- Python 3.7 (-> virtual env)
- Flask? (Django probably overkill)
- Docker image


## ToDos

- [x] HTTP Server
- [x] POST -> write to local file
- [x] test log parsing
- [x] Containerize (+ volume ?)
- [x] Makefile
- [ ] Serve prod app using gunicorn workers instead of Flask dev server

# Level 2

## Notes

- Redis => docker-compose Architecture to interop with app
- Long running process: use Celery task to do it asynchronously
- Celery: second Redis queue for tasks?

## ToDos

- [x] Docker-compose Redis + app
- [ ] Run long process async
