Python Assorted code
====================

Miscellaneous Python code snippets and experiments.

### Individual files / Scripts
* `\change_detector.py`: Given a list of urls fetches their HTML, stores a CRC32 and upon next run will compare stored CRC with new one to see if has changed. Call me lazy ;)
* `\list_search.py`: Search for a command line provided string in all txt files of folder where script is launched. Made for personal use as I keep my catalog of games, movies, etc. in text files. Sample text files format:
```
0   /media/kartones/pre1/test 1/blablabla
123 /media/kartones/pre1/test 1/blablabla2
0   /media/kartones/pre1/test 1
0   /media/kartones/pre1/test 2/blablabla
0   /media/kartones/pre1/test.1/blablabla
```

### Folders / Projects
* `\pelican`: Plugins for the Pelican static site generator tool.
* `\rpg-combat-kata`: A coding kata. I went for an inside-out TDD approach, building only the minimal needed functionality.
* `\shopping-lists`: A pet project to easily manage shopping lists. Mobile-friendly although nothing too complex nor feature-full. See its README for more details.
* `\twitter-purge`: Script to delete your tweets older than X days (5 with sample config). Best setup as a cron job to run hourly or daily.
* `\weather-email`: Small script that fetches Madrid's current weather info and sends it via email. Perfect to be setup as a cron job at 7AM to remind me daily of the weather before I head out for work.
