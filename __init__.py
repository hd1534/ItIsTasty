
from flask import Flask

app = Flask(__name__)

__import__('itIsTasty.database')
__import__('itIsTasty.resource')