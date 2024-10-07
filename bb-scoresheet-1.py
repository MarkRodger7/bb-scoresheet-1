import openai

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key="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"
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Write me a poem",
        }
    ],
    model="gpt-4o",
)

# Print the result
print(chat_completion.choices[0].message.content)