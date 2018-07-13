# Introduction to Text Mining through Twitter
An introductory text mining experiment using the Twitter API

# Getting Twitter API Keys
- Visit https://apps.twitter.com/ and log in to your twitter account
- Click "Create New App"
- Fill out the form, agree to the terms, and click "Create your Twitter application"
- Click on "API keys" tab, and copy your "API key" and "API key secret"
- Scroll down, click "Create my access token", and copy your "Access token" and "Access token secret"

# Create your config file
- Run the command `cp ./src/config-default.ini ./src/config.ini`
- You will need to input your API Keys into `config.ini`

# Running the Experiment
The first part of the experiment involves collecting data. To do this, we will need to run the following line in your terminal:
  python twitter_streaming.py > twitter_data.txt
To get a meaningful sample, you may need to run the program for a while (two days is recommended). After you have collected your data, you can run the next program in the src folder with the following command:
  python text_mining.py
  
# Understanding the Results
