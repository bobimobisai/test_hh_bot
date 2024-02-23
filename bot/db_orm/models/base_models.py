from sqlalchemy import text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bot.db_orm.database import Base, str_264


class DataEoraOrm(Base):
    __tablename__ = "eora"
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    data: Mapped[list[str]] = mapped_column(JSON)


