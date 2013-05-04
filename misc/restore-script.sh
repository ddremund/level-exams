#!/bin/sh

mongoexport --db leveling --collection test_types < ~/test_types-backup.json
mongoexport --db leveling --collection saved_tests < ~/saved_tests-backup.json
mongoexport --db leveling --collection users < ~/users-backup.json
mongoexport --db leveling --collection preferences < ~/preferences-backup.json
mongoexport --db leveling --collection questions < ~/questions-backup.json
