from typing import List, Optional

from fastapi import APIRouter, Depends, status

from Schemas.AuthorPostRequestSchema import AuthorSchema
from services.AuthorService import AuthorService

AuthorRouter = APIRouter(
    prefix="/v1/authors", tags=["author"]
)


@AuthorRouter.get("/", response_model=List[AuthorSchema])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    authorService: AuthorService = Depends(),
):
    return [
        author.normalize()
        for author in authorService.list(
            name, pageSize, startIndex
        )
    ]
