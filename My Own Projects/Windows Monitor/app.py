import streamlit as st
import psutil
import time
import pandas as pd

st.set_page_config(page_title="Monitor de Recursos Docker", layout="wide")

st.title("📊 Monitor de Sistema Local (Via Docker)")

# Sidebar para configurações
st.sidebar.header("Configurações")
refresh_rate = st.sidebar.slider("Taxa de atualização (segundos)", 1, 10, 2)

# Containers de métricas
cpu_metric = st.empty()
mem_metric = st.empty()
chart_data = pd.DataFrame(columns=['CPU', 'Memória'])

st.subheader("Histórico de Uso")
line_chart = st.line_chart(chart_data)

while True:
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    
    with cpu_metric.container():
        st.metric("Uso de CPU", f"{cpu}%")
    with mem_metric.container():
        st.metric("Uso de Memória", f"{mem}%")
        
    # Atualiza o gráfico
    new_data = pd.DataFrame({'CPU': [cpu], 'Memória': [mem]})
    line_chart.add_rows(new_data)
    
    time.sleep(refresh_rate)