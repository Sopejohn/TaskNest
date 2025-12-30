#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python planner/manage.py collectstatic --no-input
python planner/manage.py migrate
