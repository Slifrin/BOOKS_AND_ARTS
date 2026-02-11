# These are the necessary import declarations
from opentelemetry import trace
from opentelemetry import metrics

from random import randint
from flask import Flask, request
import logging

tracer = trace.get_tracer("diceroller.tracer")
meter = metrics.get_meter("diceroller.meter")

roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def roll():
    return randint(1, 6)


@app.route("/rolldice")
def roll_dice():
    with tracer.start_as_current_span("roll") as roll_span:
        player = request.args.get("player", default=None, type=str)
        result = str(roll())
        roll_span.set_attribute("roll.value", result)
        roll_counter.add(1, {"roll.value": result})
        if player:
            logger.warning("BLA %s is rolling the dice: %s", player, result)
        else:
            logger.warning("BLA Anonymous player is rolling the dice: %s", result)
        return result


@app.route("/")
def hello():
    return "Hello world!"


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)
