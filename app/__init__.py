from flask import Flask

from app.dashboard import dashboard

def create_server():
    # environment_check()
    server = Flask(__name__)
    dashboard(server)
    return server