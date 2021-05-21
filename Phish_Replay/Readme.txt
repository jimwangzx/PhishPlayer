The modified files are all found in the perf folder

JSON Data File : perf/page_sets/RecordedData.json

Page_Set: perf/page_sets/Replay_page.py

Helper class : perf/page_sets/replay_helpers/ReplayWrapper.py


Download the chromium telemtry source code and replace the perf folder wth this folder contents

command to replay the web page

python record_wpr --browser=system replay_page_set


