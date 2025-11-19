from flask import Blueprint, request, jsonify
from db import get_connection
from services.auth_service import verify_token
import functools

# Blueprint para rutas de bolsillos ARU
bolsillos_aru = Blueprint("bolsillos_aru", __name__)


def autenticacion_requerida(funcion_decorada):
    """Decorador para requerir autenticación con token"""
    @functools.wraps(funcion_decorada)
    def envoltura(*args, **kwargs):
        autorizacion_header = request.headers.get("Authorization", "")
        
        if not autorizacion_header.startswith("Bearer "):
            return jsonify({"error": "Token faltante"}), 401
        
        token_aru = autorizacion_header.split()[1]
        usuario_aru = verify_token(token_aru)
        
        if not usuario_aru:
            return jsonify({"error": "Token inválido o expirado"}), 401
        
        request.usuario_id_aru = usuario_aru["user_id"]
        return funcion_decorada(*args, **kwargs)

    return envoltura


@bolsillos_aru.route("/create", methods=["POST"])
@autenticacion_requerida
def crear_bolsillo_aru():
    """Crea un nuevo bolsillo para el usuario autenticado"""
    datos_entrada = request.get_json() or {}

    nombre_bolsillo_aru = datos_entrada.get("nombre")
    fecha_desembolso_aru = datos_entrada.get("fecha")
    saldo_inicial_aru = datos_entrada.get("saldo", 0)
    monto_aru = saldo_inicial_aru
    fecha_creacion_aru = fecha_desembolso_aru

    if not nombre_bolsillo_aru:
        return jsonify({"error": "El nombre es obligatorio"}), 400

    try:
        conexion_aru = get_connection()
        cursor_aru = conexion_aru.cursor()
        
        cursor_aru.execute(
            "INSERT INTO bolsillos (usuario_id, nombre, fecha_creacion, monto) VALUES (%s, %s, %s, %s)",
            (request.usuario_id_aru, nombre_bolsillo_aru, fecha_creacion_aru, monto_aru)
        )
        
        conexion_aru.commit()
        return jsonify({"message": "Bolsillo creado con éxito"}), 201
    except Exception as excepcion_aru:
        return jsonify({"error": str(excepcion_aru)}), 500
    finally:
        if conexion_aru:
            conexion_aru.close()


@bolsillos_aru.route("/", methods=["GET"])
@autenticacion_requerida
def listar_bolsillos_aru():
    """Lista todos los bolsillos del usuario autenticado"""
    try:
        conexion_aru = get_connection()
        cursor_aru = conexion_aru.cursor(dictionary=True)
        
        cursor_aru.execute(
            "SELECT id_bolsillo as id, nombre, fecha_creacion as fecha, monto as saldo FROM bolsillos WHERE usuario_id = %s", 
            (request.usuario_id_aru,)
        )
        
        filas_resultado = cursor_aru.fetchall()
        cursor_aru.close()
        conexion_aru.close()
        
        return jsonify(filas_resultado)
    except Exception as excepcion_aru:
        return jsonify({"error": str(excepcion_aru)}), 500

