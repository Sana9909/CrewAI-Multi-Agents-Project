from crewai import Agent,LLM
from tools import yt_tool


import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#     verbose=True,
#     temperature=0.5,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

llm=LLM(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-1.5-flash",
)

# embedding_model="text-embedding-004"

## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog researcher from Youtube Videos',
    goal='To get the relevant video content for the topic {topic} from Youtube channel',
    name='Senior blog researcher',
    description='Blog reasearcher having experience in researching and providing suggestions',
    verbose=True,
    memory=True,
    backstory='This agent is expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providingn suggestion',
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

## Create a senior blog writer agent with Youtube tools

blog_writer=Agent(
    role='Blog writer from Youtube Videos',
    goal='Narrate compelling tech stories about the video content for the topic {topic} from Youtube channel',
    name='Senior blog writer',
    description='Blog writer having experience in writing engaging blog posts',
    verbose=True,
    memory=True,
    backstory='With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in and accessible manner',
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)