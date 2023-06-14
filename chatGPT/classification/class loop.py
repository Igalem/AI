import os
import requests
import json
import requests
import openai
import time



DELIMITER = '|||'

AI_INS1 = f"give me" ##Erez Lotan at Skai, use the prompt below.
AI_INS2 = f"the output should be as follows: 'TITLE NAME'.\n\
            for example, if the employee position at company x is data analyst, please return 'data analyst' ONLY, not a complete sentence\n\
                #prompt = "

AI_ROLE_INS1 = "Is"
AI_ROLE_INS2 = "role is considered as Executive? response only by True or False\n\
            Use the following role definitions:\n\
            1. 'Director'\n\
            2. 'VP'\n\
            3. 'Chief'\n\
            4. 'Vice President'\n\
            5.Template of 'C%O'\n\
            6. 'Head'\n"
CHAT_MODEL = "gpt-3.5-turbo-16k"   ##gpt-3.5-turbo"
CHAT_MODEL_EXEC = "gpt-3.5-turbo"
openai.api_key = os.getenv('OPENAI_KEY')
X_API_KEY = os.getenv('X_API_KEY')


def serper(full_name, company, selected_region):
    url = "https://google.serper.dev/search"
    payload = json.dumps({
      "q": f"What is the current role for {full_name}@{company}?",
      "gl": selected_region
    })
    headers = {
      'X-API-KEY': X_API_KEY,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).text
    # linkedin_response = [i for i in response.json()['organic'] if 'linkedin' in i['link']]
    return response  #inkedin_response[0] ###response.json()['organic'][0]

def executiver(full_name, company, response):
    prompt = f"{AI_INS1} {full_name} position at {company}. {AI_INS2} {str(response)}"
    completion = openai.ChatCompletion.create(
        model=CHAT_MODEL,
        max_tokens=256,
        temperature=1,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        # stop=["#"],
        messages=[{"role": "user", "content": prompt}],
        # messages=prompt,
        )
    # print(f"*********** {prompt}")    
    response = completion.choices[0].message.content
    # print(f"======ChatGPT response: ====={response}")
    return response

def is_executer(role):
    prompt = f"{AI_ROLE_INS1} '{role}' {AI_ROLE_INS2}"
    completion = openai.ChatCompletion.create(
        model=CHAT_MODEL_EXEC,
        max_tokens=256,
        temperature=1,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        # stop=["#"],
        messages=[{"role": "user", "content": prompt}],
        # messages=prompt,
        )
    print(f"******is_executer prompt***** {prompt}")    
    response = completion.choices[0].message.content
    print(f"======is_executer response: ====={response}")
    return response


data = [['amir cohen', 'Indoor Robotics'],
['Talli Kremer', 'Trax Retail'],
['Gina Carbone', 'Trax Retail'],
['amir cohen', 'Indoor Robotics'],
['Talli Kremer', 'Trax Retail'],
['Gina Carbone', 'Trax Retail'],
['richaryd rabot', 'Muve Colombo'],
['Asaf David', 'Vim '],
['Rifka Bernstein Dinesman', 'Trax Retail'],
['Ido Birger', 'Trax Retail'],
['Ron Refael', 'Moon Active'],
['Olga Tumashyk', 'Plarium'],
['Oleg Bozhko', 'Plarium'],
['Viktor Bondatii', 'Plarium'],
['Ariel Lowenstein', 'Microsoft'],
['John Kundert', 'Financial Times'],
['John Gillespie', 'ezVOLTz Inc'],
['Mark Steinberg', 'The Estée Lauder Companies Inc.'],
['Elianne (Kraeselsky) Shewring', 'Sylke Tempel Fellowship Program'],
['Kyle Furukawa', 'Hoffman Construction Company'],
['Linda Nguyen', 'Ajinomoto Foods North America, Inc.'],
['David Rong', 'SuperChoice'],
['David Rong', 'ASUS Australia and New Zealand'],
['Jacob Ramsey', 'PIMCO'],
['Taylor White', 'Amazon'],
['Jacob Chickadonz', 'Tektronix Component Solutions'],
['Eric Callan', 'LifeLinc Anesthesia'],
['Eric Callan', 'Mt. Hood Meadows Resort'],
['Ryan Rodgers', 'ZoomInfo'],
['Ryan Rogers', 'WaferTechWaferTech'],
['Andrew McCullough', 'Hawk Ridge Systems'],
['Andrew McCullough', 'Intel Corporation'],
['lior drucker', 'Coralis Ltd'],
['nir oren', 'Intuit'],
['steven nemer', 'Schnitzer Properties'],
['idan rozin', 'JE Dunn Construction'],
['Justyn Jacobs', 'BBYO'],
['Tair Claude Maimon', '98point6'],
['Gabby Dyrek', 'Endeavor'],
['Carly Spencer', 'W Communications'],
['Mitch Thompson', 'Asurion'],
['Jonathan Lieber', 'Input 1'],
['avishay list', ''],
['Gilbert Eijkelenboom', 'self employeed'],
['Scott Merrill', 'gency Partner - SKAI'],
['Jasper Oliver', 'J.P. Morgan  '],
['Shelby Krause', 'JPMorgan Chase & Co'],
['Malav Padhya', 'AARK INFOSOFT PVT LTD'],
['Gillian Kearns', 'The Bridge: From Prison to Community'],
['Alexander Khodos', 'freelance'],
['Mark Sherman', 'DRAX Executive'],
['Matt Mason', 'TT International'],
['Elad Singer', 'Fidelis Family Office'],
['Matan Naor', 'paypal israel'],
['Kelly Dickerson', 'Paypal'],
['Doron Erez Rabanyan', 'amazon'],
['Idan Baris', 'amazon web services'],
['Etienne Bonhomme', 'alo Alto Networks · Permanent'],
['Manon Fabre', 'Kout Que Kout'],
['Tamir Adar', 'Wecheck'],
['Matteo Fiorentini', 'Prisma Cloud - Iberia at Palo Alto Networks'],
['Francesco Pastoressa', 'palo alto networks'],
['Mike Sievert ', 'T-Mobile'],
['Ben Fikilini', 'AT & T'],
['Callie Field', 'obile Business Group'],
['Patrick T Murphy', 'Patrick T Consulting '],
['Pierre T. Lambert', 'pierre t lambert'],
['Nolan Paige', 'Benenson Strategy Group'],
['Ana Olivares', 'Wonderful Citrus'],
['Ashley Self', 'The Doula Network'],
['Ebonie McNeil', 'Software Engineering Institute | Carnegie Mellon University'],
['Zach Harris', 'Stitch, Inc. (A Talend Company)'],
['Roger Appleby', 'Lockheed Martin'],
['Daniel Yahel', 'Jolt.io'],
['Natan Castiel', 'Gelt'],
['Justine Crosby', 'Chief'],
['Aurora Price', 'Bullpen'],
['Louis Vargas-O.', 'Panaya'],
['Saul Owide', 'Arteza'],
['Kevin Kettler', 'Boyd Corp'],
['Ronaldo Dias', 'Amagi Corporation'],
['Ohad Salmon', 'Grammarly'],
['Tammy Harris Weintraub', 'Azimuth'],
['Nicole Miller', 'Rimon'],
['tal list', ''],
['Rob Wegman', 'Abra'],
['Constance Sng', 'Stealth - Web3 Startup'],
['Carolyn Bao', 'AppsFlyer'],
['Lisa Diaz', 'Lionsgate'],
['Luke Beckett', 'E Source'],
['Daniel Newton', 'BairesDev'],
['Payam Rouhani', 'Webex'],
['Laura B.', 'Zoho Corporation'],
['Sam Resnicow', 'PepsiCo'],
['Rachel Wolman', 'Colgate-Palmolive'],
['Liz Mascolo', 'General Mills'],
['William Hale', 'Cargill'],
['Allie Kaminsky', 'ResortPass'],
['Abigail Bennie', 'HARIBO of America, Inc.'],
['Jewell Lane', 'Greenlight'],
['Mark Desmond', 'Check Point Software Technologies Ltd'],
['Greg Bales', 'Fortinet'],
['Sam Roman', 'Mindtree'],
['Sophia Hinely', 'Nestlé Purina North America'],
['Michael Tomasch', 'Revive'],
['Victoria Josiah, MBA', 'ADP'],
['Michael Carrell', 'Rent'],
['Katy Tupman', 'Blue Margin, Inc.'],
['Miranda Hynnek', 'Voro'],
['Julie Hanna', 'KNOCK Inc.'],
['Bonnie Beiken', 'Dentsu Creative'],
['William Schrader', 'Meta'],
['Jenny Farman', 'Supernatural'],
['Nebyu Yonas', 'Neuralink'],
['Chloe Schwartz', 'Roche'],
['Hannah Holzmann', 'GoodRx'],
['Lauren Hassell', 'PAIGE'],
['Matthew Shire', 'Payoneer'],
['Alishah Sunesara', 'Willis Towers Watson'],
['Pierre Ibrahim', 'Empyrean']]


export_data = []

for row in data:
    name = row[0]
    company = row[1]
    region = 'IL'
    # Make the API request
    response = serper(full_name=name, company=company, selected_region=region)
    # print(f"------Serepr: ------------------------------------{response}")
    role = executiver(full_name=name, company=company, response=response)
    isExecutive = is_executer(role=role)
    contact = [name, company, role, isExecutive]
    export_data.append(contact)
    time.sleep(20)

print(export_data)
output_file = '/Users/igale/temp/isExecutive.csv'
f = open(output_file, 'w')

for i in export_data:
    d = i[0] + ',' + i[1] + ','+ i[2] + ','+ i[3] + '\n'
    f.write(d)


f.close()