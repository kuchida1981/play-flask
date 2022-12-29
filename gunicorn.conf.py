wsgi_app = "app:create_app()"
reload = True
bind = "unix:///run/gunicorn/gunicorn.sock"
