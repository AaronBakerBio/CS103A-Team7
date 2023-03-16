""" Aaron Baker
aajbaker@brandeis.edu
Program :
Date :
Content :
Description :
"""
import openai



class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self, apikey):
         self.apikey=apikey
         # Set up the OpenAI API client
         openai.api_key = apikey #os.environ.get('APIKEY')

         # Set up the model and prompt
         self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

if __name__=='__main__':
    '''
    '''
    import os
    openai.api_key = "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"
    g = GPT("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")
