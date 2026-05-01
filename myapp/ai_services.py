from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def generate_user_description(user_data):
    llm = OllamaLLM(model="llama3.2", base_url="http://host.docker.internal:11434")

    template = """
    You are a professional copywriter who specializes in writing interesting biographies for social networks.
    Your task: based on the provided data, create a short (2-3 sentences), stylish and friendly profile description.

    User data:
    - Name: {name}
    - Age: {age}
    - Location: {location}
    - Interests: {interests}

    Write a description from the third person. Do not use the phrases "Here is the description" or "Generated text", write the result immediately.
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    response = chain.invoke(user_data)
    return response.strip()
