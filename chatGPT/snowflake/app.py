from flask import Flask, render_template, request
import snowflake.connector
import matplotlib as mpl
mpl.use('Agg')  # Use the Agg backend
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import openai
import config
import string

app = Flask(__name__)

# Set up OpenAI API credentials and instructions
openai.api_key = config.OPENAI_KEY
CHAT_MODEL = config.CHAT_MODEL
DEFAULT_PROMPT = config.DEFAULT_PROMPT
MESSAGES = config.MESSAGES
SNF_USER = config.SNF_USER
SNF_PWD = config.SNF_PWD
SNF_ACCOUNT = config.SNF_ACCOUNT
SNF_REGION = config.SNF_REGION
SNF_DATABASE = config.SNF_DATABASE
SNF_SCHEMA = config.SNF_SCHEMA


def convert_to_query(query):
    if '```' in query:
        sqlQuery = f"{query.split('```')[1]};"
    else:
        sqlQuery = f"SELECT {query.split('SELECT')[1].split(';')[0]};"

    return sqlQuery

def generate_response(prompt):
    completion = openai.ChatCompletion.create(
        model=CHAT_MODEL,
        max_tokens=2048,
        temperature=0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"],
        messages=MESSAGES + [{"role": "user", "content": prompt}],
        )

    response = completion.choices[0].message.content
    return response


def snowflake_connector(user, password, account, region, database, schema):
    snowflakeClient = snowflake.connector.connect(
        user = user,
        password = password,
        account = account,
        region = region,
        database = database,
        schema = schema
        )
    return snowflakeClient


def exec_query(query):
    if 'select' in query.lower():
        query = convert_to_query(query)
        snfClient = snowflake_connector(user=SNF_USER,
                        password = SNF_PWD,
                        account=SNF_ACCOUNT,
                        region = SNF_REGION,
                        database = SNF_DATABASE,
                        schema = SNF_SCHEMA).cursor()
        cursor = snfClient.execute(query)
        columns = tuple([string.capwords(column[0].replace('_', ' ')) for column in cursor.description])
        response = []
        response.append(tuple(columns))
        data = cursor.fetchall()
        response = response + data
        print(f"********************** {response}")
        return response
    else:
        return query


def results_to_string(results):
    if results:
        data = ''
        for row in results:
            row_to_list = [str(r) for r in row]
            data += '<br>' + ' | '.join(row_to_list)
        return data
    else:
        return 'No results found.'
    

def create_plot(data):
    # Convert data into DataFrame
    columns = list(data[0])
    df = pd.DataFrame(data[1:], columns=data[0])

    bar_colors = ['#575f6f']
    # Create bar plot
    # plt.plot(df['Month'], df['Total Spend'], color=bar_colors)
    # plt.plot(df['Month'], df['Total Spend'])
    # plt.xlabel('Month')
    # plt.ylabel('Total Spend')
    x = columns[0]
    y = columns[1]
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')
    mpl.rcParams['font.size'] = 10

    plt.plot(df[x], df[y], linewidth=2.0, color='#571270', marker='o')
    plt.ticklabel_format(style='plain', axis='y')
    plt.xlabel(x)
    plt.ylabel(y)
    # plt.tight_layout()
    plt.legend()
    plt.title(x)

    graph_path = 'static/graph1.png'
    plt.savefig(graph_path)
    plt.close() 
    return graph_path


# Route for the home page
@app.route('/')
def home():

    
    # graph_path=create_plot(data=data)
    graph_path=''

    return render_template('index.html', graph_path=graph_path)

# Route for chat interactions
@app.route('/chat', methods=['POST'])
def chat():
    graph_path=''
    user_message = request.form['user_message']
    prompt = f'User: {user_message}\nChatGPT: '    
    sqlQuery = generate_response(prompt)
    print(f"========>>> {sqlQuery}")
    response = exec_query(sqlQuery)
    
    # validate AI response for query or language
    if 'select' in sqlQuery.lower():
        results = results_to_string(results=response)
        graph_path=create_plot(data=response)
    else:
        results = response
    return {'response': results, 'graph_path' : graph_path}

if __name__ == '__main__':
    app.run()
