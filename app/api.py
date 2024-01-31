from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.routes.pride import pride_router
from app.routes.pdbdev import pdbdev_router
from app.routes.xiview import xiview_data_router
from app.routes.parse import parser_router

app = FastAPI(title="xi-mzidentml-converter WS",
              description="This is an API to crosslinking archive",
              version="0.0.1",
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              },
              openapi_url=" /pride/ws/archive/crosslinking/openapi.json",
              docs_url="/pride/ws/archive/crosslinking/docs")

# Set up CORS middleware
origins = ["*"]  # Update this with your allowed origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pride_router, prefix="/pride/ws/archive/crosslinking")
app.include_router(pdbdev_router, prefix="/pride/ws/archive/crosslinking/pdbdev")
app.include_router(xiview_data_router, prefix="/pride/ws/archive/crosslinking/data")
app.include_router(parser_router, prefix="/pride/ws/archive/crosslinking/parse")

