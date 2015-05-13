# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment

css = Bundle(
    "libs/skeleton/css/skeleton.css",
    "libs/skeleton/css/normalize.css",
    "css/style.css",
    filters="cssmin",
    output="public/css/common.css"
)

js = Bundle(
    "libs/d3/d3.js",
    "libs/jQuery/dist/jquery.js",
    "libs/underscore/underscore.js",
    "js/plugins.js",
    filters='jsmin',
    output="public/js/common.js"
)

assets = Environment()

assets.register("js_all", js)
assets.register("css_all", css)
