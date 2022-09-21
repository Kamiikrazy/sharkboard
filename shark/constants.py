from fastapi.templating import Jinja2Templates


class Server:
    TEMPLATES = Jinja2Templates(directory="shark/templates")
