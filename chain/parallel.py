from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


 
prompt1=PromptTemplate(
    template='Generate short and simple notes from the text \n {text}', 
    input_variables=['text']

)

prompt2=PromptTemplate(
    template='Generate 5 short Q/A from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="""
Merge the following notes and Q/A into a single study document.

Output format:

## Notes
{notes}

## Questions and Answers
{quiz}

Do not summarize. Include all notes and all Q/A pairs.
""",
    input_variables=["notes", "quiz"]
)

parser=StrOutputParser()

parallel_chain = RunnableParallel({
    'notes':prompt1 | model1 |parser,
    'quiz': prompt2 | model1 | parser
    }
)

merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain

result=chain.invoke({'text':'The capital of France is Paris. It is known for its art, culture, and history. The Eiffel Tower is one of the most famous landmarks in Paris.'})

print(result)




