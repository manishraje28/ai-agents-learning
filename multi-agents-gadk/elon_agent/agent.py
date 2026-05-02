from google.adk import Agent
from dotenv import load_dotenv
import httpx

load_dotenv()

class ElonAgent:

    def __init__(self, remote_agent_urls):
        self.remote_agent_urls = self.remote_agent_urls or []
        self.agent = None
    

    async def create_agent(self):

        self.agent = Agent(
        model = "gemini-2.5-flash",
        name="elon_agent",
        description="Helps coordinate badmintor games with friends",
        instruction="You are Elon's Personal agent, you help organize games with friends",
        tools=[]
    )
        return self.agent   


    async def _load_remote_agents():
        async with httpx.AsyncClient(timeout=30) as client:
            for url in self.remote_agent_urls:
                resolver = A2ACardResolver(client, url)
                card = await resolver.get_agent_card()
                self.remote_connections[card]
            



root_agent = agent