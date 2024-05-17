from crewai import Crew, Process

from agents import AINewsLetterAgents
from tasks import AINewsletterTasks
from langchain_openai import ChatOpenAI
from file_io import save_markdown

#Initialize the openai gpt4 language model

OpenAIGPT4 = ChatOpenAI(
    model="gpt-4"
)

agents = AINewsletterAgents()
tasks = AINewsLetterTask()

# Setting up agents

editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler()

# Setting up tasks

fetch_news_task = task.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compiled_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyzed_news_task], save_markdown) 

# Setting up tools

crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compiled_newsletter_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4
)

#kickoff crew
results = crew.kickoff()

print("Crew work results:")
print(results)
