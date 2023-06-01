class Config(object):
    DEBUG = True
    TESTING = False

OPENAI_KEY = 'add your key here'

CHAT_MODEL="gpt-3.5-turbo"

DEFAULT_PROMPT = '''### Snowflake SQL tables, with their properties:
#BI_DWH_PROD.DM_HACKATON_V(KSNAME,COUNTRY,PRODUCT,CAMPAIGN_ID,CAMPAIGN_NAME,SPEND,DATE_YEAR,DATE_MONTH)
#PRODUCT value examples:
#Albertsons,Amazon,AmazonDSP,AmazonDSPReporting,Apple,Apple (Adquant),Baidu,CitrusAd,CityGrid,Criteo,Display, Drizly, FB, Facebook, Facebook (Adquant), GoPuff, Google, #Google (Adquant), HyVee, Instacart, Kroger, LinkedIn, Lowes, MSN, Nectar360, Petco, Pinterest, Reddit, #SamsClub, Snapchat, Snapchat (Adquant), Social2, Target, TheTradeDesk, Tiktok, Twitter, UNIVERSAL, #Unknown, Walmart, Yahoo, YahooGemini, YahooJapan, Yandex, YouTube
#DATE_MONTH values: 1,2,3,4,5,6,7,8,9,10,11,12
# Use format to TO_CHAR(DATE, '999,999,999,999') for the aggregationed fields in the SELECT clause liks SUM
# add alias to the fields query
### '''

MESSAGES = [
    {"role": "system", "content": "Act as SQL developer expert."},
    {"role": "system", "content": DEFAULT_PROMPT},
    # {"role": "assistant", "content": "{\"recipient\": \"USER\", \"message\":\"I understand.\"}."},
    ]

SNF_USER = ''
SNF_PWD = ''
SNF_ACCOUNT = ''
SNF_REGION = ''
SNF_DATABASE = ''