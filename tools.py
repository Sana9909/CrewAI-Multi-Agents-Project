from crewai_tools import YoutubeChannelSearchTool
from dotenv import load_dotenv
load_dotenv()
import os

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

yt_tool=YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')