from flask import Blueprint

images = Blueprint('images', __name__)

import app.api.images.views