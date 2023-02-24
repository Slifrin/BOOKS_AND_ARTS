"""
    https://www.youtube.com/watch?v=QF-qHWekhxw&list=WL&index=4
"""

import time
import uuid
import random

from flask import Flask, Response, stream_with_context


app = Flask(__name__)

@app.route("/very_large_request/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount:int):
    """Returns N rows of data"""
    def f():
        """Generator of the mock data."""
        for i in range(rowcount):
            time.sleep(.01)
            transaction_id = uuid.uuid4()
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            print(transaction_id)
            yield f"('{transaction_id}', '{uid}', {amount})\n"
    return Response(stream_with_context(f()))

if __name__ == '__main__':
    app.run(debug=True)