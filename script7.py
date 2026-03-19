
import os
key = os.getenv("OPENAI_API_KEY")
print("repr:", repr(key))
if key:
    print("starts with:", key[:6])
    print("length:", len(key))
else:
    print("OPENAI_API_KEY is not set")
