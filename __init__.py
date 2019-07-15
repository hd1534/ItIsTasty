
from flask import Flask

app = Flask(__name__)

__import__('ItIsTasty.database')
__import__('ItIsTasty.resource')