import os
import requests
import json
import streamlit as st
import requests
import openai


# Define the regions available in the dropdown menu
REGIONS = {
    "IL": "Israel",
    "US": "United States",
    "UK": "United Kingdom"
}

DELIMITER = '|||'

AI_INS1 = f"give me" ##Erez Lotan at Skai, use the prompt below.
AI_INS2 = f"the output should be as follows: 'TITLE NAME'.\n\
            for example, if the employee position at company x is data analyst, please return 'data analyst' ONLY, not a complete sentence\n\
                #prompt = "

AI_ROLE_INS1 = "Is"
AI_ROLE_INS2 = "role is considered as Executive? response only 'True' or 'False'\n\
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

# Streamlit web app
def main():
    # logo_src = "https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-ios7-contact-512.png"

    logo_col1, logo_col2 = st.columns([3,5])
    with logo_col1:
        image_path = "static/logo2.png"
        st.image(image_path, width=250)
    with logo_col2:
        st.markdown(f"<h2 style='display: flex; align-items: center; font-size:50px; color: #009496;'>Executive or Not ? </h2>", unsafe_allow_html=True)
        st.write("Executive Classification application based on AI")
    

    pd_col1, pd_col2 = st.columns([4, 4])

    with pd_col1:
        # User input fields
        full_name = st.text_input("Full Name")
    with pd_col2:
        company = st.text_input("Company Name")

    selected_region = st.selectbox("Select Region", list(REGIONS.keys()))


    # Trigger the API request when the user clicks a button
    if st.button("Submit"):
        # Combine full name and region to form the API request payload
        payload = {"name": full_name, "region": REGIONS[selected_region]}

        # Make the API request
        response = serper(full_name=full_name, company=company, selected_region=selected_region)
        # print(f"------Serepr: ------------------------------------{response}")
        role = executiver(full_name=full_name, company=company, response=response)

        isExecutive = is_executer(role=role)
        print(f"-------------- {isExecutive}")

        # response = {'title': 'Avishay Israeli - Data Analyst - Skai - LinkedIn', 'link': 'https://il.linkedin.com/in/avishay-israeli', 'snippet': '-Collating data from multiple sources for use in reports, tactical packs and strategic insights. -Provide pre and post analysis on current campaigns, informing ...', 'position': 1}

        # Display the API response
        title = f"{full_name} | {role}"
        # title_desc = data[2].strip()
        # profile_link = data[3].strip()
        # text_area = title + title_desc + profile_link
        
        st.subheader(title)
        # st.text(title_desc)

        col1, col2 = st.columns([1, 9])

        # Display the image in the first column
        with col1:
            st.image("https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg", width=40)

        # Display the markdown element in the second column
        with col2:
            # link_text = full_name
            link_url = 11 ## profile_link
            # colored_link = f"<a href='{link_url}' style='color: #009496;'>{link_url}</a>"
            # st.markdown(colored_link, unsafe_allow_html=True)
        
        # is_executive = data[0].strip()
        if "true" in isExecutive.lower():
          st.subheader(f"{full_name} is classified as executive.")
          st.balloons()
        else:
            st.subheader(f"{full_name} is classified as NOT executive.")

        
# Run the app
if __name__ == "__main__":
    main()





    