from flask import Flask
from routes.usuarios import usuarios_aru
from routes.bolsillos import bolsillos_aru
from routes.saldo import saldo_aru
from routes.admin import admin_aru
from flask_cors import CORS

# Inicializar aplicación ARU
app_aru = Flask(__name__)

# Permitir CORS en desarrollo
CORS(app_aru)

# Registrar blueprints
app_aru.register_blueprint(usuarios_aru)
app_aru.register_blueprint(bolsillos_aru, url_prefix="/api/bolsillos")
app_aru.register_blueprint(saldo_aru)
app_aru.register_blueprint(admin_aru, url_prefix="/admin")


@app_aru.route('/')
def inicio_aru():
    return "Backend ARU funcionando correctamente."


if __name__ == "__main__":
    app_aru.run(debug=True, port=5000)

