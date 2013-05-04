#!/bin/sh

mongoimport --db leveling --collection users < ./users.json
mongoimport --db leveling --collection preferences < ./preferences.json

