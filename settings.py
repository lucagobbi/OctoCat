from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field

class OctoCatSettings(BaseModel):
    octoprint_url: str = Field(
        title="OctoPrint URL",
        default="http://octopi.local:8081/"
    )
    octoprint_api_key: str = Field(
        title="Your OctoPrint API Key",
        default="XXXXXXXXXXXXXXXXXXXXX"
    )
    
    

@plugin
def settings_model():
    return OctoCatSettings
