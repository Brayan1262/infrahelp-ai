# InfraHelp AI

InfraHelp AI es una plataforma inteligente para el análisis de tickets de soporte técnico e infraestructura TI. El sistema permite ingresar una descripción de incidencia técnica y devuelve categoría, prioridad, posible causa y pasos recomendados de solución usando Inteligencia Artificial.

## Tecnologías Utilizadas

- **Backend**: Python 3.12, FastAPI, Pydantic, Scikit-learn, Pandas, SQLite.
- **Frontend**: Angular, TypeScript, HTML, CSS, Bootstrap (o estilos modernos).

## Estructura del Proyecto

- `/backend`: API REST construida con FastAPI y los modelos de IA.
- `/frontend`: Interfaz de usuario construida con Angular.

## Ejecutar Backend

1. Entrar a la carpeta `backend`:
   ```bash
   cd backend
   ```
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
5. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

## Ejecutar Frontend

1. Entrar a la carpeta `frontend`:
   ```bash
   cd frontend
   ```
2. Instalar las dependencias:
   ```bash
   npm install
   ```
3. Ejecutar el servidor de desarrollo:
   ```bash
   ng serve
   ```
   (O usa `npm start`)
