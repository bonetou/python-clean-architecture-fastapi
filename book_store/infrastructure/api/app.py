from fastapi import FastAPI

from book_store.infrastructure.api.routers.books import books_router
from book_store.infrastructure.api.routers.management import management_router


app = FastAPI()
app.include_router(management_router)
app.include_router(books_router)
