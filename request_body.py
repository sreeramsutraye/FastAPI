from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

#This is called Request Body. It shows all the required parameters of Book Object
class Book(BaseModel):
    id: UUID
    title: str = Field(title="Title of the Book ",min_length=1)
    author: str = Field(title="Author of the Book",min_length=1)
    description: Optional[str] = Field(title="Description of the Book",min_length=1,max_length=100)
    rating: int
    
    #It shows the example values of the Book Object
    class Config:
        schema = {
            "Example": {
            "id":"6bedb5b4-ed8c-4aa8-877c-f6e0745e0849",
            "title":"Name of the book",
            "author":"Name of the Author of the book",
            "description":"Give a Genuine Description",
            "rating":"0-5"
        }   
        }
  