from pydantic import BaseModel, Field


class AuthorPostRequestSchema(BaseModel):
    name: str


class AuthorSchema(AuthorPostRequestSchema):
    id: int


