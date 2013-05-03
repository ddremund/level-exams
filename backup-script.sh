mongoexport --db leveling --collection test_types -o ~/test_types-backup.json
mongoexport --db leveling --collection saved_tests -o ~/saved_tests-backup.json
mongoexport --db leveling --collection users -o ~/users-backup.json
mongoexport --db leveling --collection preferences -o ~/preferences-backup.json
mongoexport --db leveling --collection questions -o ~/questions-backup.json
