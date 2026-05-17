from Elysium_Config.model_config import Elysium_Model_Config as EMC

class Load_Agent():
 def __init__(self):
    self.Elysium_ModelConfig = EMC() # EMC stants for Elysium_Model_Config : ) 
    self.model_config = self.Elysium_ModelConfig.load_config()
        
    


if __name__ == "__main__":
    agent = Load_Agent()
    print(agent.Elysium_ModelConfig.insert_api_key(api_key="something",provider_name="ollama",model_name="gemma4"))

