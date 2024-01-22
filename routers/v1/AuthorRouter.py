from typing import List, Optional

from fastapi import APIRouter, Depends, status

from Schemas.AuthorPostRequestSchema import AuthorSchema, AuthorPostRequestSchema
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

@AuthorRouter.get("/{id}",response_model=AuthorSchema)
def get(id : int ,authorService: AuthorService = Depends()):
    return authorService.get(id).normalize()

@AuthorRouter.post("/",response_model=AuthorSchema)
def create(
        author_body: AuthorPostRequestSchema,
        authorService: AuthorService = Depends()):
    return authorService.create(author_body).normalize()
@AuthorRouter.patch("/{id}",response_model=AuthorSchema)
def update(
    id : int,
    author_body: AuthorPostRequestSchema,
    authorService: AuthorService = Depends(),
):
    return authorService.update(
        id,
        author_body
    ).normalize()




