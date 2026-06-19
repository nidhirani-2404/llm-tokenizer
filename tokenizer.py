import tiktoken
text=input("ENTER TEXT:  ")

tokenizer=tiktoken.encoding_for_model("gpt-4")

token_ids=tokenizer.encode(text)

print("\nToken IDs:")
print(token_ids)