# python mvc

## Descripción 

Este proyecto es una aplicación de lista de tareas implementada en Python utilizando el patrón de diseño Modelo-Vista-Controlador (MVC). 

La aplicación permite a los usuarios agregar tareas con un título y una descripción. Cada tarea se asigna un ID único que comienza en 0 y se incrementa para cada nueva tarea. Las tareas se pueden marcar como completadas o incompletas.

El proyecto está estructurado de la siguiente manera:

- `model/`: Contiene la lógica de negocio del proyecto. Incluye la definición de la clase `Task` y `TaskList`.
- `view/`: Contiene la lógica de la interfaz de usuario. Incluye la definición de la clase `TaskView`.
- `controller/`: Contiene la lógica de control del proyecto. Incluye la definición de la clase `TaskController`.
- `main.py`: Es el punto de entrada de la aplicación.

mvc_python/
│
├── model/
│   ├── __init__.py  
│   └── model.py     # Contiene las clases `Task` y `TaskList`
│
├── view/
│   ├── __init__.py  
│   └── view.py      # Contiene la clase `TaskView` para la GUI de Tkinter
│
├── controller/
│   ├── __init__.py 
│   └── controller.py # Contiene la clase `TaskController`
│
└── main.py  # Punto de entrada de la aplicación


## Uso

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
2. Navega hasta el directorio del proyecto.
3. Ejecuta el archivo `main.py` con Python.

```bash
git clone https://github.com/criveraapex/python_mvc-ac-ex.git
cd python_mvc-ac-ex
python main.py