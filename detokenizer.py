import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-4")

token_ids = list(map(int, input("Enter token IDs separated by spaces: ").split()))

decoded_text = tokenizer.decode(token_ids)

print("\nDecoded Text:")
print(decoded_text)