"""
This is the people module and supports all the REST actions for the
people data
"""

from re import A
from flask import make_response, abort
from config import db
from models import Avocado, AvocadoSchema


def read_all():
    """
    This function responds to a request for /api/avocado
    with the complete lists of avocado

    :return:        json string of list of avocado
    """
    # Create the list of people from our data
    avocado = Avocado.query.order_by().all()

    # Serialize the data for the response
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocado)
    return data