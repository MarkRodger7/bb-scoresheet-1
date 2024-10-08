import openai
import requests
import base64

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key="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"
)

def getImage(imagePath):
  with open(imagePath, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

teamImage = getImage("team.jpg")
scoreImage = getImage("score.jpg")


GPTOutput = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "From the first image, extract the player name and number. From the second image extract the points of each player from their corresponding number in the B column. The space between numbers dictate the point difference. For example if one number is two boxes below another, this means two points have been scored by the player of that number. By looking at the final score number of team B at the bottom of the second image, this should show you what all the player's points sum to. If the sum of the player's points that you have extracted does not equal the total of this final score number, then re-analyse the score column and begin to estimate symbols that you were unsure of and round them to the most likely number relating to a player. Do this until the player's total score equals the final score total. Then, output these stats together. That is the only output that I want."
                },
                {
                 "type": "image_url",
                 "image_url": {
                   "url": f"data:image/jpeg;base64,{teamImage}"
                 } 
                },
                                {
                 "type": "image_url",
                 "image_url": {
                   "url": f"data:image/jpeg;base64,{scoreImage}"
                 } 
                }
            ]
        }
    ],
    model="gpt-4o",
    temperature=0.2,
)

# Print the result
print(GPTOutput.choices[0].message.content)