#!/bin/sh

mongoimport --db leveling --collection test_types < ~/test_types-backup.json
mongoimport --db leveling --collection saved_tests < ~/saved_tests-backup.json
mongoimport --db leveling --collection users < ~/users-backup.json
mongoimport --db leveling --collection preferences < ~/preferences-backup.json
mongoimport --db leveling --collection questions < ~/questions-backup.json
