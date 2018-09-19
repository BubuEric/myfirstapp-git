from app.api.images import images
from flask import jsonify


@images.route('/')
def images_index():
    return 'imsges api'
