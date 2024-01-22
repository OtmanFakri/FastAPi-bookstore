from typing import List, Optional, Type

from fastapi import Depends

from Repo.AuthorRepository import AuthorRepository
from Schemas.AuthorPostRequestSchema import AuthorSchema
from models.AuthorModel import Author


class AuthorService:
    authorRepository: AuthorRepository

    def __init__(self, authorRepository: AuthorRepository = Depends()) -> None:
        self.authorRepository = authorRepository

    def get(self, author_id: int) -> Optional[Type[Author]]:
        return self.authorRepository.get(Author(id=author_id))


    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 10,
        startIndex: Optional[int] = 0,
    ) -> List[Type[Author]]:
        return self.authorRepository.list(
            name, pageSize, startIndex
        )

    def create(self,author_body : AuthorSchema) -> Author:
        return self.authorRepository.create(
            Author(name=author_body.name)
        )

    def update(
            self,
            author_id: int,
            author_body: AuthorSchema
    ):
        return self.authorRepository.update(
            author_id,
            Author(name=author_body.name)
        )