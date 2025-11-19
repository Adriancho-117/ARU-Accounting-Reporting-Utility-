from flask import Blueprint, request, jsonify
from db import get_connection

# Blueprint para rutas de saldo ARU
saldo_aru = Blueprint('saldo_aru', __name__)

# --- OBTENER SALDO ---
@saldo_aru.route('/saldo/<int:id_usuario>', methods=['GET'])
def obtener_saldo_aru(id_usuario):
    """Obtiene el saldo disponible de un usuario"""
    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor(dictionary=True)
    
    cursor_aru.execute(
        "SELECT saldo FROM usuarios WHERE id_usuario = %s", 
        (id_usuario,)
    )
    fila_resultado = cursor_aru.fetchone()
    cursor_aru.close()
    conexion_aru.close()

    if not fila_resultado:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    return jsonify({"saldo": float(fila_resultado["saldo"])})


# --- ACTUALIZAR SALDO ---
@saldo_aru.route('/saldo/<int:id_usuario>', methods=['PUT'])
def actualizar_saldo_aru(id_usuario):
    """Actualiza el saldo de un usuario"""
    datos_entrada = request.json
    cantidad_aru = float(datos_entrada.get("cantidad", 0))
    operacion_aru = datos_entrada.get("operacion", "sumar")

    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor()

    if operacion_aru == "sumar":
        cursor_aru.execute(
            "UPDATE usuarios SET saldo = saldo + %s WHERE id_usuario = %s", 
            (cantidad_aru, id_usuario)
        )
    else:
        cursor_aru.execute(
            "SELECT saldo FROM usuarios WHERE id_usuario = %s", 
            (id_usuario,)
        )
        saldo_actual = cursor_aru.fetchone()
        
        if saldo_actual and saldo_actual[0] < cantidad_aru:
            cursor_aru.close()
            conexion_aru.close()
            return jsonify({"mensaje": "Fondos insuficientes"}), 400

        cursor_aru.execute(
            "UPDATE usuarios SET saldo = saldo - %s WHERE id_usuario = %s", 
            (cantidad_aru, id_usuario)
        )

    conexion_aru.commit()
    cursor_aru.close()
    conexion_aru.close()

    return jsonify({"mensaje": "Saldo actualizado"})

