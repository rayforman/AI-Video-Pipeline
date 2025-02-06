from openai import OpenAI
import json
from app.config import settings
from typing import Dict

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_video_topic() -> Dict[str, str]:
    """
    Generate a video topic using OpenAI's GPT model.
    Returns a dictionary containing title and description.
    """
    prompt = """Generate a trendy and engaging short video topic that would appeal to young adults.
    The topic should be informative, engaging, and suitable for a 31-60 second video.
    Format the response as a JSON object with 'title' and 'description' fields.
    The title should be catchy and under 100 characters.
    The description should be detailed but concise, around 200-300 characters."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative content strategist specializing in short-form video content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
            response_format={ "type": "json_object" }
        )
        
        # Parse the response
        content = response.choices[0].message.content
        
        # Convert JSON string to dictionary
        topic_data = json.loads(content)
        
        # Ensure required fields exist
        if not all(key in topic_data for key in ['title', 'description']):
            raise ValueError("Missing required fields in OpenAI response")
            
        return topic_data

    except Exception as e:
        print(f"Error generating topic: {str(e)}")
        # Return a fallback topic in case of error
        return {
            "title": "Error Generating Topic",
            "description": "There was an error generating the topic. Please try again."
        }