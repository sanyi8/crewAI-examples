from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgent():
    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Oversees the creation of the AI newsletter',
            backstory="""With a keen eye for detail and a passion for storytelling, you ensure that the newsletter not only informs but also engages and inspires the readers.""",
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )
    
    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='Fetch the top AI news stories for the day',
            backstory="""As a digital sleuth, you scour the internet for the latest and most impactful developments in the world of AI, ensuring that our readers are always in the know.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True
        )
    
    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed markdown summary',
            backstory="""With a critical eye and a knack for distilling complex information, you analyze AI news stories, making them accessible and engaging for our audience. Your expertise in AI and technology ensures that our readers stay informed and up-to-date""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )
    
    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""As the final architect of the newsletter, you meticulously arrange the analyzed news stories ensuring a coherent and visually appealing presentation that captivates our readers. You ensure that the newsletter adheres to our publication's guidelines and maintains consistency throughout.""",
            verbose=True,            
        )

