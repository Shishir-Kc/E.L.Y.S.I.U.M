from openai import OpenAI
from Agents import Load_Agent


agent = Load_Agent()





class NvidiaAgent:
    def __init__(self,agent) -> None:
        roulet = agent.model_roulet(priority_provider="nvidia")
        self.model:str=roulet['model']
        self.provider:str=roulet['model_provider']
        self.api_key:str =  agent.model_key(provider=self.provider,model=self.model)
        self.baseurl:str="https://integrate.api.nvidia.com/v1"
        self.client = OpenAI(
            base_url=self.baseurl,
            api_key=self.api_key
        )
        print(f"""
                model => {self.model} \n 
                provider => {self.provider}

              """)

    def chat(self,prompt):
        print(f"{self.provider}/{self.model}")
        response = self.client.responses.create(
            model=f"{self.provider}/{self.model}",
            input=prompt,
            reasoning={'effort':'high'}
        )
        return response.output_text

if __name__ == "__main__":
    agent = Load_Agent()
    agent = NvidiaAgent(agent)
    print(agent.chat(prompt=input(':>')))
