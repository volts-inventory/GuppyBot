import chatgpt

print("Bot is up")
while(1):
    i = input(">")
    resp = chatgpt.get_response(i, "asker")
    print("Bot: " + resp)