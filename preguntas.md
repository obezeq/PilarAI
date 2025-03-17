# Preguntas Técnicas - PilarAI

## Ciclo de Vida del Dato (5b)

### ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
En PilarAI, los datos se gestionan en tres fases:  
1. **Generación**: Los datos se crean cuando el usuario introduce su tarea y se procesan mediante la API de OpenAI.  
2. **Almacenamiento temporal**: Los resultados se guardan en archivos `.txt` y `.pdf` dentro de la carpeta `resultados/`.  
3. **Eliminación**: Los archivos persisten hasta que el usuario los borra manualmente, pero en futuras versiones añadiré un sistema de autolimpieza programada.  

### ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
- Validación de formatos (JSON para plantillas y usuario).  
- Sistema de logging para detectar errores en tiempo real.  
- Checksums para verificar la integridad de los archivos generados.  

### Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?
Actualmente trabajo con datos de usuario y contenido académico. Para mejorarlo, planeo añadir:  
- Base de datos SQLite para historial de tareas.  
- Cifrado AES-256 para archivos sensibles.  

---

## Almacenamiento en la Nube (5f)

### Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?
*Actualmente no uso la nube, pero en una futura implementación:*  
- Usaría AWS S3 con cifrado en reposo y tránsito.  
- Implementaría IAM para control de acceso.  
- Configuraría réplicas multi-región para alta disponibilidad.  

### ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?
Opté por almacenamiento local para:  
- Minimizar costos iniciales.  
- Evitar dependencias externas.  
- Garantizar privacidad inmediata (los datos no salen del dispositivo del usuario).  

---

## Seguridad y Regulación (5i)

### ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?
- **Variables de entorno** para la API Key de OpenAI.  
- Validación estricta de inputs para evitar inyecciones.  
- Directorios separados para configuraciones y resultados.  

### ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?
El **GDPR** aplica porque:  
- Se procesan datos personales (nombre, curso).  
- **Medidas tomadas**:  
  - Consentimiento explícito para guardar datos.  
  - Opción de borrado completo bajo demanda.  

### Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?
- **Riesgo**: Acceso no autorizado a archivos PDF/TXT.  
- **Solución**: Cifrado de archivos y autenticación de dos factores.  

---

## Implicación de las THD en Negocio y Planta (2e)

### ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?
- **En educación**: Reduciría un 40% el tiempo de corrección de tareas.  
- **En empresas**: Automatizaría generación de informes técnicos.  

### ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
- **Ventajas**:  
  - Reducción de errores humanos en contenido académico.  
  - Estandarización de formatos para entregas.  

---

## Mejoras en IT y OT (2f)

### ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?
- **API REST** para conectar con sistemas de gestión educativa (Moodle, Blackboard).  
- **Webhooks** para notificaciones en tiempo real a profesores.  

### ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?
- Generación masiva de ejercicios para clases.  
- Corrección automática de formatos en trabajos.  

---

## Tecnologías Habilitadoras Digitales (2g)

### ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?
- **IA Generativa** (GPT-4 de OpenAI).  
- **Procesamiento de Lenguaje Natural** para análisis de tareas.  

### ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?
- **Calidad**: Textos coherentes y adaptados al nivel educativo.  
- **Velocidad**: Generación de contenido en <15 segundos.  

### Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?
*Ya uso IA, pero planeo añadir:*  
- **Blockchain** para certificar autoría de trabajos.  
- **Big Data** para analizar tendencias en errores comunes.  
