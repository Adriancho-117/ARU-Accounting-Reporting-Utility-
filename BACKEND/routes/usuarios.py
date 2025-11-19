from flask import Blueprint, request, jsonify
from db import get_connection

# Blueprint para rutas de usuarios ARU
usuarios_aru = Blueprint('usuarios_aru', __name__)


# =========================
#   AUTENTICACIÓN / LOGIN
# =========================
@usuarios_aru.route('/login', methods=['POST'])
def login_aru():
    """Autentica un usuario y retorna token"""
    datos_entrada = request.json

    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor(dictionary=True)

    consulta_login = "SELECT * FROM usuarios WHERE correo = %s AND contrasena_hash = %s"
    cursor_aru.execute(consulta_login, (datos_entrada["correo"], datos_entrada["contrasena_hash"]))

    usuario_aru = cursor_aru.fetchone()

    cursor_aru.close()
    conexion_aru.close()

    if usuario_aru:
        token_aru = str(usuario_aru["id_usuario"])
        return jsonify({
            "mensaje": "Login exitoso", 
            "id": usuario_aru["id_usuario"], 
            "token": token_aru
        })
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401


# =========================
#   CREAR USUARIO
# =========================
@usuarios_aru.route('/usuarios', methods=['POST'])
def crear_usuario_aru():
    """Crea un nuevo usuario en el sistema"""
    datos_entrada = request.json

    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor()

    consulta_crear = """
        INSERT INTO usuarios (nombre, correo, rol, contrasena_hash)
        VALUES (%s, %s, %s, %s)
    """

    cursor_aru.execute(consulta_crear, (
        datos_entrada["nombre"],
        datos_entrada["correo"],
        datos_entrada["rol"],
        datos_entrada["contrasena_hash"]
    ))

    conexion_aru.commit()
    cursor_aru.close()
    conexion_aru.close()

    return jsonify({"mensaje": "Usuario creado"}), 201


# =========================
#   SALDO: OBTENER
# =========================
@usuarios_aru.route('/saldo/<int:id_usuario>', methods=['GET'])
def obtener_saldo_usuario_aru(id_usuario):
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


# =========================
#   SALDO: ACTUALIZAR
# =========================
@usuarios_aru.route('/saldo/<int:id_usuario>', methods=['PUT'])
def actualizar_saldo_usuario_aru(id_usuario):
    """Actualiza el saldo de un usuario (sumar o restar)"""
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
        # Verificar fondos suficientes
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


# =========================
#   BOLSILLOS: CREAR
# =========================
@usuarios_aru.route('/crear-bolsillo', methods=['POST'])
def crear_bolsillo_aru():
    """Crea un nuevo bolsillo para un usuario"""
    datos_entrada = request.json
    
    id_usuario_aru = datos_entrada.get("usuario_id", 1)
    nombre_bolsillo = datos_entrada.get("nombre", "Bolsillo")
    monto_bolsillo = float(datos_entrada.get("monto", 0))

    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor()

    cursor_aru.execute(
        "INSERT INTO bolsillos (usuario_id, nombre, monto) VALUES (%s, %s, %s)",
        (id_usuario_aru, nombre_bolsillo, monto_bolsillo)
    )

    conexion_aru.commit()
    cursor_aru.close()
    conexion_aru.close()

    return jsonify({"mensaje": "Bolsillo creado correctamente"}), 201


# =========================
#   BOLSILLOS: OBTENER
# =========================
@usuarios_aru.route('/bolsillos/<int:id_usuario>', methods=['GET'])
def obtener_bolsillos_usuario_aru(id_usuario):
    """Obtiene todos los bolsillos de un usuario"""
    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor(dictionary=True)
    
    cursor_aru.execute(
        "SELECT id_bolsillo, nombre, monto, fecha_creacion FROM bolsillos WHERE usuario_id = %s", 
        (id_usuario,)
    )
    bolsillos_resultado = cursor_aru.fetchall()
    cursor_aru.close()
    conexion_aru.close()
    
    return jsonify(bolsillos_resultado)


# =========================
#   PAGOS AUTOMÁTICOS: CREAR
# =========================
@usuarios_aru.route('/pagos_automaticos', methods=['POST'])
def crear_pago_automatico_aru():
    """Crea un nuevo pago automático"""
    datos_entrada = request.json
    id_usuario_aru = datos_entrada.get("usuario_id")
    nombre_pago = datos_entrada.get("nombre")
    monto_pago = float(datos_entrada.get("monto", 0))
    fecha_pago = datos_entrada.get("fecha")

    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor()
    
    cursor_aru.execute(
        "INSERT INTO pagos_automaticos (usuario_id, nombre, monto, fecha) VALUES (%s, %s, %s, %s)",
        (id_usuario_aru, nombre_pago, monto_pago, fecha_pago)
    )
    
    conexion_aru.commit()
    cursor_aru.close()
    conexion_aru.close()

    return jsonify({"mensaje": "Pago automático creado"}), 201


# =========================
#   PAGOS AUTOMÁTICOS: OBTENER
# =========================
@usuarios_aru.route('/pagos_automaticos/<int:id_usuario>', methods=['GET'])
def obtener_pagos_automaticos_usuario_aru(id_usuario):
    """Obtiene todos los pagos automáticos de un usuario"""
    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor(dictionary=True)
    
    cursor_aru.execute(
        "SELECT * FROM pagos_automaticos WHERE usuario_id = %s", 
        (id_usuario,)
    )
    pagos_resultado = cursor_aru.fetchall()
    cursor_aru.close()
    conexion_aru.close()
    
    return jsonify(pagos_resultado)


# =========================
#   PAGOS AUTOMÁTICOS: ELIMINAR
# =========================
@usuarios_aru.route('/pagos_automaticos/eliminar/<int:id_pago>', methods=['DELETE'])
def eliminar_pago_automatico_aru(id_pago):
    """Elimina un pago automático"""
    conexion_aru = get_connection()
    cursor_aru = conexion_aru.cursor()
    
    cursor_aru.execute(
        "DELETE FROM pagos_automaticos WHERE id_pago = %s", 
        (id_pago,)
    )
    
    conexion_aru.commit()
    cursor_aru.close()
    conexion_aru.close()
    
    return jsonify({"mensaje": "Pago automático eliminado"})




