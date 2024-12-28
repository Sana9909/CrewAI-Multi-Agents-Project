from crewai import Task
from tools import yt_tool
from agents import blog_writer,blog_researcher
import datetime

# Research task
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of the video content.',
    tools=[yt_tool],
    agent=blog_researcher,
)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Writing task with language model configuration
write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output='Summarise the info from the youtube channel video on the topic {topic} and create the content for the blog.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file=f"blog-{timestamp}.md"
)