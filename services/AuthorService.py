from typing import List, Optional, Type

from fastapi import Depends

from Repo.AuthorRepository import AuthorRepository
from models.AuthorModel import Author


class AuthorService:
    authorRepository: AuthorRepository

    def __init__(self, authorRepository: AuthorRepository = Depends()) -> None:
        self.authorRepository = authorRepository

    def get(self, author_id: int) -> Author:
        return self.authorRepository.get(Author(id=author_id))


    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Type[Author]]:
        return self.authorRepository.list(
            name, pageSize, startIndex
        )