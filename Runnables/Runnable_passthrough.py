from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n{text}',
    input_variables=['text']
)

parser = StrOutputParser()

joke_gen_chain= RunnableSequence(template1,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation'
:RunnableSequence(template2,model,parser)
}
    )

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({
    'topic': 'Samsung Galaxy S24 Ultra' 
}))

