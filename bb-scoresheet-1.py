import openai
import requests
import base64

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key="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"
)

imagePath = input("Enter image filename ")

def getImage(imagePath):
  with open(imagePath, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

base64Image = getImage(imagePath)

GPTOutput = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "This is a basketball scoresheet. By looking at the St Andrews Mens 2 team section in the bottom left of the image, give me the name, number and points for each player from St Andrews. St Andrews are in the team B column of the running score."
                },
                {
                 "type": "image_url",
                 "image_url": {
                   "url": f"data:image/jpeg;base64,{base64Image}"
                 } 
                }
            ]
        }
    ],
    model="gpt-4o",
)

# Print the result
print(GPTOutput.choices[0].message.content)