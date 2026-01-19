from app.database import Base
from sqlalchemy import Integer, ForeignKey, Text, TIMESTAMP, CheckConstraint, Boolean, text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .users import User
    from .products import Product

class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("grade >= 1 AND grade <= 5", name="check_grade_range"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    comment_date: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    rating: Mapped[float] =mapped_column(Float, default=0.0, server_default=text('0'))  # Средний рейтинг

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="reviews")

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    product: Mapped["Product"] = relationship("Product", back_populates="reviews")