from fastapi import FastAPI
from book_store.infrastructure.api.routers.management import management_router


app = FastAPI()
app.include_router(management_router)
