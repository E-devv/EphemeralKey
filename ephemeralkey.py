import random
import string
import argparse
import sys

# Importar pyperclip con manejo de errores si no está instalado
try:
    import pyperclip
except ImportError:
    pyperclip = None


# --- GENERADOR DE CONSTRSEÑAS ---


def generate_strong_password(
    length=16,
    use_upper=True,
    use_lower=True,
    use_digits=True,
    use_symbols=True
):
    """
    Genera una contraseña fuerte y aleatoria basada en parámetros de
    complejidad.
    """

    # 1. Definir los conjuntos de caracteres disponibles
    characters = ""
    # Aseguramos que haya al menos un caracter de cada tipo seleccionado
    # (Paso A)
    password_list = []

    if use_upper:
        characters += string.ascii_uppercase
        password_list.append(random.choice(string.ascii_uppercase))
    if use_lower:
        characters += string.ascii_lowercase
        password_list.append(random.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password_list.append(random.choice(string.digits))

    # Símbolos comunes y seguros
    symbols = "!@#$%^&*()-_=+"
    if use_symbols:
        characters += symbols
        password_list.append(random.choice(symbols))

    # 2. Verificar que al menos un conjunto de caracteres esté seleccionado
    if not characters:
        raise ValueError(
            "Debes seleccionar al menos un tipo de caracter para generar la "
            "contraseña."
        )

    # 3. Rellenar el resto de la longitud (Paso B)
    remaining_length = length - len(password_list)
    if remaining_length > 0:
        # Usamos random.choices para llenar el resto con caracteres aleatorios
        # de cualquier tipo
        password_list.extend(random.choices(characters, k=remaining_length))

    # 4. Mezclar la lista para asegurar la aleatoriedad
    random.shuffle(password_list)

    # 5. Convertir la lista a cadena (string)
    return "".join(password_list)


# --- GENERADOR DE CORREO TEMPORAL ---


def generate_temp_email(username_length=12, domain="ephemeral.key"):
    """
    Genera una dirección de correo electrónico temporal simulada.
    """

    # Usamos solo letras minúsculas y dígitos para el nombre de usuario del
    # correo
    characters = string.ascii_lowercase + string.digits

    if not characters:
        raise ValueError(
            "No se pudo generar el conjunto de caracteres para el nombre de "
            "usuario."
        )

    # Generamos la cadena aleatoria del nombre de usuario
    username = "".join(random.choices(characters, k=username_length))

    # Combinamos el nombre de usuario con el dominio
    return f"{username}@{domain}"


# --- INTERFAZ DE LÍNEA DE COMANDOS (CLI) ---


def main():
    """
    Función principal que maneja los argumentos de la línea de comandos.
    """
    parser = argparse.ArgumentParser(
        description=(
            "EphemeralKey: Generador CLI de credenciales seguras "
            "(contraseñas y correos temporales)."
        ),
        epilog=(
            "Ejemplos: python ephemeralkey.py --password -l 18 -s -c | "
            "python ephemeralkey.py --email --copy"
        )
    )

    # Argumentos para el tipo de generación
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-p', '--password', action='store_true',
        help='Generar una contraseña segura.'
    )
    group.add_argument(
        '-e', '--email', action='store_true',
        help='Generar una dirección de correo temporal.'
    )
    group.add_argument(
        '-a', '--all', action='store_true',
        help='Generar tanto la contraseña como el correo.'
    )

    # Argumentos para la Contraseña
    parser.add_argument(
        '-l', '--length', type=int, default=16,
        help='Longitud de la contraseña a generar (por defecto: 16).'
    )
    parser.add_argument(
        '-s', '--symbols', action='store_true',
        help='Incluir símbolos en la contraseña.'
    )
    parser.add_argument(
        '--no-upper', action='store_true', help='Excluir letras mayúsculas.'
    )
    parser.add_argument(
        '--no-lower', action='store_true', help='Excluir letras minúsculas.'
    )
    parser.add_argument(
        '--no-digits', action='store_true', help='Excluir dígitos.'
    )

    # Argumentos para el Correo
    parser.add_argument(
        '-d', '--domain', type=str, default='ephemeral.key',
        help='Dominio a usar para el correo temporal (por defecto: '
             'ephemeral.key).'
    )
    parser.add_argument(
        '-ul', '--user-length', type=int, default=12,
        help='Longitud del nombre de usuario del correo (por defecto: 12).'
    )

    # Argumento para copiar al portapapeles
    parser.add_argument(
        '-c', '--copy', action='store_true',
        help='Copiar el resultado al portapapeles.'
    )

    args = parser.parse_args()

    output_to_copy = []

    try:
        if args.password or args.all:
            # Generar Contraseña
            password = generate_strong_password(
                length=args.length,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                use_digits=not args.no_digits,
                use_symbols=args.symbols
            )
            print(f"🔑 Contraseña Generada: {password}")
            output_to_copy.append(password)

        if args.email or args.all:
            # Generar Correo
            email = generate_temp_email(
                username_length=args.user_length,
                domain=args.domain
            )
            print(f"📧 Correo Temporal: {email}")
            output_to_copy.append(email)

        # Copiar al portapapeles si se especifica
        if args.copy:
            if not pyperclip:
                print(
                    "\n⚠️  Error: La librería 'pyperclip' no está instalada. "
                    "No se pudo copiar al portapapeles.", file=sys.stderr
                )
                print(
                    "   Para instalarla, ejecuta: pip install pyperclip",
                    file=sys.stderr
                )
                sys.exit(1)

            try:
                # Unir los resultados con un salto de línea si hay más de uno
                pyperclip.copy("\n".join(output_to_copy))
                print("\n✅ ¡Resultado copiado al portapapeles!")
            except pyperclip.PyperclipException as e:
                print(
                    f"\n❌ Error: No se pudo acceder al portapapeles del "
                    f"sistema: {e}", file=sys.stderr
                )
                sys.exit(1)

    except ValueError as e:
        # Captura el error de validación de la función generadora
        print(f"Error al generar credenciales: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
