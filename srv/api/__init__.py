from flask_mongorest import MongoRest
from app import app


api = MongoRest(app)

import models
import routes