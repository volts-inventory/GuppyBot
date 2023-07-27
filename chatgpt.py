import openai
from duckduckgo_search import ddg
import trafilatura

openai.api_key = ""
SET_MSG = {"role": "system", "content": "Your name Guppy, you are our friend. Your responses have a 50 word limit, unless asked for more detail."}
MSGS = {}

def get_response(query, asker):
    global MSGS
    if asker not in MSGS:
        MSGS[asker] = [{"role":"user", "content":query}]
    else:
        MSGS[asker].append({"role":"user", "content":query})
    MSGS[asker] = MSGS[asker][-30:]
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[SET_MSG]+MSGS[asker],
        temperature=1.11
    )
    message = completions.choices[0].message.content
    if ("an ai language model" in message.lower() and ("economic" in message.lower() or "current" in message.lower() or "time" in message.lower())):
        message = "I couldn't find in my memory banks...but checking the web: \n\n"
        results = ddg(query)
        downloaded = trafilatura.fetch_url(results[0]["href"])
        web_text = trafilatura.extract(downloaded)
        message += web_text
    
    MSGS[asker].append({"role": "assistant", "content": message})
    print(MSGS[asker])
    return message