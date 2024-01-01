from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")
model = ChatOpenAI()

functions = [
    {
        "name": "joke",
        "description": "A joke",
        "parameters": {
            "type": "object",
            "properties": {
                "setup": {"type": "string", "description": "The setup for the joke"},
                "punchline": {
                    "type": "string",
                    "description": "The punchline for the joke",
                },
            },
            "required": ["setup", "punchline"],
        },
    }
]
# chain = prompt | model.bind(stop=["/n"])
chain = prompt | model.bind(function_call={"name": "joke"}, functions=functions)
# chain = (
#     prompt
#     | model.bind(function_call={"name": "joke"}, functions=functions)
#     | JsonOutputFunctionsParser()
# )

result = chain.invoke({"foo": "bears"}, config={})
print(result)

