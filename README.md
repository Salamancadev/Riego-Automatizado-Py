# Riego-Automatizado-Py
📝 Guía para iniciar el entorno de pruebas del proyecto Django
🔁 Paso 1: Clonar el repositorio
Abre una terminal (PowerShell o CMD) y clona el proyecto:
git clone [git@github.com:Salamancadev/Riego-Automatizado-Py.git](https://github.com/Salamancadev/Riego-Automatizado-Py.git)
cd proyecto-riego
🐍 Paso 2: Crear y activar el entorno virtual
🔹 En Windows (CMD o PowerShell):
python -m venv venv_riego
venv_riego\Scripts\activate
🔹 En WSL (Linux):
python3 -m venv venv_riego
source venv_riego/bin/activate
📦 Paso 3: Instalar las dependencias
Entrar a la carpeta backend y ejecutar:
cd backend
python -m pip install -r requirements.txt
⚙️ Paso 4: Migrar la base de datos
python manage.py makemigrations
python manage.py migrate
🚀 Paso 5: Ejecutar el servidor de desarrollo
python manage.py runserver
Esto ejecuta en http://127.0.0.1:8000/
