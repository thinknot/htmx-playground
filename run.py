# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from htmxapp import app

# Disable debug in production
if __name__ == "__main__":
    app.run(debug=True)
