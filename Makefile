
run:
	gunicorn -c gunicorn_config.py src.app:app

