from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(model='llama3.2')

response = llm('give me top 10 germnay movie in history , return data as json')
print(response)

