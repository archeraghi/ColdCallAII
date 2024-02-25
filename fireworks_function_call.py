from fireworks.client import Fireworks
from openai import OpenAI
import pygame

def check_for_agent_query(sentence):
    """
    Checks if the input sentence is asking if this is an AI agent.
    If so, it triggers the function to connect to a real person through fireworks.ai.
    """
    normalized_sentence = sentence.lower().strip()
    if normalized_sentence == "are you an ai agent" or normalized_sentence == "are u an ai agent":
        return connect_to_real_person_through_fireworks()
    else:
        return "How can I assist you further?"

def connect_to_real_person_through_fireworks():
    """
    Simulates connecting to a real person using fireworks.ai API.
    """
    print("Connecting to a real person through fireworks.ai...")

    client = Fireworks(api_key="NXG4HOUrE42PIoX5F19CG5KfkkUmH1LTY6oH3MWYLuLPr0vG")
    # Example using chat completions API
    response = client.chat.completions.create(
      model="accounts/fireworks/models/llama-v2-7b-chat",
      messages=[{
        "role": "user",
        "content": "I'm looking to speak with a real person.",
      }],
    )
    # Assuming the response structure follows the provided example
    return response.choices[0].message.content

print("Are you an AI agent?")
response = check_for_agent_query("Are u an AI agent")
print(response)
