from ElysiumConfig.model_config import Elysium_Model_Config as EMC
import random

class Load_Agent():
  def __init__(self):
    self.ElysiumModelConfig = EMC() # EMC stants for Elysium_Model_Config : ) 
    self.model_config = self.ElysiumModelConfig.load_config()
  def modelroulet(self): 
    provider  = self.ElysiumModelConfig.available_providers()
    random_provider = random.choice(list(provider))
    provider = provider[random_provider]
    print(provider)


if __name__ == "__main__":
    agent = Load_Agent()
    try:
        # print(agent.   agent.modelroulet()ElysiumModelConfig.insert_api_key(api_key="are_u_stupid",provider_name="google_genai",model_name="gemini-2.5-flash"))
     agent.modelroulet()
    except Exception as e:
        print(e)
