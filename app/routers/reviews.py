from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db_depends import get_async_db
from app.schemas import Review, ReviewCreate
from app.models.reviews import Review as ReviewModel
from app.models.products import Product as ProductModel
from app.models.users import User as UserModel
from app.auth import get_current_buyer
from app.utils import update_product_rating

router = APIRouter(prefix="/reviews",
                   tags=["reviews"])

@router.get("/", response_model=list[Review])
async def get_reviews(db: AsyncSession = Depends(get_async_db)):
    stmt = select(ReviewModel).where(ReviewModel.is_active == True)
    db_reviews = await db.scalars(stmt)

    return db_reviews.all()

@router.post("/", response_model=Review)
async def create_review(review: ReviewCreate,
                        db: AsyncSession = Depends(get_async_db),
                        current_user: UserModel = Depends(get_current_buyer)):

    stmt = select(ProductModel).where(ProductModel.id == review.product_id, ProductModel.is_active == True)
    temp = await db.scalars(stmt)
    db_product = temp.first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_review = ReviewModel(**review.model_dump(), user_id=current_user.id)
    db.add(new_review)
    await db.commit()

    await update_product_rating(db, review.product_id)

    return new_review

@router.delete("/{review_id}")
async def delete_review(review_id: int,
                        db: AsyncSession = Depends(get_async_db),
                        current_user: UserModel = Depends(get_current_buyer)) -> dict:

    stmt = select(ReviewModel).where(ReviewModel.id == review_id, ReviewModel.is_active == True)
    temp = await db.scalars(stmt)
    db_review = temp.first()

    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    # Удалить может либо автор отзыва, либо администратор
    if db_review.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="You can only delete your own reviews"
        )

    db_review.is_active = False
    await db.commit()

    await update_product_rating(db, db_review.product_id)

    return {"message": "Review deleted"}