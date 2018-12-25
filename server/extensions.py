from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

cors = CORS()
jwt = JWTManager()
swagger = Swagger()
db = SQLAlchemy()
