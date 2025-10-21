import streamlit as st

st.set_page_config(page_title="Amigo Digital - Chat Educativo", page_icon="🤖")
st.title("🤖 Amigo Digital")
st.write("Olá! Eu posso conversar sobre **Bullying, Cyberbullying e Segurança de Dados**. Escolha um tópico abaixo:")

# Inicializa o histórico de mensagens
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if "etapa" not in st.session_state:
    st.session_state.etapa = "inicio"  # controla em qual etapa do fluxo o usuário está

def adicionar_mensagem(msg):
    st.session_state.mensagens.append(msg)

# Mostra o histórico
for msg in st.session_state.mensagens:
    st.write(msg)

# Função para resetar fluxo
def resetar():
    st.session_state.etapa = "inicio"
    st.rerun()

# Fluxo principal
if st.session_state.etapa == "inicio":
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Bullying"):
            adicionar_mensagem("👤 Você escolheu: Bullying")
            adicionar_mensagem("🤖 Bullying é qualquer comportamento agressivo ou intimidador praticado repetidamente contra alguém.")
            st.session_state.etapa = "bullying"
            st.rerun()
    with col2:
        if st.button("Cyberbullying"):
            adicionar_mensagem("👤 Você escolheu: Cyberbullying")
            adicionar_mensagem("🤖 Cyberbullying é quando alguém usa a internet ou redes sociais para ofender, ameaçar ou humilhar outra pessoa.")
            st.session_state.etapa = "cyberbullying"
            st.rerun()
    with col3:
        if st.button("Segurança de Dados"):
            adicionar_mensagem("👤 Você escolheu: Segurança de Dados")
            adicionar_mensagem("🤖 Segurança de dados envolve proteger suas informações pessoais online, como senhas, fotos e dados bancários. Use senhas fortes e nunca compartilhe suas informações com estranhos.")
            st.session_state.etapa = "seguranca"
            st.rerun()

# Etapa Bullying – pergunta se está sofrendo bullying
elif st.session_state.etapa == "bullying":
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sim, estou sofrendo bullying"):
            adicionar_mensagem("👤 Sim, estou sofrendo bullying")
            adicionar_mensagem("🤖 Sinto muito que esteja passando por isso. Procure alguém de confiança, como um professor, familiar ou psicólogo, e nunca se sinta sozinho.")
            st.session_state.etapa = "final"
            st.rerun()
    with col2:
        if st.button("Não, só quero aprender mais"):
            adicionar_mensagem("👤 Não, só quero aprender mais")
            adicionar_mensagem("🤖 Ótimo! Saber sobre bullying ajuda a reconhecer e prevenir. Lembre-se de sempre praticar empatia e respeito com os outros.")
            st.session_state.etapa = "final"
            st.rerun()

# Etapa Cyberbullying – opção extra
elif st.session_state.etapa == "cyberbullying":
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Já presenciei cyberbullying"):
            adicionar_mensagem("👤 Já presenciei cyberbullying")
            adicionar_mensagem("🤖 Se você presenciou cyberbullying, nunca compartilhe conteúdos que possam prejudicar alguém e reporte comportamentos abusivos.")
            st.session_state.etapa = "final"
            st.rerun()
    with col2:
        if st.button("Quero apenas aprender"):
            adicionar_mensagem("👤 Quero apenas aprender")
            adicionar_mensagem("🤖 Saber sobre cyberbullying ajuda a se proteger e ajudar outros. Sempre mantenha sua privacidade e respeite os outros online.")
            st.session_state.etapa = "final"
            st.rerun()

# Etapa Segurança de Dados – opção extra
elif st.session_state.etapa == "seguranca":
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Quero dicas práticas"):
            adicionar_mensagem("👤 Quero dicas práticas")
            adicionar_mensagem("🤖 Use senhas fortes, ative autenticação em dois fatores e nunca compartilhe suas informações pessoais com estranhos.")
            st.session_state.etapa = "final"
            st.rerun()
    with col2:
        if st.button("Só quero aprender mais"):
            adicionar_mensagem("👤 Só quero aprender mais")
            adicionar_mensagem("🤖 É importante conhecer conceitos básicos de segurança digital para proteger suas informações e a de outros online.")
            st.session_state.etapa = "final"
            st.rerun()

# Etapa final – opção de reiniciar
elif st.session_state.etapa == "final":
    st.write("---")
    st.write("Deseja escolher outro tópico ou reiniciar a conversa?")
    if st.button("Reiniciar conversa"):
        resetar()
