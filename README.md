Compare Candidates' Online Personalities
=========================================

Python script that uses the Watson Personality Insight API to compare candidates' (or any two people's) personalities based on their last 200 tweets.


Installation and configuration
----------------------------
(1) Clone the repository and cd into it
(2) Make a copy of `settings_template.py` and rename it to `settings.py`
(3) Fill in the credentials in `settings.py`. You'll need Twitter API and Watson API creds.
(4) Create and activate a virtual environment named `venv` (this is to match our .gitignore file - if you want to name your environment something else, just rename it in the .gitignore as well).
(5) Run `pip install -r requirements.txt` to set up the virtual environment.



Running the script
------------------

(1) Run `python compare.py`

(2) When prompted, enter the two candidates' Twitter handles (without the '@' sign)

(3) Here's a [Guide to understanding the numeric results outputted by this script](https://console.bluemix.net/docs/services/personality-insights/numeric.html#numeric)


Next features to be added
-------------------------
+ Choose which traits you want to compare
+ Improve printout readability for CLI
+ Develop single-page web/phone version