import streamlit as st
import pandas as pd
import os

st.title("🔐 Cadastro - Os Sparnauê")

senha = st.text_input("Digite a senha de acesso:", type="password")
senha_correta = "sparnaue123"

if senha == senha_correta:
    st.success("Acesso liberado! Faça seus cadastros abaixo 👇")

    # --- Arquivos ---
    arq_participantes = "participantes.csv"
    arq_itens = "itens.csv"

    if os.path.exists(arq_participantes):
        participantes = pd.read_csv(arq_participantes)
    else:
        participantes = pd.DataFrame(columns=["Nome", "Tipo", "Valor Pago"])

    if os.path.exists(arq_itens):
        itens = pd.read_csv(arq_itens)
    else:
        itens = pd.DataFrame(columns=["Nome", "Unidade", "Quantidade", "Categoria", "Preço"])


    # --- Cadastro de Participantes ---
    with st.expander("👥 Cadastrar Participantes", expanded=True):
        with st.form("form_participantes", clear_on_submit=True):
            nome = st.text_input("Nome")
            tipo = st.selectbox("Tipo", ["Solteiro", "Casal"])
            valor = 125 if tipo == "Solteiro" else 175
            enviar_part = st.form_submit_button("💾 Adicionar Participante")

            if enviar_part and nome:
                novo = pd.DataFrame([[nome, tipo, valor]], columns=participantes.columns)
                participantes = pd.concat([participantes, novo], ignore_index=True)
                participantes.to_csv(arq_participantes, index=False)
                st.success(f"{nome} adicionado com sucesso!")

        st.dataframe(participantes, use_container_width=True)
        total = participantes["Valor Pago"].sum()
        st.metric("💰 Total arrecadado", f"R$ {total:.2f}")

    st.divider()

    # --- Cadastro de Itens ---
    with st.expander("🛒 Cadastrar Itens", expanded=True):
        with st.form("form_itens", clear_on_submit=True):
            nome_produto = st.text_input("Nome do Produto")
            unidade_produto = st.selectbox("Unidades", ["Grama", "Litros", "Unidades", "Kg", "Latas","Dias"])
            quantidade_produto = st.number_input("Quantidade", min_value=0.0)
            categoria_produto = st.selectbox("Categoria", [
                "Carne", "Cachaça", "Refrigerante", "Cerveja", "Carvão", "Sal", "Cigarro", "Alucinogenos", "Utensilios","Sitio"
            ])
            preco_produto = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")
            salvar = st.form_submit_button("💾 Adicionar Item")

            if salvar and nome_produto:
                novo_item = pd.DataFrame(
                    [[nome_produto, unidade_produto, quantidade_produto, categoria_produto, preco_produto]],
                    columns=itens.columns
                )
                itens = pd.concat([itens, novo_item], ignore_index=True)
                itens.to_csv(arq_itens, index=False)
                st.success(f"{nome_produto} adicionado com sucesso!")

        st.dataframe(itens, use_container_width=True)
        total_gasto = itens["Preço"].sum()
        st.metric("💸 Total gasto", f"R$ {total_gasto:.2f}")

else:
    st.warning("Digite a senha correta para acessar os cadastros.")
