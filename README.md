# UNIVERISDAD TECNOLOGICA NACIONAL (UTN) --- TPI --- ORGANIZACION EMPRESARIAL --- 2026

Alumnas: Agustina Lobo & Chiara Aquino.

Fecha: 19/06/2026. 

Titulo: Sistema de Gestion de Solicitudes de Vacaciones

# DESCRIPCIÓN
VacacionesBot es un chatbot en Python que gestiona las solicitudes de vacaciones para la empresa ficticia STECH. Reemplaza el proceso manual de verificacion de días de vacaciones disponibles que realizaba el área de Recursos Humanos. 

# FUNCIONAMIENTO
El bot utiliza un archivo CSV como base de datos. En dicho archivo se registra el legajo de cada empleado y su saldo de dias de vacaciones. El bot realiza lecturas de este para consulta y ejecucion de actualizaciones. Esto permite mantener un registro de las acciones realizadas. 

El codigo se estructura mediante un sistema de estados: 

      1. Con el comando /start el bot inicia el primer estado y solicita el número de legajo del empleado;
      2. Ingresado el legajo, se transita al segundo estado; El usuario debe realizar una solicitud de la cantidad de días de vacaciones que desea concederse. 

Los parametros "LEGAJO" y "DÍAS" son necesarios para el procesamiento de la solicitud. Por lo tanto, obtenidos ambos datos el bot lee el archivo CSV para determinar los días disponibles del empleado;
       - Si tiene días suficientes: descuenta los días solicitados, realiza una actualización de valores y APRUEBA la solicitud.
       - Si presenta una cantidad de dias insuficientes, RECHAZA la solicitud.

El código en la terminal se desarrolla dentro de un ciclo while infinito. Al finalizar la consulta, ofrece como opción SALIR, la cual permite el cierre del bucle. 

El código python trasladado a API queda a la espera de nuevas solicitudes hasta que el usuario elige SALIR. 

# MANEJO DE ERRORES
El bot valida los datos ingresados por el usuario. Si cumplen con las condiciones establecidas en el código, se ejecutan las funciones correspondientes.

En el caso de ingresar referencias invalidas y/o que no cumplan con las condiciones del programa, devuelve mensajes de "ERROR", especifica por qué o solicita el ingreso de opciones válidas;
    1. "ERROR ❗. Legajo no encontrado🤔 Ingreselo nuevamente"
    2. "ERROR ❗. Ingrese solo numeros 🔢"
    3. "🚫Ingrese una opción válida: SOLICITAR o SALIR🚫"
    
# RESTRICCIÓN DE GUARDADO
El bot almacena una cantidad de días y realiza los descuentos solicitados en un archivo CSV local. La plataforma de mensajeria "Telegram" unicamente guarda el chat, no archivo. Por ello, los cambios no son permanentes si se reinicia el programa. 

# ENLACE A VIDEO DEMOSTRATIVO
El siguiente enlace redirige a un archivo de video en Google Drive, el cual permite visualizar la interacción entre el usuario y el bot. Mediante distintas solicitudes, se verifica el adecuado funcionamiento del manejo de errores programado. 

https://drive.google.com/file/d/1N8Ay-oG8y0tF74eonOKAd03jd7SRqxo-/view?usp=drive_link
