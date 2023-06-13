import os
class Config(object):
    DEBUG = True
    TESTING = False

OPENAI_KEY = os.getenv('OPENAI_KEY')

CHAT_MODEL="gpt-3.5-turbo"

DEFAULT_PROMPT_MARKETING = '''
### Snowflake SQL tables, with their properties:
#create TABLE BI_DWH_PROD.DM_HACKATON_V(
KS string,
COUNTRY string,
PRODUCT string,
CAMPAIGN_ID number,
CAMPAIGN_NAME string,
CAMPAIGN_CATEGORY string,
SPEND number,
CLICKS number,
YEAR number,
MONTH number)
#PRODUCT value examples:
Albertsons,Amazon,AmazonDSP,AmazonDSPReporting,Apple,Apple (Adquant),Baidu,CitrusAd,CityGrid,Criteo,Display, Drizly, FB, Facebook, Facebook (Adquant), GoPuff, Google, #Google (Adquant), HyVee, Instacart, Kroger, LinkedIn, Lowes, MSN, Nectar360, Petco, Pinterest, Reddit, #SamsClub, Snapchat, Snapchat (Adquant), Social2, Target, TheTradeDesk, Tiktok, Twitter, UNIVERSAL, #Unknown, Walmart, Yahoo, YahooGemini, YahooJapan, Yandex, YouTube
#MONTH values: between 1 to 12
#YEAR values: between 1900 to 2023
# add alias to the fields query
# Content will return as the SQL clause query ONLY!
'''

DEFAULT_PROMPT_JIRA = '''
### Snowflake SQL tables, with their properties:
#create TABLE BI_DWH_PROD.JI_HACKATON_V (
ISSUE VARCHAR(16777216),
CREATED TIMESTAMP_NTZ(9),
UPDATED TIMESTAMP_NTZ(9),
YEAR NUMBER,
MONTH NUMBER,
TITLE VARCHAR(16777216),
ISSUE_TYPE VARCHAR(16777216),
STATUS VARCHAR(16777216),
PROJECT VARCHAR(16777216),
TEAM VARCHAR(16777216),
CREATOR VARCHAR(16777216),
ASSIGNEE VARCHAR(16777216),
ENVIRONMENT VARCHAR(16777216),
TOTAL_SPRINTS NUMBER,
TIMETRACKING NUMBER,
PROGRESS NUMBER) 
#MONTH values: between 1 to 12
#YEAR values: between 1900 to 2023
# add alias to the fields query
# Content will return as the SQL clause query ONLY!
'''

GRAPH_PROMPT = "Act as an expert python developer and use matplotlib to genereate class by the following instructions:\
# Act as an expert data analyst to create very insighful plots from the following data:\
# data = XXXXX\
# Create python class name: 'InsightGraphs' \
# Use the package matplotlib for generating the graphs\
# The class will include 1 parameter called: 'data' which will use as data for the plots\
# The class will include 3 functions for createing plot types called:  line_plot, bar_plot and pie_plot.\
# Every function will save the graph into PNG file, in the following path: 'static/'\
# Every function will return the full path of the created PNG file.\
# Dont add plt.show() \
# Use soft colors\
# markersize = 5\
# linewidth=2.0\
# Content will include only the python code"

MESSAGES = [
    # {"role": "system", "content": "Act as SQL developer expert."},
    {"role": "system", "content": "Act as an Senior Data Analyst expert."},
    # {"role": "system", "content": DEFAULT_PROMPT_JIRA},
    ]

SNF_USER = os.getenv('SNF_USER')
SNF_PWD = os.getenv('SNF_PWD')
SNF_ACCOUNT = os.getenv('SNF_ACCOUNT')
SNF_REGION = os.getenv('SNF_REGION')
SNF_DATABASE = os.getenv('SNF_DATABASE')
SNF_SCHEMA = os.getenv('SNF_SCHEMA')