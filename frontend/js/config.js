/* ============================================
   CONFIGURACIÓN DE LA APLICACIÓN
   Centraliza las variables de configuración
   ============================================ */

const CONFIG = {
    // URL base del servidor backend
    API_BASE: "http://localhost:5000",
    
    // Configuración de almacenamiento
    STORAGE: {
        TOKEN_KEY: "token",
        USER_ID_KEY: "usuario_id",
        USER_EMAIL_KEY: "usuario_email",
        BOLSILLOS_UPDATE_KEY: "bolsillos_actualizado",
        PAGOS_UPDATE_KEY: "pagos_actualizado",
    },
    
    // Tiempos
    TIMEOUTS: {
        FETCH_TIMEOUT: 10000, // ms
        BADGE_UPDATE_INTERVAL: 30000, // ms
    },
    
    // Texto y mensajes
    MESSAGES: {
        ERROR_CONEXION: "No se pudo conectar con el servidor.",
        ERROR_AUTENTICACION: "Debes iniciar sesión.",
        ERROR_GENERICO: "Ocurrió un error. Intenta nuevamente.",
        EXITO_CREACION: "Creado exitosamente.",
        EXITO_ACTUALIZACION: "Actualizado exitosamente.",
        EXITO_ELIMINACION: "Eliminado exitosamente.",
    },
    
    // Formatos
    FORMATS: {
        LOCALE: "es-CO",
        CURRENCY: "COP",
        DATE_OPTIONS: {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        },
    },
};

// Exportar si se usa en módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
