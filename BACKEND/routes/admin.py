from flask import Blueprint, request, jsonify
from db import get_connection
from services.auth_service import verify_token
import functools

# Blueprint para rutas administrativas ARU
admin_aru = Blueprint('admin_aru', __name__)


def autenticacion_requerida(funcion_decorada):
    """Decorador para requerir autenticación"""
    @functools.wraps(funcion_decorada)
    def envoltura(*args, **kwargs):
        autorizacion_header = request.headers.get('Authorization', '')
        
        if not autorizacion_header.startswith('Bearer '):
            return jsonify({'error': 'Token faltante'}), 401
        
        token_aru = autorizacion_header.split()[1]
        usuario_aru = verify_token(token_aru)
        
        if not usuario_aru:
            return jsonify({'error': 'Token inválido o expirado'}), 401
        
        request.usuario_id_aru = usuario_aru['user_id']
        return funcion_decorada(*args, **kwargs)

    return envoltura


def admin_requerido(funcion_decorada):
    """Decorador para requerir permisos de administrador"""
    @functools.wraps(funcion_decorada)
    def envoltura(*args, **kwargs):
        autorizacion_header = request.headers.get('Authorization', '')
        
        if not autorizacion_header.startswith('Bearer '):
            return jsonify({'error': 'Token faltante'}), 401
        
        token_aru = autorizacion_header.split()[1]
        usuario_aru = verify_token(token_aru)
        
        if not usuario_aru:
            return jsonify({'error': 'Token inválido o expirado'}), 401

        # Verificar rol en la base de datos
        conexion_aru = get_connection()
        try:
            cursor_aru = conexion_aru.cursor(dictionary=True)
            cursor_aru.execute(
                'SELECT rol FROM usuarios WHERE id_usuario = %s', 
                (usuario_aru['user_id'],)
            )
            fila_resultado = cursor_aru.fetchone()
            cursor_aru.close()
            
            if not fila_resultado or fila_resultado.get('rol') != 'admin':
                return jsonify({'error': 'Se requieren permisos de administrador'}), 403
        except Exception as excepcion_aru:
            return jsonify({'error': str(excepcion_aru)}), 500
        finally:
            if conexion_aru:
                conexion_aru.close()

        request.usuario_id_aru = usuario_aru['user_id']
        return funcion_decorada(*args, **kwargs)

    return envoltura


@admin_aru.route('/users', methods=['GET'])
@admin_requerido
def listar_usuarios_aru():
    """Lista todos los usuarios del sistema"""
    try:
        conexion_aru = get_connection()
        cursor_aru = conexion_aru.cursor(dictionary=True)
        
        cursor_aru.execute(
            'SELECT id_usuario as id, nombre, correo, rol FROM usuarios'
        )
        filas_resultado = cursor_aru.fetchall()
        cursor_aru.close()
        conexion_aru.close()
        
        return jsonify(filas_resultado)
    except Exception as excepcion_aru:
        return jsonify({'error': str(excepcion_aru)}), 500


@admin_aru.route('/users/<int:id_usuario>/bolsillos', methods=['GET'])
@admin_requerido
def obtener_bolsillos_usuario_aru(id_usuario):
    """Obtiene todos los bolsillos de un usuario específico"""
    try:
        conexion_aru = get_connection()
        cursor_aru = conexion_aru.cursor(dictionary=True)
        
        cursor_aru.execute(
            'SELECT id_bolsillo as id, nombre, fecha_creacion as fecha, monto as saldo FROM bolsillos WHERE usuario_id = %s', 
            (id_usuario,)
        )
        filas_resultado = cursor_aru.fetchall()
        cursor_aru.close()
        conexion_aru.close()
        
        return jsonify(filas_resultado)
    except Exception as excepcion_aru:
        return jsonify({'error': str(excepcion_aru)}), 500


@admin_aru.route('/users/<int:id_usuario>/pagos', methods=['GET'])
@admin_requerido
def obtener_pagos_usuario_aru(id_usuario):
    """Obtiene todos los pagos automáticos de un usuario específico"""
    try:
        conexion_aru = get_connection()
        cursor_aru = conexion_aru.cursor(dictionary=True)
        
        cursor_aru.execute(
            'SELECT id_pago as id, nombre, monto, fecha FROM pagos_automaticos WHERE usuario_id = %s', 
            (id_usuario,)
        )
        filas_resultado = cursor_aru.fetchall()
        cursor_aru.close()
        conexion_aru.close()
        
        return jsonify(filas_resultado)
    except Exception as excepcion_aru:
        return jsonify({'error': str(excepcion_aru)}), 500

