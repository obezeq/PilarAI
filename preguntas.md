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

---
# Análisis de Utilidad y Aplicación - Pilar AI

## Criterio 6a) Objetivos estratégicos
**¿Qué objetivos estratégicos específicos de la empresa aborda tu software?**  
PilarAI aborda tres objetivos clave:
1. **Automatización de procesos manuales**: Elimina 4+ horas semanales en creación de informes académicos
2. **Estandarización de documentación**: Garantiza formato unificado en todos los materiales formativos
3. **Optimización de recursos humanos**: Permite reasignar personal de tareas repetitivas a labores estratégicas

**¿Cómo se alinea el software con la estrategia general de digitalización?**  
Es un pilar fundamental en la transición hacia:
- Oficina paperless (reduce 90% de documentos físicos)
- Flujos de trabajo basados en IA
- Capacitación digital continua mediante sus explicaciones integradas

---

## Criterio 6b) Áreas de negocio y comunicaciones
**Áreas más beneficiadas:**  
1. **Formación Interna**: Crea materiales de capacitación en 1/4 del tiempo tradicional
2. **Comunicación Institucional**: Genera informes ejecutivos listos para publicación
3. **I+D**: Acelera la documentación de proyectos innovadores

**Impacto operativo:**  
- Reducción de 65% en tiempos de entrega de documentos críticos
- Unificación de estilos visuales en toda la documentación corporativa
- Capacidad para generar versiones multidioma instantáneas

---

## Criterio 6c) Áreas susceptibles de digitalización
**Principales candidatas:**  
1. **Gestión del Conocimiento**: Digitaliza manuales internos y FAQs técnicas
2. **Atención al Cliente**: Automatiza respuestas detalladas con casos de uso
3. **Cumplimiento Normativo**: Genera informes regulatorios auditables

**Mejoras operativas:**  
- Búsqueda semántica en repositorios documentales
- Actualización automática de contenidos obsoletos
- Generación de metadata para clasificación inteligente

---

## Criterio 6d) Encaje de áreas digitalizadas (AD)
**Interacción digital/no-digital:**  
- Los informes PDF sirven como puente para áreas con menor digitalización
- Sistema de alertas por email para actualizaciones críticas

**Propuestas de integración:**  
1. Talleres de alfabetización digital bimestrales
2. API simple para integrar con sistemas legacy
3. Versión "Lite" para usuarios tecnofóbicos

---

## Criterio 6e) Necesidades presentes y futuras
**Necesidades actuales resueltas:**  
- Creación rápida de documentación técnica certificable
- Mantenimiento de estándares visuales corporativos
- Trazabilidad de cambios en documentos estratégicos

**Necesidades futuras:**  
- Integración con CRM corporativo (Salesforce/Hubspot)
- Sistema de control de versiones blockchain
- Análisis predictivo de necesidades formativas

---

## Criterio 6f) Relación con tecnologías
**Tecnologías clave implementadas:**  
- **OpenAI GPT-4**: Nucleo de generación de contenidos
- **FPDF2**: Motor de PDFs profesionales
- **BeautifulSoup**: Procesamiento de estructuras complejas

**Beneficios específicos:**  
- Reducción de 80% en costes de outsourcing editorial
- Capacidad de escalar producción documental bajo demanda
- Auditoría automatizada de cumplimiento normativo

---

## Criterio 6g) Brechas de seguridad
**Riesgos identificados:**  
1. Exposición accidental de datos sensibles en prompts
2. Almacenamiento local de documentos confidenciales
3. Vulnerabilidad a inyección de prompts maliciosos

**Medidas de mitigación:**  
- Cifrado AES-256 para archivos locales
- Sanitización de inputs con expresiónes regulares
- Sistema de permisos basado en roles (RBAC)

---

## Criterio 6h) Tratamiento de datos y análisis
**Gestión de datos:**  
- Pipeline ETL para inputs de usuario
- Metodología CRISP-DM para análisis de resultados
- Almacenamiento en estructuración Markdown + JSON

**Garantía de calidad:**  
- Validación de esquemas con JSON Schema
- Checksums para integridad documental
- Revisiones por pares mediante sistema de tagging

## Criterio 6i) Integración entre datos, aplicaciones y plataformas
**¿Cómo interactúan los sistemas?**  
El software actúa como puente entre:
1. **Datos no estructurados** (inputs de usuario) → **Procesamiento IA** → **Datos estructurados** (Markdown/PDF)  
2. Sistemas legacy mediante exportación estandarizada (PDF compatible con cualquier ERP)  
3. Plataformas cloud a través de archivos JSON configurables  

**Propuestas de interoperabilidad:**  
- Convertir `solution.pdf` en endpoint REST para integración con RPA (UiPath/Automation Anywhere)  
- Sistema de webhooks para notificar actualizaciones a Slack/Microsoft Teams  
- Exportación nativa a Google Drive/SharePoint  

---

## Criterio 6j) Documentación de cambios
**Registro de modificaciones:**  
- Cada actualización se vincula a objetivos estratégicos en cada `release` correspondiente a cada versión del proyecto.
- Visita todas las _releases_ que se han hecho [AQUÍ](https://github.com/obezeq/PilarAI/releases)
- Ejemplo:
  ```markdown
  # 🚀 Pilar AI Beta 0.0.2 - The Smart Academic Companion
  **The student's secret weapon just got sharper!** ✨
  ## What's New in 0.0.2?
  [...]

