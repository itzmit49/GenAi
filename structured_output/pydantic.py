from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Schema
class Review(BaseModel):
    key_themes: list[str] = Field(
        description="A list of key themes or topics discussed in the review"
    )

    summary: str = Field(
        description="A brief summary of the review"
    )

    sentiment: Literal["pos", "neg"] = Field(
        description="The sentiment of the review"
    )

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
""")

print(result)