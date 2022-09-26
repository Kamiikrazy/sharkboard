from fastapi.templating import Jinja2Templates


class Config:
    TEMPLATES = Jinja2Templates(directory="shark/templates")
    TITLE: str = "Admin Panel"
    DESCRIPTION: str = "Fancy way to communicate with your API and do testing"
    VERSION: str = "0.1"
