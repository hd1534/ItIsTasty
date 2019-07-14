
from flask import Flask

app = Flask(__name__)

__import__('hackathon.database')
__import__('hackathon.resource')