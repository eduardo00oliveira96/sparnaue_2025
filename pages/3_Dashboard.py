import streamlit as st
import pandas as pd
import os

st.title("📊 Dashboard - Os Sparnauê")

arq_participantes = "participantes.csv"
arq_itens = "itens.csv"

participantes = pd.read_csv(arq_participantes) if os.path.exists(arq_participantes) else pd.DataFrame(columns=["Nome", "Tipo", "Valor Pago"])
itens = pd.read_csv(arq_itens) if os.path.exists(arq_itens) else pd.DataFrame(columns=["Nome", "Unidade", "Quantidade", "Categoria", "Preço"])

if not participantes.empty or not itens.empty:
    col1, col2, col3 = st.columns(3)

    with col1:
        total_arrecadado = participantes["Valor Pago"].sum()
        st.metric("💰 Total Arrecadado", f"R$ {total_arrecadado:.2f}")

    with col2:
        total_gasto = itens["Preço"].sum()
        st.metric("💸 Total Gasto", f"R$ {total_gasto:.2f}")
        
    with col3:
        restante =  total_arrecadado - total_gasto
        st.metric("💡 Restante", f"R$ {restante:.2f}")
        
        

    saldo = total_arrecadado - total_gasto
    if saldo > 0:
        st.success(f"✅ Sobrou R$ {saldo:.2f}")
    elif saldo < 0:
        st.error(f"🚨 Faltou R$ {-saldo:.2f}")
    else:
        st.info("💡 Tudo fechado certinho!")

    st.divider()

    st.subheader("👥 Participantes")
    st.dataframe(participantes, use_container_width=True)

    st.subheader("🛒 Itens Comprados")
    st.dataframe(itens, use_container_width=True)

    st.divider()

    # --- Resumo simples por categoria ---
    if not itens.empty:
        st.subheader("📦 Total por Categoria")
        resumo = itens.groupby("Categoria")["Preço"].sum().reset_index()
        for _, row in resumo.iterrows():
            st.write(f"**{row['Categoria']}** → R$ {row['Preço']:.2f}")

else:
    st.warning("Nenhum dado encontrado. Cadastre participantes e itens primeiro.")


st.subheader("Notas fiscais")
media_files = [
    {"type": "image", "file": "assets/nota-1.jpeg"},
    {"type": "image", "file": "assets/nota-2.jpeg"},
]

# Slider para escolher mídia
idx = st.slider("Navegue pelas notas:", 0, len(media_files)-1, 0)

current_media = media_files[idx]

if current_media["type"] == "image":
    st.image(current_media["file"], caption=f"Momento {idx+1}", use_container_width=True)
elif current_media["type"] == "video":
    st.video(current_media["file"])