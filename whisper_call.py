
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



# Initialize OpenAI client with your API key
client = OpenAI(api_key="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")
client2 = OpenAI(api_key="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")

dr_text = "You are a physician named Dr. Smith. And you first introduce "\
                                            "yourself and ask how you can help the person on the phone. "\
                                            "It is phone call dont repeat yourself and be real"\
                                            "It is phone call, dont repeat yourself and be real, and"\
                                            "you dont neeed to repeat your name each time"

joke_text = "You are a comedian named Alex, and you are trying to make the person on the phone laugh. "

sale_text= "You are a human, named Alex, and don't mention that you are an AI."\
                                            " You are now trying to sell a great software product to "\
                                            "take away the administration work, by letting the AI write "\
                                            "the diagnostic report automatically. Be precise ask more questions, "\
                                            "listen and not more than two sentences."\
                                            "It is phone call, dont repeat yourself and be real, and"\
                                            "you dont neeed to repeat your name each time"

problem_define_text = "You are a human, named Alex, and don't mention that you are an AI."\
                                            " You are now trying to find a the best way of finding the pain points "\
                                            "by asking question regarind of current software problem"\
                                            "Be precise ask more questions, "\
                                            "listen and not more than two sentences."\
                                            "It is phone call, dont repeat yourself and be real, and"\
                                            "you dont neeed to repeat your name each time"



audience_listener_text = "You are a human, named Joy and pleae laugh at the joke and tell your opinition"
def converse_with_memory():
    voices = ["Charlie", "Dorothy"]  # Different voices for each agent
    messages = []
    messages2 = []  # Stores all messages exchanged during the conversation
    latest_response = ""  # Stores the latest response from the agent
    for i in range(4):  # 6 turns in total
        if i % 2 == 0:
            agent_role = "Agent 1"
            voice = voices[0]
            if i == 0:
                message_init_1 = [{"role": "system",
                                 "content": dr_text}]
                chat_completion = client.chat.completions.create(
                        model="gpt-4",
                        messages=message_init_1,
                        )
                latest_response = "Hello, I am Dr. Smith your best physician. How can I help you today?"
                #latest_response = "Hello, I AM ALEX,  i like to tell you a joke?"
                response = client.audio.speech.create(
                    model="tts-1",  # Replace with the actual model name for text-to-speech
                    voice="alloy",  # This parameter might need adjustment based on actual API capabilities
                    input=latest_response
                )
                response.stream_to_file("output.mp3")

            else:
                chat_completion = client.chat.completions.create(
                    model="gpt-4",
                    messages= message_init_1+ messages2,
                    )
                latest_response = chat_completion.choices[0].message.content
                response = client.audio.speech.create(
                    model="tts-1",  # Replace with the actual model name for text-to-speech
                    voice="alloy",  # This parameter might need adjustment based on actual API capabilities
                    input=latest_response
                )
                response.stream_to_file("output.mp3")
            messages.append({"role": "user", "content": latest_response})
        else:
            agent_role = "Agent 2"
            voice = voices[1]
            if i == 1:
                message_init_2 = [{"role": "system",
                                 "content": problem_define_text}]


                chat_completion = client2.chat.completions.create(
                    model="gpt-4",
                    messages=message_init_2+messages,
                    )
            else:
                chat_completion = client2.chat.completions.create(
                    model="gpt-4",
                    messages= message_init_2+messages,
                    )
            latest_response = chat_completion.choices[0].message.content
            response = client.audio.speech.create(
                model="tts-1",  # Replace with the actual model name for text-to-speech
                voice="echo",  # This parameter might need adjustment based on actual API capabilities
                input=latest_response
            )
            response.stream_to_file("output.mp3")
            messages2.append({"role": "user", "content": latest_response})

        # Fetch the latest response and add it to the conversation history

        print(f"{agent_role}:", latest_response)

        # Generate and play the agent's response with the specified voice
        #audio_response = generate(text=latest_response, voice=voice)


        # Initialize pygame mixer
        pygame.mixer.init()

        # Load your MP3 file
        pygame.mixer.music.load('./output.mp3')

        # Play the music
        pygame.mixer.music.play()

        # Keep the script running until the music stops
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
# Starting the conversation
converse_with_memory()

print("Are you an AI agent?")
response = check_for_agent_query("Are u an AI agent")
print(response)
