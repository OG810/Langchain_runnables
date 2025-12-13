from langchain_openai import ChatOpenAI
from langchian_core.prompts import PromptTemplate 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchian.schema.runnable import RunnableSequence

load_dotenv()
model=ChatOpenAI()
parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Explain the following joke {text}',
    input_variables=['text']
)

chain=RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':'AI'}))
