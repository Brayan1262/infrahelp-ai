def get_recommendation(category: str, description: str) -> dict:
    description_lower = description.lower()
    
    possible_cause = f"Incidencia de tipo {category} requiere revisión técnica detallada para identificar la causa raíz."
    recommended_steps = ["Revisar logs del sistema", "Escalar a soporte de nivel superior si es necesario"]

    if category == "REDES":
        if any(word in description_lower for word in ["lento", "lentitud", "demora", "ancho de banda"]):
            possible_cause = "Saturación de red o alto consumo de ancho de banda."
            recommended_steps = [
                "Validar consumo de red.",
                "Revisar equipos conectados.",
                "Identificar descargas o tráfico inusual.",
                "Aplicar priorización de tráfico si corresponde."
            ]
        elif any(word in description_lower for word in ["internet", "wifi", "red", "conexión", "conectado", "gateway", "dns", "ip"]):
            possible_cause = "Problema de conectividad, DNS, gateway o configuración IP."
            recommended_steps = [
                "Verificar conexión física o WiFi.",
                "Ejecutar ipconfig para validar IP, gateway y DNS.",
                "Hacer ping al gateway.",
                "Hacer ping a 8.8.8.8.",
                "Hacer ping a google.com para descartar problema DNS."
            ]

    elif category == "VIDEOVIGILANCIA":
        if any(word in description_lower for word in ["camara", "cámara", "ip", "monitoreo", "video", "nvr", "dvr", "hikvision", "milestone", "visualiza"]):
            possible_cause = "Cámara IP sin conectividad, problema de energía PoE, IP incorrecta o falla en NVR/VMS."
            recommended_steps = [
                "Verificar alimentación eléctrica o PoE de la cámara.",
                "Confirmar que la cámara tenga una IP válida.",
                "Hacer ping a la IP de la cámara.",
                "Revisar conexión al switch o puerto PoE.",
                "Validar credenciales y configuración en NVR/VMS.",
                "Revisar si la cámara aparece en la red."
            ]

    elif category == "IMPRESORA":
        if any(word in description_lower for word in ["impresora", "imprimir", "cola", "toner", "papel", "driver"]):
            possible_cause = "Problema de conectividad, cola de impresión, driver o consumibles."
            recommended_steps = [
                "Verificar que la impresora esté encendida y conectada.",
                "Revisar IP de la impresora y hacer ping.",
                "Validar cola de impresión.",
                "Reiniciar servicio de impresión.",
                "Revisar driver, papel y tóner."
            ]

    elif category == "CORREO":
        if any(word in description_lower for word in ["correo", "outlook", "enviar", "recibir", "smtp", "imap", "exchange", "buzón"]):
            possible_cause = "Problema de configuración de correo, conectividad con servidor o credenciales."
            recommended_steps = [
                "Verificar conexión a internet.",
                "Validar credenciales del usuario.",
                "Revisar configuración SMTP/IMAP/Exchange.",
                "Probar envío desde webmail.",
                "Revisar tamaño de adjuntos y espacio del buzón."
            ]

    elif category == "WINDOWS_SERVER":
        if any(word in description_lower for word in ["servidor", "dominio", "active directory", "usuario", "permisos", "carpeta compartida", "login"]):
            possible_cause = "Problema de permisos, autenticación, servicio de dominio o recurso compartido."
            recommended_steps = [
                "Validar conectividad con el servidor.",
                "Revisar usuario y grupo en Active Directory.",
                "Verificar permisos NTFS y permisos de recurso compartido.",
                "Revisar visor de eventos.",
                "Confirmar que los servicios necesarios estén activos."
            ]

    elif category == "BASE_DE_DATOS":
        if any(word in description_lower for word in ["base de datos", "postgresql", "mysql", "sql", "conexión", "consulta", "servidor bd"]):
            possible_cause = "Problema de conexión, credenciales, servicio detenido o saturación de base de datos."
            recommended_steps = [
                "Verificar que el servicio de base de datos esté activo.",
                "Validar host, puerto, usuario y contraseña.",
                "Revisar logs de la base de datos.",
                "Probar conexión manual.",
                "Verificar consumo de CPU, RAM y disco."
            ]

    elif category == "SEGURIDAD":
        if any(word in description_lower for word in ["virus", "acceso", "contraseña", "bloqueo", "intento", "sospechoso", "malware", "phishing"]):
            possible_cause = "Posible incidente de seguridad, credenciales comprometidas o intento de acceso no autorizado."
            recommended_steps = [
                "Bloquear temporalmente la cuenta si corresponde.",
                "Revisar intentos fallidos de acceso.",
                "Cambiar contraseña del usuario.",
                "Escanear el equipo con antivirus.",
                "Revisar logs de seguridad.",
                "Escalar al responsable de seguridad TI."
            ]

    elif category == "HARDWARE":
        if any(word in description_lower for word in ["laptop", "pc", "pantalla", "disco", "memoria", "ram", "apagado", "calienta", "teclado", "mouse"]):
            possible_cause = "Posible falla física de hardware, sobrecalentamiento o problema de componentes."
            recommended_steps = [
                "Revisar conexión eléctrica y periféricos.",
                "Verificar temperatura del equipo.",
                "Revisar estado de disco y memoria.",
                "Probar con otro cargador o periférico.",
                "Escalar a mantenimiento si la falla persiste."
            ]

    elif category == "SOFTWARE":
        if any(word in description_lower for word in ["programa", "aplicación", "sistema", "error", "instalar", "actualizar", "licencia"]):
            possible_cause = "Error de aplicación, instalación incompleta, incompatibilidad o licencia vencida."
            recommended_steps = [
                "Reiniciar la aplicación.",
                "Validar mensaje de error.",
                "Revisar versión instalada.",
                "Actualizar o reinstalar el software.",
                "Revisar permisos del usuario."
            ]

    elif category == "SISTEMA_LENTO":
        if any(word in description_lower for word in ["lento", "demora", "congelado", "cpu", "memoria", "disco", "rendimiento"]):
            possible_cause = "Alto consumo de recursos, procesos en segundo plano o saturación del equipo."
            recommended_steps = [
                "Revisar uso de CPU, memoria y disco.",
                "Cerrar procesos innecesarios.",
                "Verificar espacio libre en disco.",
                "Revisar programas de inicio.",
                "Escanear malware.",
                "Reiniciar el equipo y validar rendimiento."
            ]

    return {
        "possible_cause": possible_cause,
        "recommended_steps": recommended_steps
    }
