/* ============================================
   ARU - App Frontend Principal
   Sistema de Gestión Financiera
   ============================================ */

// Usar configuración centralizada (ver config.js)
// Si config.js no está disponible, usar valor por defecto
const API_BASE = typeof CONFIG !== 'undefined' ? CONFIG.API_BASE : "http://localhost:5000";

// ============================================
// INICIALIZACIÓN
// ============================================

window.addEventListener('DOMContentLoaded', () => {
    // Cargar bolsillos si existe el contenedor
    if (document.getElementById('listaBolsillos')) {
        cargarBolsillos();
    }

    // Vincular botón de crear bolsillo si existe
    const crearBolsilloBtn = document.getElementById('crearBolsilloBtn');
    if (crearBolsilloBtn) {
        crearBolsilloBtn.addEventListener('click', crearBolsillo);
    }

    // Mostrar saludo del usuario
    const userGreeting = document.getElementById('userGreeting');
    const usuarioId = localStorage.getItem('usuario_id');
    if (userGreeting) {
        userGreeting.textContent = usuarioId ? `👤 Usuario ${usuarioId}` : '👤 Hola';
    }

    // Actualizar badges
    actualizarBadges();
});

// ============================================
// BADGES Y NOTIFICACIONES
// ============================================

function mostrarBadge(elementoId, cantidad) {
    const elemento = document.getElementById(elementoId);
    if (!elemento) return;
    
    if (!cantidad || cantidad <= 0) {
        elemento.style.display = 'none';
    } else {
        elemento.style.display = 'inline-flex';
        elemento.textContent = String(cantidad);
    }
}

async function actualizarBadgeBolsillos() {
    try {
        const token = localStorage.getItem('token');
        if (!token) { mostrarBadge('badgeBolsillos', 0); return; }
        
        const resp = await fetch(`${API_BASE}/api/bolsillos`, { 
            method: 'GET', 
            headers: { Authorization: 'Bearer ' + token } 
        });
        
        if (!resp.ok) { mostrarBadge('badgeBolsillos', 0); return; }
        
        const datos = await resp.json().catch(() => []);
        mostrarBadge('badgeBolsillos', Array.isArray(datos) ? datos.length : 0);
    } catch (err) {
        console.error('Error actualizando badge de bolsillos:', err);
        mostrarBadge('badgeBolsillos', 0);
    }
}

async function actualizarBadgePagos() {
    try {
        const usuarioId = localStorage.getItem('usuario_id');
        if (!usuarioId) { mostrarBadge('badgePagos', 0); return; }
        
        const resp = await fetch(`${API_BASE}/pagos_automaticos/${usuarioId}`);
        if (!resp.ok) { mostrarBadge('badgePagos', 0); return; }
        
        const datos = await resp.json().catch(() => []);
        mostrarBadge('badgePagos', Array.isArray(datos) ? datos.length : 0);
    } catch (err) {
        console.error('Error actualizando badge de pagos:', err);
        mostrarBadge('badgePagos', 0);
    }
}

function actualizarBadges() {
    actualizarBadgeBolsillos();
    actualizarBadgePagos();
}

// ============================================
// BOLSILLOS
// ============================================

async function cargarBolsillos() {
    const token = localStorage.getItem("token");
    const resp = await fetch(`${API_BASE}/api/bolsillos`, {
        method: "GET",
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    if (!resp.ok) {
        if (resp.status === 401 || resp.status === 403) {
            window.location.href = 'login.html';
        }
        return;
    }

    const bolsillos = await resp.json();
    const contenedorBolsillos = document.getElementById('listaBolsillos');
    contenedorBolsillos.innerHTML = '';

    if (bolsillos.length === 0) {
        contenedorBolsillos.innerHTML = '<div class="info-box">No tienes bolsillos aún. ¡Crea uno para comenzar a ahorrar!</div>';
        return;
    }

    bolsillos.forEach(bolsillo => {
        const elementoBolsillo = document.createElement('div');
        elementoBolsillo.classList.add('bolsillo-item');

        const saldoFormateado = new Intl.NumberFormat('es-CO', { 
            style: 'currency', 
            currency: 'COP' 
        }).format(bolsillo.saldo || 0);

        const fechaFormato = bolsillo.fecha 
            ? new Date(bolsillo.fecha).toLocaleDateString('es-CO')
            : 'Sin fecha';

        elementoBolsillo.innerHTML = `
            <div>
                <h4 style="margin: 0 0 var(--spacing-sm) 0;">${bolsillo.nombre}</h4>
                <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary);">
                    📅 ${fechaFormato}
                </p>
            </div>
            <div class="list-item-value">${saldoFormateado}</div>
        `;

        contenedorBolsillos.appendChild(elementoBolsillo);
    });
}

async function crearBolsillo() {
    const nombreElemento = document.getElementById('nombreBolsillo');
    const fechaElemento = document.getElementById('fechaDesembolso');
    const saldoElemento = document.getElementById('saldoInicial');

    if (!nombreElemento) return;

    const nombreBolsillo = nombreElemento.value;
    const fechaDesembolso = fechaElemento ? fechaElemento.value : null;
    const saldoInicial = saldoElemento ? saldoElemento.value : 0;

    if (nombreBolsillo.trim() === '') {
        alert('Por favor ingresa un nombre para el bolsillo.');
        return;
    }

    const token = localStorage.getItem("token");
    if (!token) {
        alert('Debes iniciar sesión para crear un bolsillo.');
        window.location.href = 'login.html';
        return;
    }

    try {
        const resp = await fetch(`${API_BASE}/api/bolsillos/create`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                ...(token ? { "Authorization": "Bearer " + token } : {})
            },
            body: JSON.stringify({
                nombre: nombreBolsillo,
                fecha: fechaDesembolso,
                saldo: Number(saldoInicial || 0)
            })
        });

        let datos = {};
        try { datos = await resp.json(); } catch (e) { /* no JSON */ }

        if (!resp.ok) {
            console.error('Error crearBolsillo:', resp.status, datos);
            alert(datos.error || datos.mensaje || "Error al crear el bolsillo");
            return;
        }

        // Recargar lista
        if (document.getElementById('listaBolsillos')) cargarBolsillos();

        // Actualizar badges
        actualizarBadges();

        // Notificar otras pestañas
        try { localStorage.setItem('bolsillos_actualizado', Date.now().toString()); } catch(e){}

        // Limpiar campos
        nombreElemento.value = '';
        if (fechaElemento) fechaElemento.value = '';
        if (saldoElemento) saldoElemento.value = '';

        alert('¡Bolsillo creado exitosamente!');
    } catch (err) {
        console.error('Error creando bolsillo:', err);
        alert('No se pudo conectar con el servidor para crear el bolsillo.');
    }
}

// ============================================
// MODALES
// ============================================

function abrirModal(idModal) {
    const elemento = document.getElementById(idModal);
    if (!elemento) return;
    elemento.classList.add('visible');
    elemento.style.display = 'flex';
}

function cerrarModal(idModal) {
    const elemento = document.getElementById(idModal);
    if (!elemento) return;
    elemento.classList.remove('visible');
    elemento.style.display = 'none';
}

// Cerrar modal al hacer clic fuera
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal-bg')) {
        e.target.classList.remove('visible');
        e.target.style.display = 'none';
    }
});

// ============================================
// PAGOS AUTOMÁTICOS
// ============================================

async function crearPago() {
    const nombre = document.getElementById('pagoNombre')?.value;
    const monto = Number(document.getElementById('pagoMonto')?.value || 0);
    const fecha = document.getElementById('pagoFecha')?.value;

    if (!nombre || monto <= 0 || !fecha) {
        alert('Por favor completa todos los campos del pago.');
        return;
    }

    try {
        const token = localStorage.getItem('token');
        const usuarioId = localStorage.getItem('usuario_id');
        
        const cuerpo = { nombre, monto, fecha };
        if (usuarioId) cuerpo.usuario_id = Number(usuarioId);

        const resp = await fetch(`${API_BASE}/pagos_automaticos`, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json', 
                ...(token ? { Authorization: 'Bearer ' + token } : {}) 
            },
            body: JSON.stringify(cuerpo)
        });

        const datos = await resp.json().catch(() => ({}));
        
        if (!resp.ok) {
            console.error('Error crearPago:', resp.status, datos);
            alert(datos.error || datos.mensaje || 'Error al crear pago.');
            return;
        }

        alert('¡Pago automático creado correctamente!');
        cerrarModal('modalPago');

        // Actualizar badges
        actualizarBadges();

        // Notificar otras pestañas
        try { localStorage.setItem('pagos_actualizado', Date.now().toString()); } catch(e){}

        // Limpiar campos
        document.getElementById('pagoNombre').value = '';
        document.getElementById('pagoMonto').value = '';
        document.getElementById('pagoFecha').value = '';
    } catch (err) {
        console.error('Error creando pago:', err);
        alert('No se pudo conectar con el servidor para crear el pago.');
    }
}

// ============================================
// SALDO
// ============================================

async function obtenerSaldo(usuarioId) {
    if (!usuarioId) return;
    
    try {
        const resp = await fetch(`${API_BASE}/saldo/${usuarioId}`);
        if (!resp.ok) return;
        
        const datos = await resp.json();
        const elementoSaldo = document.getElementById('saldoTotal');
        
        if (elementoSaldo && datos && typeof datos.saldo !== 'undefined') {
            elementoSaldo.textContent = new Intl.NumberFormat('es-CO', { 
                style: 'currency', 
                currency: 'COP' 
            }).format(datos.saldo);
        }
    } catch (err) {
        console.error('Error al obtener saldo:', err);
    }
}

// ============================================
// AUTENTICACIÓN
// ============================================

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('usuario_id');
    window.location.href = 'login.html';
}

// ============================================
// ADMIN
// ============================================

async function cargarUsuariosAdmin() {
    const token = localStorage.getItem('token');
    if (!token) return;
    
    try {
        const resp = await fetch(`${API_BASE}/admin/users`, { 
            headers: { Authorization: 'Bearer ' + token } 
        });
        
        if (!resp.ok) return;
        return await resp.json();
    } catch (err) { 
        console.error('cargarUsuariosAdmin error:', err); 
    }
}

// ============================================
// ESCUCHADORES DE ALMACENAMIENTO
// ============================================

// Sincronizar cambios entre pestañas
window.addEventListener('storage', (e) => {
    if (e.key === 'bolsillos_actualizado') {
        actualizarBadges();
        if (document.getElementById('listaBolsillos')) cargarBolsillos();
    }
    if (e.key === 'pagos_actualizado') {
        actualizarBadges();
    }
});

// ============================================
// UTILIDADES
// ============================================

// Función para formatear moneda
function formatearMoneda(valor) {
    return new Intl.NumberFormat('es-CO', { 
        style: 'currency', 
        currency: 'COP' 
    }).format(valor);
}

// Función para formatear fecha
function formatearFecha(fecha) {
    return new Date(fecha).toLocaleDateString('es-CO', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}
