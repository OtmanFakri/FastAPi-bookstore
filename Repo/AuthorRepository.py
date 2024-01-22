from typing import List, Optional, Type

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from config.Databases import (
    get_db_connection,
)
from models.AuthorModel import Author

class AuthorRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Type[Author]]:
        query = self.db.query(Author)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()
