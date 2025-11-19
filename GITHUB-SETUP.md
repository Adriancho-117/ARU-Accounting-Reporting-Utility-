# 🚀 Cómo Subir el Proyecto a GitHub

## Paso 1: Crear Repositorio en GitHub

1. Ve a [github.com](https://github.com) y accede a tu cuenta
2. Haz clic en `+` (arriba a la derecha) → `New repository`
3. **Nombre del repositorio:** `proyecto-aru`
4. **Descripción:** Sistema de gestión de billeteras digitales
5. Selecciona `Public` o `Private` según prefieras
6. **NO** marques "Initialize this repository with a README"
7. Haz clic en `Create repository`

## Paso 2: Conectar tu Repositorio Local

Una vez creado, GitHub te mostrará comandos. Ejecuta en PowerShell en la carpeta del proyecto:

```powershell
git remote add origin https://github.com/TU_USUARIO/proyecto-aru.git
git branch -M main
git push -u origin main
```

**Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub**

## Alternativa: Si ya hay un remoto existente

```powershell
git remote -v  # Ver remoto actual
git remote remove origin  # Eliminar remoto viejo
git remote add origin https://github.com/TU_USUARIO/proyecto-aru.git
git push -u origin main
```

## Paso 3: Verificar en GitHub

1. Actualiza la página de GitHub
2. Deberías ver todos tus archivos subidos
3. El README.md se mostrará automáticamente

## Pasos Posteriores (Opcionales)

### Añadir Descripción al Repositorio
- Haz clic en el engranaje ⚙️ (Settings)
- En "Description", añade: "Sistema web de gestión de billeteras digitales con separación frontend/backend"
- En "Website", puedes añadir una URL (si la tienes)
- Guarda cambios

### Configurar Rama Principal
- Ve a Settings → Branches
- Asegúrate que `main` sea la rama por defecto

### Añadir Temas (Topics)
- Ve a Settings
- En "Topics", añade: `python`, `flask`, `javascript`, `html5`, `billetera`, `finanzas`

## ⚠️ Importante

- El proyecto ya tiene `.gitignore` configurado
- No se subirán archivos de `__pycache__`, `.env`, etc.
- Todos los archivos necesarios ya están listos

## 📋 Checklist Antes de Hacer Push

- ✅ `.gitignore` creado
- ✅ Duplicados eliminados
- ✅ `backend-aru/` removido
- ✅ Documentación limpia
- ✅ Commit inicial hecho
- ✅ README.md actualizado

## 🔗 Resultado Final

Tu repositorio estará en:
```
https://github.com/TU_USUARIO/proyecto-aru
```

## Comandos Útiles Post-Push

```powershell
# Ver estado
git status

# Ver commits
git log --oneline

# Ver cambios
git diff

# Crear rama nueva (para desarrollo)
git checkout -b desarrollo

# Ver ramas
git branch -a
```

---

¡Tu proyecto está listo para compartir con el mundo! 🎉
