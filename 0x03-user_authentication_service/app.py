#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, jsonify
from typing import List, Tuple
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page(methods: List[str] = ['GET']) -> Tuple[dict, int]:
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
