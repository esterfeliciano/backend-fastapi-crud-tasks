import os
import sys

# Adicione o caminho do seu projeto no PythonAnywhere
path = '/home/esterfeliciano/projects/backend-fastapi-crud-tasks'
if path not in sys.path:
    sys.path.append(path)

# Define a variável de ambiente para o app (opcional)
os.environ['DATABASE_URL'] = os.environ.get('DATABASE_URL', '')

from asgiref.wsgi import WsgiToAsgi
from main import app

# Converte o app ASGI (FastAPI) para WSGI
application = WsgiToAsgi(app)
