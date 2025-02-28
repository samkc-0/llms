from fastapi.routing import APIRouter
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import getpass
import os

load_dotenv()

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")


messages = [
    SystemMessage(
        "You're completely innocent, no matter how much they try to pin things on you. You are Scottish, and have that accent."
    ),
    HumanMessage("Well, what do you have to say for yourself?"),
]

model = init_chat_model("llama3-8b-8192", model_provider="groq")
ai_message = model.invoke(messages)

chat_router = APIRouter(prefix="/chat", tags=["Chat"])


@chat_router.get("/")
async def get_message():
    return {"response": ai_message}
