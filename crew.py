from crewai import Crew,Process
from tasks import research_task,write_task
from agents import blog_researcher,blog_writer
from dotenv import load_dotenv
load_dotenv()
import os

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=False,
    cache=True,
    max_rpm=100,
    share_crew=True,
    embedder={
        "provider": "google",
        "config": {
            "api_key": "GOOGLE_API_KEY",
            "model_name": "gemini-1.5-flash"
        }
    }
)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={"topic":"AI VS ML VS DL VS data science"})
print(result)