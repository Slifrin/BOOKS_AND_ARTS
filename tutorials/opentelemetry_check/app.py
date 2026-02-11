"""
Docstring for tutorials.opentelemetry_check.app
https://opentelemetry.io/docs/languages/python/getting-started/
"""

from random import randint
from flask import Flask, request

import logging

from opentelemetry import trace

tracer = trace.get_tracer("diceroller.tracer")

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/rolldice")
def role_dice():
    logger.info(f"{request}")
    player = request.args.get("player", default=None, type=str)
    result = str(roll())
    if player:
        logger.warning("%s is rolling the dice: %s", player, result)
    else:
        logger.warning("Anonymous player is rolling the dice: %s", result)
    return result


def roll():
    return randint(1, 6)


@app.route("/rolledice2")
def role_dice2():
    return str(roll2())


def roll2():
    with tracer.start_as_current_span("roll") as roll_span:
        res = randint(1, 6)
        roll_span.set_attribute("roll.value", res)
        return res
