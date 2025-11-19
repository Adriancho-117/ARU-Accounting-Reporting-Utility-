def verificar_token_aru(token_aru: str):
    """
    Implementación de verificación de token para ARU en desarrollo.
    - Si el token == 'demo' devuelve id_usuario=1
    - Si el token es un número, lo acepta como id_usuario
    - En producción reemplazar por verificación JWT con seguridad completa
    """
    if not token_aru:
        return None
    
    # Token de demostración para pruebas
    if token_aru == 'demo':
        return {"user_id": 1}
    
    # Aceptar token numérico como id de usuario (para desarrollo)
    try:
        id_usuario_aru = int(token_aru)
        return {"user_id": id_usuario_aru}
    except Exception:
        return None


# Alias para compatibilidad con código existente
verify_token = verificar_token_aru

