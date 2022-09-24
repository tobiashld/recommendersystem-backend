#!/bin/sh
gunicorn --chdir app main:app -w 2 -b 0.0.0.0:80