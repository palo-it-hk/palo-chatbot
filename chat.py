from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


def gpt_model(input):
    if input:

        # messages = [
        #     {"role": "system", "content": "You are an AI specialized in climate change. Do not answer anything other than climate change-related queries."},
        #     {"role": "user", "content": input}
        # ]

        messages = [
            {"role": "system", "content": "You are an AI specialized helpful assistant."},
            {"role": "user", "content": input}
        ]

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content

        return reply
    return "something went wrong..."


def gpt16k(input):
    if input:

        # messages = [
        #     {"role": "system", "content": "You are an AI specialized in climate change. Do not answer anything other than climate change-related queries."},
        #     {"role": "user", "content": input}
        # ]

        messages = [
            {"role": "system", "content": "you are a helpful assistant."},
            {"role": "user", "content": input}
        ]

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", messages=messages
        )
        reply = chat.choices[0].message.content

        return reply
    return "something went wrong..."


# def llma2_model(input):
#     if input:
#         # define the parameters for your Llama2 request
#         params = {
#             'input': 'hello world',
#             'model': 'llama2',
#             'num_samples': 5,
#             'length': 250,
#             'temperature': 0.7
#         }


#         # use the generate_text() method of the Replicate client to make the Llama2 API request
#         response = client.generate_text(params)

#         # print the generated text samples
#         print(response['samples'])
#         reply = response['samples']

#         return reply

#     return "something went wrong..."