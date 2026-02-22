# librerias necesarias para la aplicación
import streamlit as st
from datetime import date
import pandas as pd
# Interfaz de la aplicación
st.set_page_config(page_title="Mi App", page_icon="📊", layout="wide")

st.markdown("""
<style>
/* ===== CORREGIR ALERTAS ===== */

/* SUCCESS */
div[data-testid="stAlert"][data-baseweb="notification"] {
    color: #1e293b !important;
}

/* Texto interno de alertas */
div[data-testid="stAlert"] p {
    color: #1e293b !important;
}
/* ===== FORZAR TEXTO OSCURO EN INPUTS Y LABELS ===== */

/* Labels */
label {
    color: #1e293b !important;
    font-weight: 600;
}

/* Texto dentro de number_input */
input[type="number"] {
    color: white !important;
}

/* Texto dentro de text_input */
input[type="text"] {
    color: white !important;
}

/* Selectbox texto seleccionado */
div[data-baseweb="select"] span {
    color: white !important;
}

/* Opciones desplegables */
ul[role="listbox"] li {
    color: #1e293b !important;
}
/* ===== CONFIGURACIÓN GENERAL ===== */
.stApp {
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    font-family: 'Segoe UI', sans-serif;
    color: #1e293b;
}

/* ===== TITULOS ===== */
h1 {
    font-weight: 800;
    color: #0f172a;
}

h2, h3 {
    font-weight: 700;
    color: #1e293b;
}

/* ===== SIDEBAR CORPORATIVO ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #1e293b);
    padding-top: 20px;
}

/* Texto sidebar */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {
    color: white !important;
}

/* ===== CONTENEDOR PRINCIPAL ===== */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ===== TARJETAS BLANCAS ===== */
div[data-testid="metric-container"],
div[data-testid="stDataFrame"],
div.stAlert {
    background-color: white !important;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
}

/* ===== BOTONES PROFESIONALES ===== */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #1e40af, #1d4ed8);
}

/* ===== INPUTS ===== */
input, textarea, .stSelectbox {
    border-radius: 10px !important;
}

/* ===== EXPANDER ===== */
div[data-testid="stExpander"] {
    background-color: white;
    border-radius: 15px;
    padding: 10px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.04);
}

</style>:

""", unsafe_allow_html=True)

# Home
# inicializar la lista de actividades en session_state
if 'actividades' not in st.session_state:
    st.session_state.actividades = []
    
# Selecciona una pagina
st.sidebar.image("logo.png")
st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página", ["🏠Home","📘 Ejercicio 1", "📘 Ejercicio 2", "📘 Ejercicio 3", "📘 Ejercicio 4"])
st.sidebar.divider()
# Página Home
if pagina == "🏠Home":
    
    st.markdown("""
    <div style="
        background:white;
        padding:50px;
        border-radius:20px;
        box-shadow:0px 10px 30px rgba(0,0,0,0.08);
    ">
        <h1 style="text-align:center; color:#0f172a;">
        Proyecto Python Fundamentals
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📚 Módulos del Proyecto")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📘 Variables y Condicionales")
        st.info("📘 Listas y Diccionarios")

    with col2:
        st.info("📘 Funciones y Programación Funcional")
        st.info("📘 Programación Orientada a Objetos")
        
    st.header(" Bienvenido a la Aplicación")
    st.write("Esta aplicación fue realizada por **Luis Ángel Córdova Palomino**.")
    st.write("El curso es Python Fundamentals impartido por DMC INSTITUTE en el año 2026.")
    st.write("En esta aplicación se presentan ejercicios prácticos relacionados con los fundamentos de Python, incluyendo variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO).")
    st.write("Se desarrolló con las siguientes herramientas: Python, Streamlit y diversas bibliotecas.")
    st.write("Lista de ejercicios:")
    st.markdown("1️⃣ **Ejercicio 1**: Variables y Condicionales.")
    st.markdown("2️⃣ **Ejercicio 2**: Listas y Diccionarios.")
    st.markdown("3️⃣ **Ejercicio 3**: Funciones y Programación Funcional.")
    st.markdown("4️⃣ **Ejercicio 4**: Programación Orientada a Objetos (POO).")
    st.write("Selecciona una opción en el menú desplegable para explorar cada ejercicio.")

# Página Ejercicio 1    
elif pagina == "📘 Ejercicio 1":
        
    st.header("Ejercicio 1: Variables y Condicionales")
    st.header("📊 Sistema de Evaluación de Presupuesto Mensual")
    
    # Inicializar valores por defecto en session_state
    if 'mes_value' not in st.session_state:
        st.session_state.mes_value = "Enero"
    if 'presupuesto_value' not in st.session_state:
        st.session_state.presupuesto_value = 0.0
    if 'gasto_value' not in st.session_state:
        st.session_state.gasto_value = 0.0
    
    # Función para limpiar los datos
    def limpiar_datos():
        st.session_state.mes_value = "Enero"
        st.session_state.presupuesto_value = 0.0
        st.session_state.gasto_value = 0.0
    
    # Lista de meses para el selectbox
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    # Encontrar el índice del mes actual
    mes_index = meses.index(st.session_state.mes_value)
    
    mes = st.selectbox("Selecciona el mes:", meses, index=mes_index)
    presupuesto = st.number_input("Ingrese su presupuesto mensual:", min_value=0.0, value=st.session_state.presupuesto_value)
    gasto = st.number_input("Ingrese su gasto mensual:", min_value=0.0, value=st.session_state.gasto_value)
    
    # Actualizar session_state con los valores actuales
    st.session_state.mes_value = mes
    st.session_state.presupuesto_value = presupuesto
    st.session_state.gasto_value = gasto
    
    # Botones en columnas
    col1, col2 = st.columns(2)
    
    with col1: 
        if st.button("Evaluar presupuesto", type="primary"):
            if gasto > presupuesto:
                st.error("⚠️ Has gastado más de tu presupuesto.")
            elif gasto == presupuesto:
                st.warning("Estás gastando exactamente tu presupuesto.")
            else:
                ahorro = presupuesto - gasto
                st.success(f'✅ Has ahorrado {ahorro:.2f} este mes de {mes}.')
       
        # Mostrar resumen
        with st.expander("📊 Ver resumen del presupuesto"):
            st.write(f"**Mes:** {mes}")
            st.write(f"**Presupuesto:** S/{presupuesto:.2f}")
            st.write(f"**Gasto:** S/{gasto:.2f}")
            st.write(f"**Ahorro:** S/{presupuesto - gasto:.2f}")
            st.write(f"**Resultado:** {'Déficit' if gasto > presupuesto else 'Equilibrio' if gasto == presupuesto else 'Superávit'}")
            
    with col2:
        if st.button("🗑️ Limpiar datos", type="secondary"):
            limpiar_datos()
            st.rerun()
            
# Página Ejercicio 2
elif pagina == "📘 Ejercicio 2":
    st.header("Ejercicio 2: Listas y Diccionarios")
    st.header("📊 Sistema de Registro de Actividades Financieras Personales")
    
    # Formualario de ingreso de actividades
    col1, col2 = st.columns(2)
    
    with col1:
        nombre_actividad = st.text_input("Nombre de la actividad:")
        tipo = st.selectbox("Tipo de actividad:", ["💰 Ingreso", "💸 Gasto", "🏦 Ahorro", "📈 Inversión", "🏠 Vivienda", "🍔 Alimentación", "🚗 Transporte"])
        presupuesto = st.number_input("Presupuesto asignado:", min_value=0.0)
    with col2:
        gasto_real = st.number_input("Gasto real:", min_value=0.0)
        
    if st.button("Registrar actividad", type="primary", use_container_width=True, key="btn_registrar_ej2"):
        nueva_actividad = {
            "Nombre" : nombre_actividad,
            "Tipo" : tipo,
            "Presupuesto" : presupuesto,
            "Gasto Real" : gasto_real
        }
        
        # Agregar la actividad a la lista
        st.session_state.actividades.append(nueva_actividad)
        st.success(f"✅ Actividad {nombre_actividad} agregada con éxito.")

    # Mostrar actividades registradas
    if st.session_state.actividades:
        st.divider()
        st.subheader("📊 Actividades Registradas:")
    
        # Convirtiendo la lista de diccionario en un DataFrame
        df = pd.DataFrame(st.session_state.actividades)
    
        st.dataframe(
            df.style.format({
            "Presupuesto" : "S/{:,.2f}",
            "Gasto Real" : "S/{:,.2f}"
            }),
            use_container_width=True,
            hide_index=True
        )
    
        # Análisis de cumplimiento de presupuesto
        st.divider()
        st.subheader("📈 Estado de Cumplimiento de Presupuesto")
    
        for i, actividad in enumerate(st.session_state.actividades):
            nombre = actividad['Nombre']
            tipo_act = actividad['Tipo']
            presupuesto = actividad['Presupuesto']
            gasto_real = actividad['Gasto Real']
            diferencia = gasto_real - presupuesto
            porcentaje = (gasto_real / presupuesto) * 100 if presupuesto > 0 else 0
        
            # Evaluar estado
            st.write(f"**Actividad {i+1}: {nombre} **")
            st.write(f"- Tipo: {tipo_act}")
    
            col1, col2, col3 = st.columns([2, 1, 2])

            with col1:
                st.write(f"Presupuesto: S/{presupuesto:,.2f}")
                st.write(f"Gasto real: S/{gasto_real:,.2f}")
            
            with col2:
                if gasto_real <= presupuesto:
                    st.markdown("<h3 style='color: green;'>✅ Cumple</h3>", unsafe_allow_html=True)
                else:
                    st.markdown("<h3 style='color: red;'>⚠️ Excede</h3>", unsafe_allow_html=True)
            with col3:
                st.write(f"Diferencia: **S/{diferencia:,.2f}**")
                st.write(f"Porcentaje usado: **{porcentaje:.1f}%**")
        
        # Mensaje detallado según el tipo
            if gasto_real <= presupuesto:
                disponible = presupuesto - gasto_real
                
                if "Ingreso" in tipo_act:
                    st.write(f"📌 Ingreso controlado: S/{disponible:,.2f} por debajo del presupuesto")
                elif "Gasto" in tipo_act:
                    st.write(f"📌 Gasto controlado: S/{disponible:,.2f} por debajo del presupuesto")
                elif "Ahorro" in tipo_act:
                    st.write(f"📌 Ahorro exitoso: S/{disponible:,.2f} adicional guardado")
                elif "Inversión" in tipo_act:
                    st.write(f"📌 Inversión controlada: S/{disponible:,.2f} de margen disponible")
                elif "Vivienda" in tipo_act:
                    st.write(f"📌 Gasto de vivienda controlado: S/{disponible:,.2f} por debajo del presupuesto")
                elif "Alimentación" in tipo_act:
                    st.write(f"📌 Gasto en alimentación controlado: S/{disponible:,.2f} por debajo del presupuesto")
                elif "Transporte" in tipo_act:
                    st.write(f"📌 Gasto en transporte controlado: S/{disponible:,.2f} por debajo del presupuesto")
                else:
                    exceso = gasto_real - presupuesto
                
                    if "Ingreso" in tipo_act:
                        st.write(f"📌 ⚠️ Ingreso excedido: S/{exceso:,.2f} por encima del presupuesto")
                    elif "Gasto" in tipo_act:
                        st.write(f"📌 ⚠️ Gasto excedido: S/{exceso:,.2f} por encima del presupuesto")
                    elif "Ahorro" in tipo_act:
                        st.write(f"📌 ⚠️ Se está utilizando ahorro adicional: S/{exceso:,.2f} extra")
                    elif "Inversión" in tipo_act:
                        st.write(f"📌 ⚠️ Inversión por encima del presupuesto: S/{exceso:,.2f} adicional")
                    elif "Vivienda" in tipo_act:
                        st.write(f"📌 ⚠️ Gasto de vivienda excedido: S/{exceso:,.2f} por encima del presupuesto")
                    elif "Alimentación" in tipo_act:
                        st.write(f"📌 ⚠️ Gasto en alimentación excedido: S/{exceso:,.2f} por encima del presupuesto")
                    elif "Transporte" in tipo_act:
                        st.write(f"📌 ⚠️ Gasto en transporte excedido: S/{exceso:,.2f} por encima del presupuesto")
            
                st.divider()
        
        # Métricas generales
        with st.expander("📊 Resumen General"):
            col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_presupuesto = sum(a['Presupuesto'] for a in st.session_state.actividades)
            st.markdown(f"**Presupuesto Total:** S/{total_presupuesto:,.2f}")
        
        with col2:
            total_gastos = sum(a['Gasto Real'] for a in st.session_state.actividades)
            st.markdown(f"**Gasto Total Real:** S/{total_gastos:,.2f}")
        
        with col3:
            diferencia_total = total_gastos - total_presupuesto
            st.markdown(f"**Diferencia Total:** S/{diferencia_total:,.2f}")
        
        with col4:
            actividades_cumplen = sum(1 for a in st.session_state.actividades if a['Gasto Real'] <= a['Presupuesto'])
            porcentaje_cumplen = (actividades_cumplen / len(st.session_state.actividades)) * 100 if st.session_state.actividades else 0
            st.markdown(f"**Actividades que cumplen:** {actividades_cumplen}/{len(st.session_state.actividades)}")
        
        # Botón para limpiar actividades
        if st.button("🗑️ Limpiar todas las actividades", type="secondary", key="btn_limpiar_ej2"):
            st.session_state.actividades = []
            st.rerun()
    
        else:
        # Mensaje cuando no hay actividades
            st.divider()
            st.info("ℹ️ No hay actividades registradas. Agrega una actividad usando el formulario superior.")

# Página Ejercicio 3
elif pagina == "📘 Ejercicio 3":
    st.header("Ejercicio 3: Funciones y Programación Funcional")
    st.header("📊 Sistema de Retorno por Actividad")
    
    # Guardar actividades
    if 'lista_actividades' not in st.session_state:
        st.session_state.lista_actividades = []
    
    # Función de cálculo
    def calcular_retorno(presupuesto, tasa, meses):
        return presupuesto * tasa * meses
    
    # Ingresar actividad 
    with st.container():
        st.write("### Ingresar nueva actividad")
        
        nombre = st.text_input("Nombre de la actividad:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            presupuesto = st.number_input("Presupuesto (S/):", min_value=0.0, value=10000.0, step=1000.0)
        with col2:
            tasa = st.number_input("Tasa (%):", min_value=0.0, max_value=100.0, value=5.0, step=0.5) / 100
        with col3:
            meses = st.number_input("Meses:", min_value=1, max_value=60, value=12, step=1)
        
        if st.button("➕ Agregar actividad"):
            if nombre:
                st.session_state.lista_actividades.append({
                    "nombre": nombre,
                    "presupuesto": presupuesto,
                    "tasa": tasa,
                    "meses": meses
                })
                st.success(f"Actividad '{nombre}' agregada")
                st.rerun()
                
    # convertir a DataFrame para mostrar
    if st.session_state.lista_actividades:
        st.write("### Registro de Actividades")
        df = pd.DataFrame(st.session_state.lista_actividades)
        df["retorno"] = df.apply(
            lambda row: calcular_retorno(row["presupuesto"], row["tasa"], row["meses"]), axis=1)
        st.dataframe(df)
        
        # 🔴 ELIMINAR ACTIVIDAD
        st.write("### 🗑️ Eliminar actividad")
        
        nombres = df["nombre"].tolist()
        
        actividad_eliminar = st.selectbox(
            "Selecciona la actividad que deseas eliminar:",
            nombres
        )
        
        if st.button("Eliminar actividad", type="secondary"):
            st.session_state.lista_actividades = [
                act for act in st.session_state.lista_actividades
                if act["nombre"] != actividad_eliminar
            ]
            st.success("Actividad eliminada correctamente")
            st.rerun()
        # Botón para calcular el retorno
        if st.button("📊 Calcular retorno", type="primary"):
            st.write("### Resultados del cálculo")
            
            # Procesar cada actividad usando map y lambda
            resultados = list(map(
                lambda act: {
                    "nombre": act["nombre"],
                    "presupuesto": act["presupuesto"],
                    "retorno": calcular_retorno(act["presupuesto"], act["tasa"], act["meses"])
                },
                st.session_state.lista_actividades
            ))
            
            # Mostrar resultados
            for r in resultados:
                st.write(f"**{r['nombre']}**: S/{r['presupuesto']:,.0f} → **S/{r['retorno']:,.0f}**")
            
            # Totales
            total_inversion = sum(map(lambda x: x["presupuesto"], resultados))
            total_retorno = sum(map(lambda x: x["retorno"], resultados))
            
            st.write(f"**Total invertido:** S/{total_inversion:,.0f}")
            st.write(f"**Retorno total:** S/{total_retorno:,.0f}")
            st.write(f"**Ganancia:** S/{total_retorno - total_inversion:,.0f}")
    
    else:
        st.info("👆 Agrega una actividad para comenzar")

# Página Ejercicio 4        
elif pagina == "📘 Ejercicio 4":
    st.header("Ejercicio 4: Programación Orientada a Objetos (POO)")
    st.header("Sistema de Actividad Financiera")
    
    #creando una clase
    class Actividad:
        def __init__ (self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real
        
        # metodos    
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto
        def mostrar_info(self):
            estado = "✅ Está en el presupuesto" if self.esta_en_presupuesto() else "❌ No está en el presupuesto"
            return f"""
            **{estado} {self.nombre}**  
            📌 Tipo: {self.tipo}  
            💰 Presupuesto: S/{self.presupuesto:,.2f}  
            💸 Gasto Real: S/{self.gasto_real:,.2f}  
            📊 Diferencia: S/{self.presupuesto - self.gasto_real:,.2f}
            """
    
    # Estado
    if 'objetos_actividad' not in st.session_state:
        st.session_state.objetos_actividad = []
    
    # Formulario
    with st.form("form_poo"):
        nombre = st.text_input("Nombre:")
        tipo = st.selectbox("Tipo:", ["💰 Ingreso", "💸 Gasto", "🏦 Ahorro", "📈 Inversión", "🏠 Vivienda", "🍔 Alimentación", "🚗 Transporte"])
        
        col1, col2 = st.columns(2)
        presupuesto = col1.number_input("Presupuesto S/", 0.0, 100000.0)
        gasto = col2.number_input("Gasto Real S/", 0.0, 100000.0)
        
        if st.form_submit_button("🧮 Calcular Actividad") and nombre:
            # Convertir a objeto
            st.session_state.objetos_actividad.append(Actividad(nombre, tipo, presupuesto, gasto))
            st.rerun()
    
    # Mostrar resumen
    if st.session_state.objetos_actividad:
        st.write("### 📋 Resumen de la Actividad")
        
        for i, obj in enumerate(st.session_state.objetos_actividad):
            col1, col2, col3 = st.columns([3, 1, 0.5])
            
            # Usar método mostrar_info()
            col1.write(obj.mostrar_info())
            
            # Usar método esta_en_presupuesto() con st.success/st.warning
            if obj.esta_en_presupuesto():
                col2.success("✅ En presupuesto")
            else:
                diferencia = obj.gasto_real - obj.presupuesto
                col2.warning(f"⚠️ Fuera del presupuesto en S/{diferencia:.0f}")
            
            if col3.button("❌", key=f"del_obj_{i}"):
                st.session_state.objetos_actividad.pop(i)
                st.rerun()
        
        