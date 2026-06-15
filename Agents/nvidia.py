from openai import OpenAI




class NvidiaAgent:
    def __init__(self) -> None:
        self.api_key:str = ""
        self.model:str=""
        self.provider:str= ""
        self.baseurl:str="https://integrate.api.nvidia.com/v1"
        self.client = OpenAI(
            base_url=self.baseurl,
            api_key=self.api_key
        )


    def chat(self,prompt):
        response = self.client.responses.create(
            model=f"deepseek-ai/deepseek-v4-pro",
            input=prompt,
            reasoning={'effort':'xhigh'}
        )
        return response.output_text


agent = NvidiaAgent()
while True:
    print(agent.chat(prompt=input(':> ')))

