import tiktoken


enc =  tiktoken.encoding_for_model("gpt-4o" )
text = "Hello, world! My name is Mian Ahmad Basit"
num_tokens = len(enc.encode(text))
tokens = enc.encode(text)

print(f"Number of tokens: {num_tokens}")
print(f"Tokens: {tokens}")

decoded  =enc.decode([13225, 11, 2375, 0, 3673, 1308, 382, 391, 1200, 97625, 18373, 278])
print(f"Decoded text: {decoded}")