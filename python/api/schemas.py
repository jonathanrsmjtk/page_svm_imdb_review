from typing import List

from pydantic import BaseModel

#Create schema as form of post input and result
class TweetBase(BaseModel):
    data:str
    sentiment:str
        
class TweetClassify(BaseModel):
    data:str