from fastapi import FastAPI
from app.infrastructure.rest.fastapi.v1.routes import product
from app.infrastructure.container import Container

def create_app() -> FastAPI:
  container = Container()
  app = FastAPI()
  app.container =container
  
  app.include_router(product.router)

  return app