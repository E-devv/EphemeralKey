# EphemeralKey 🔑

*Tu navaja suiza para la seguridad y el anonimato en línea.*

---

## 📜 Descripción General

**EphemeralKey** es una herramienta de línea de comandos (CLI) diseñada para fortalecer tu seguridad digital. Con una doble función, te permite generar **contraseñas criptográficamente seguras** y **direcciones de correo electrónico temporales simuladas**, todo desde la comodidad de tu terminal.

- **Seguridad primero**: Crea contraseñas robustas y difíciles de adivinar.
- **Anonimato simplificado**: Genera correos electrónicos desechables para registros en línea sin comprometer tu bandeja de entrada principal.

---

## ✨ Características

- **Generador de Contraseñas Personalizable**:
  - Define la longitud de tus contraseñas.
  - Incluye o excluye mayúsculas, minúsculas, números y símbolos.
- **Simulador de Correo Temporal**:
  - Crea direcciones de correo electrónico con un solo comando.
  - Personaliza el dominio para simular diferentes proveedores.
- **Desarrollo Multi-plataforma**:
  - Implementado en **Python** para una máxima compatibilidad.
  - Próximamente portado a **Go** para obtener binarios nativos y un rendimiento superior.

---

## 🚀 Instalación

Para empezar a usar EphemeralKey, solo necesitas tener Python 3 instalado y seguir estos sencillos pasos.

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/ephemeralkey.git
   cd ephemeralkey
   ```

2. **Requisitos**:
   - El script no requiere dependencias externas, solo una instalación estándar de Python 3.

---

## 💻 Uso (Ejemplos CLI)

La herramienta es muy fácil de usar. Aquí tienes algunos ejemplos:

1. **Generar solo una contraseña**:
   - `python ephemeralkey.py --password`
   - Para una contraseña de 20 caracteres y con símbolos:
     ```bash
     python ephemeralkey.py --password -l 20 -s
     ```

2. **Generar solo un correo electrónico temporal**:
   - `python ephemeralkey.py --email`
   - Para usar un dominio personalizado:
     ```bash
     python ephemeralkey.py --email -d mytempdomain.com
     ```

3. **Generar ambos (contraseña y correo) a la vez**:
   ```bash
   python ephemeralkey.py --all
   ```

---

## 🔮 Desarrollo Futuro

Tenemos grandes planes para EphemeralKey. Las próximas mejoras incluyen:

- **Portabilidad a Go**: Reescribir la herramienta en Go para compilarla en un único binario ejecutable, eliminando la necesidad de un intérprete de Python.
- **Integración de una GUI (Interfaz Gráfica de Usuario)**: Desarrollar una interfaz gráfica sencilla para aquellos que prefieren no usar la terminal.

---

Hecho con ❤️ por tu equipo de desarrollo.
