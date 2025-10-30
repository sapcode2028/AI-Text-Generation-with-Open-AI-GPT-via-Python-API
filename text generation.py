import os
from openai import OpenAI
from transformers import pipeline
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

prompts = [
    "Write a short story about a robot learning to paint.",
    "Summarize the importance of renewable energy in one paragraph."
]

temperature = 0.9   
max_tokens = 200    
responses = []

try:
    print(" Using OpenAI GPT model...")
    client = OpenAI(api_key=api_key)
    for prompt in prompts:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        text = response.choices[0].message.content.strip()
        print(f"\nPrompt: {prompt}\nResponse: {text}\n{'-'*60}")
        responses.append({"prompt": prompt, "response": text})


except Exception as e:
    print(f"⚠ OpenAI API failed ({e._class.name_}): {e}")
    print("Switching to local Hugging Face model...")

    generator = pipeline("text-generation", model="distilgpt2")

    for prompt in prompts:
        result = generator(prompt, max_length=120, temperature=temperature)
        text = result[0]["generated_text"]
        print(f"\nPrompt: {prompt}\nResponse: {text}\n{'-'*60}")
        responses.append({"prompt": prompt, "response": text})

df = pd.DataFrame(responses)
df.to_csv("gpt_responses.csv", index=False)
print("\n Responses saved to gpt_responses.csv")

all_text = " ".join(df["response"])
word_freq = Counter(all_text.split())
wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Generated Responses")
plt.show()