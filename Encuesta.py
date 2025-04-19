# Configuración inicial
import streamlit as st # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore


# Configuración de la página
st.set_page_config(
    page_title="Técnicas y Habilidades de Estudio Universitarias", 
    page_icon="📚", 
    layout="wide"
)

# Título y descripción
st.title("📚 “Técnicas y Habilidades de Estudio Universitarias”")

st.markdown("""
**Objetivo:** Analizar las técnicas y habilidades de estudio del estudiantado del Instituto Tecnológico Superior de Apan 
            en el programa educativo de Ingeniería en Sistemas Computacionales de 2° 4° 6° y 8° semestre,
             con la finalidad de identificar áreas de oportunidad y proponer estrategias que aumenten el rendimiento académico.
""")

# Sección de datos demográficos
with st.expander("📝 Datos demográficos", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        sexo = st.text_input("Sexo")
    with col2:
        semestre = st.selectbox("Semestre", ["2do", "4to", "6to", "8vo", "Otro"])
    with col3:
        edad = st.number_input("Edad", min_value=15, max_value=50, step=1)

        # --- Sección 1: Pregunta abierta ---
st.header("✍️ Sección 1: Comentarios adicionales")
q_open = st.text_area(
    "1.¿Organiza su tiempo de estudio para lograr un mejor rendimiento académico? ¿Cómo lo organizas? (Máx. 350 caracteres)",
    max_chars=350
)


# --- Sección 2: Preguntas de escala 1-5 ---
st.header("📈 Sección 2: Evaluación general")
st.markdown("Califica del 1 (menor) al 5 (mayor)")

q2 = st.slider(
    "2. ¿Cuál es su nivel de satisfacción con sus habilidades para planificar y organizar su tiempo de estudio?",
    1, 5, 3,
    help="1: Muy insatisfecho, 5: Muy satisfecho"
)

q3 = st.slider(
    "3. ¿En qué medida considera que las técnicas de estudio que utiliza le ayudan a comprender y retener la información de manera efectiva?",
    1, 5, 3,
    help="1: Muy poco, 5: Demasiado"
)

q4 = st.slider(
    "4. ¿Qué tan útiles son las herramientas digitales (apps, plataformas) para su aprendizaje?",
    1, 5, 3,
    help="1: Nada útiles, 5: Muy útiles"
)

q5 = st.slider(
    "5. ¿Qué tan efectiva es la técnica de toma de apuntes clave en sus estudios universitarios?   ",
    1, 5, 3,
    help="1: Poco efectiva, 5: Muy efectiva"
)

q6 = st.slider(
    "6. ¿Con qué frecuencia participa en grupos de estudio para reforzar tus conocimientos universitarios?",
    1, 5, 3,
    help="1: Nunca, 5: Siempre"
)

q7 = st.slider(
    "7. ¿Cuál es la importancia de las habilidades de comunicación para tu desempeño académico?",
    1, 5, 3,
    help="1: Nada importante, 5: Muy importante"
)

q8 = st.slider(
    "8. ¿Qué tan efectiva considera la habilidad de repetición espaciada en su proceso de estudio?",
    1, 5, 3,
    help="1: Poco efectiva, 5: Muy efectiva"
)

# --- Sección 3: Preguntas de opción múltiple ---
st.header("📋 Sección 3: Hábitos de estudio")
st.markdown("Seleccione la opción que más se adecue a su caso. (En caso de ser otra especifique).")

q9 = st.radio(
    "9. ¿Cuántas horas aproximadamente dedica a estudiar diariamente?",
    ["Menos de 2 horas", "2-4 horas", "4-6 horas", "6-8 horas", "Más de 8 horas"]
)

q10 = st.radio(
    "10.  ¿Cúal es la forma en la que prefiere estudiar?",
    ["Individual", "Parejas", "Equipo", "Grupal", "Sin preferencia"]
)

q11 = st.radio(
    "11.  ¿Utiliza regularmente alguna herramienta digital (aplicación, software, plataforma en línea) para organizar o mejorar su estudio?",
    ["Sí", "No"]
)

q12 = st.selectbox(
    "12. ¿Qué habilidad suele utilizar para tomar apuntes durante sus clases?",
    ["Cognitivas (concentración, comprensión)", 
     "Metacognitivas (planificación, autorregulación)",
     "Gestión de tiempo (organización)",
     "Comunicación (explicación oral/escrita)",
     "Otra"]
)

q13 = st.selectbox(
    "13. ¿Qué material de estudio utiliza con mayor frecuencia?",
    ["Libros", "Notas de clase", "Videos educativos", 
     "Mapas conceptuales", "Ninguna de las anteriores"]
)

q14 = st.selectbox(
    "14.¿Qué técnica de estudio utiliza con mayor frecuencia?",
    ["Mapas mentales", "Subrayar información clave", 
     "Autoevaluación", "Casos prácticos", "Ninguna de las anteriores"]
)

q15 = st.selectbox(
    "15. ¿Cuál de las siguientes acciones considera más valiosas para tu aprendizaje en la universidad?",
    ["Pensamiento crítico", "Comunicación", "Reflexión", 
     "Colaboración", "Otra"]
)

q16 = st.selectbox(
    "16.  ¿Recibió orientación académica de su instituto para mejorar sus técnicas y habilidades de estudio?",
    ["Sí", "Sí, pero no suficiente", 
     "No, pero me interesa", 
     "No, y no me interesa",
     "No"]
)

q17 = st.selectbox(
    "17. ¿Cuál de los siguientes factores considera que tiene el mayor impacto negativo en tu rendimiento académico?",
    ["Falta de tiempo", "Dificultad para concentrarse",
     "Métodos ineficaces", "Falta de claridad en explicaciones",
     "Falta de motivación"]
)

# --- Procesamiento de respuestas ---
if st.button("📤 Enviar respuestas"):

    # Validación de datos obligatorios
    if not sexo or not semestre or edad is None:
        st.error("⚠️ Por favor, complete todos los datos demográficos antes de enviar sus respuestas.")
    elif not q_open.strip():
        st.error("⚠️ Por favor, proporciona detalles sobre cómo organizas tu tiempo.")
    else:
        # Continuar con el procesamiento
        st.success("✅ ¡Tus respuestas han sido registradas! A continuación tu análisis personalizado:")

        # Guardar datos en DataFrame
        data = {
            "Sexo": sexo,
            "Semestre": semestre,
            "Edad": edad,
            "Horas_estudio": q9,
            "Preferencia_estudio": q10,
            "Usa_herramientas_digitales": q11,
            "Habilidad_apuntes": q12,
            "Material_estudio": q13,
            "Tecnica_estudio": q14,
            "Accion_valiosa": q15,
            "Orientacion_recibida": q16,
            "Factor_negativo": q17,
            "Satisfaccion_planificacion": q2,
            "Utilidad_tecnicas": q3,
            "Utilidad_herramientas": q4,
            "Efectividad_apuntes": q5,
            "Frecuencia_grupos": q6,
            "Importancia_comunicacion": q7,
            "Efectividad_repeticion": q8,
            "Organizacion_tiempo": q_open
        }

        # --- Generar recomendaciones basadas en respuestas ---
        st.subheader("🔍 Recomendaciones personalizadas según tus puntajes")

        recomendaciones = []  # Almacenar recomendaciones para el archivo CSV

        # Gestión del tiempo (q2: Satisfacción con planificación)
        if q2 <= 2:
            recomendaciones.append("Usa Google Calendar y la técnica Pomodoro para mejorar planificación.")
            st.warning("""⏰ **Planificación Débil:**
            - Usa Google Calendar para organizar tus horarios diarios.
            - Divide tus tareas en metas pequeñas usando la técnica Pomodoro.
            """)
        elif q2 == 3:
            recomendaciones.append("Prioriza tus tareas con la matriz Eisenhower.")
            st.info("""⏰ **Planificación Regular:**
            - Prioriza tus tareas usando la matriz Eisenhower.
            - Revisa semanalmente tu progreso en las metas.""")
        else:
            recomendaciones.append("Mantén tus buenos hábitos organizativos.")
            st.success("""⏰ **Planificación Efectiva:**
            - Excelente organización. Mantén el hábito y explora herramientas avanzadas como Notion.""")

        # Técnicas de estudio (q3: Utilidad de técnicas)
        if q3 <= 2:
            recomendaciones.append("Prueba mapas mentales y la técnica Feynman.")
            st.warning("""📚 **Refuerzo de Técnicas:**
            - Aprende la técnica Feynman para explicar conceptos complejos.
            - Usa mapas mentales para organizar ideas visualmente.""")
        elif q3 == 3:
            recomendaciones.append("Experimenta con autoevaluaciones periódicas.")
            st.info("""📚 **Técnicas Intermedias:**
            - Realiza autoevaluaciones para identificar áreas débiles.
            - Prueba esquematizar tus apuntes con colores.""")
        else:
            recomendaciones.append("Comparte tus estrategias de estudio con compañeros.")
            st.success("""📚 **Técnicas Sólidas:**
            - Estás aplicando buenas técnicas. Comparte tus estrategias con compañeros.""")

        # Herramientas digitales (q4: Utilidad de herramientas)
        if q4 <= 2:
            recomendaciones.append("Explora Notion, Anki y otras herramientas digitales.")
            st.warning("""💻 **Exploración Digital:**
            - Descubre Notion o Trello para organizar proyectos.
            - Usa Anki para repetición espaciada.""")
        elif q4 == 3:
            recomendaciones.append("Aprovecha apps como Forest para mantener el enfoque.")
            st.info("""💻 **Nivel Intermedio:**
            - Aprovecha apps como Forest para mantener el enfoque durante tus sesiones.""")
        else:
            recomendaciones.append("Sigue explorando integraciones avanzadas como Zapier.")
            st.success("""💻 **Optimización Digital:**
            - Estás bien adaptado a las herramientas digitales. Explora integraciones como Zapier.""")

        # Recomendaciones adicionales según dificultad (q17)
        if q17 == "Falta de tiempo":
            recomendaciones.append("Prioriza tus actividades usando la matriz Eisenhower y reduce distracciones.")
            st.error("""🚨 **Gestión del tiempo:**
            - Prioriza tus actividades con la matriz Eisenhower (urgente/importante).
            - Reduce distracciones como redes sociales mientras estudias.""")
        elif q17 == "Dificultad para concentrarse":
            recomendaciones.append("Prueba bloques de trabajo profundo y usa ruido blanco.")
            st.error("""🧠 **Concentración:**
            - Usa ruido blanco (apps como Noisli).
            - Aplica la técnica 'Deep Work': bloques de trabajo profundo sin interrupciones.""")

        # Agregar recomendaciones al DataFrame
        data["Recomendaciones"] = "\n".join(recomendaciones)

        # Crear DataFrame
        df = pd.DataFrame([data])

        # --- Mostrar gráfica optimizada ---
        st.subheader("📊 Gráfica: Evaluación General de Técnicas y Habilidades")
        fig, ax = plt.subplots()
        categories = [
            "Planificación", "Técnicas", "Herramientas", 
            "Apuntes", "Grupos", "Comunicación", "Repetición"
        ]
        values = [q2, q3, q4, q5, q6, q7, q8]

        ax.bar(categories, values, color=['blue', 'green', 'orange', 'purple', 'red', 'cyan', 'magenta'])
        ax.set_ylim(0, 5)
        ax.set_ylabel("Nivel (1-5)")
        ax.set_title("Evaluación General de Técnicas y Habilidades de Estudio")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

        # Guardar gráfica como archivo PNG
        fig.savefig("grafica_tecnicas_habilidades.png")

        # Botón para descargar la gráfica
        with open("grafica_tecnicas_habilidades.png", "rb") as img_file:
            st.download_button(
                label="📥 Descargar gráfica (PNG)",
                data=img_file,
                file_name="grafica_tecnicas_habilidades.png",
                mime="image/png"
            )

        # --- Mostrar respuestas en tabla ---
        st.subheader("📋 Tus respuestas completas")
        st.dataframe(df.T.rename(columns={0: "Respuesta"}))  # Transponer para mejor visualización

        # --- Opción para descargar respuestas ---
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar mis respuestas (CSV)",
            data=csv,
            file_name="mis_respuestas_encuesta.csv",
            mime="text/csv"
        )

st.markdown("---")
st.caption(""" 🔒 Tus respuestas son anónimas y solo se usarán con fines académicos.
Gracias por participar en esta investigación.
""")


