
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

__import__('ItIsTasty.database')
__import__('ItIsTasty.resource')