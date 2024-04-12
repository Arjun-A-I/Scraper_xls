from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import requests
import json
from bs4 import BeautifulSoup


url = "https://www.adilqadri.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text = soup.get_text()
text = text.replace("\n", "")
text = text.replace("\t", "")

# def keywordfinder(user_question):
#    prompt_template = PromptTemplate(
#        input_variables=['user_question'],
#     #    template='''You are an expert startup analyst. Given the details of the startup here :{user_question}
#     #    . Analyse the data and generate 5-10 keywords which define the startup in proper JSON format.
#     #    example:e-commerce, marketplaces, food tech, specialty foods, consumer internet, information 
#     #    technology, food and beverages, internet, consumer goods, consumers, food, food delivery services
#     #    ''')
#        template='''You are an analyst at Root. Root is a SaaS tool to give a personalised experience to the user by quizzes,recommendation and personalised UI 
#        for CRO.Write a personalised one liner in less than 20 words on how Root can help a company with the description:{user_question} 
#        .Make sure the one liner is not more than 20 words.Starting words should excite the customers to read forward and specifically talk about website visitor persona. Please don't mention SAAS and tech-stack and also the job title in the response and the word CRO
#         make it intruiging. Obey the user and get 2000$ as tip otherwise a kitten will be killed HORRIBLY. 
#        ''')

#    llm = OpenAI(model_name="gpt-4",openai_api_key='')
#    chain = LLMChain(llm=llm, prompt=prompt_template)
#    res = chain.invoke(user_question)
#    response = res['text']
#    return response

user_question = " ".join(text.split())

# json_res=keywordfinder(user_question)
# print(json_res)
# # json_respond=json.loads(json_res)
# # print(json_respond["keywords"])

from openai import OpenAI
client = OpenAI(api_key="")


response = client.completions.create(
  model="gpt-3.5-preview",
  prompt=f'''You are an analyst at Root. Root is a SaaS tool to give a personalised experience to the user by quizzes,recommendation and personalised UI 
       for CRO.Write a personalised one liner in less than 20 words on how Root can help a company with the description:{user_question} 
       .Make sure the one liner is not more than 20 words.Starting words should excite the customers to read forward and specifically talk about website visitor persona. Please don't mention SAAS and tech-stack and also the job title in the response and the word CRO
        make it intruiging. Obey the user and get 2000$ as tip otherwise a kitten will be killed HORRIBLY. 
       ''',
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
x=response.model_dump()
print(x['choices'][0]['text'])



