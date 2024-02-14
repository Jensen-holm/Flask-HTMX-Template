from src.blueprints.login import login
from src.blueprints.index import index

from flask import Blueprint

blueprints: list[Blueprint] = [
    login,
    index,
]
