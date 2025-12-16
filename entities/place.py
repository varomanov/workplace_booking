from entities.base import Base
from sqlalchemy import SmallInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class Place(Base):

    __tablename__ = "places"

    number: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    section: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    floor: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    is_public: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    @classmethod
    def to_str(self):
        return f'{self.section}/{self.number}'