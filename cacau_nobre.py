
import streamlit as st

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Cacau Nobre | Brownies Artesanais",
    page_icon="🍫",
    layout="wide"
)

# -------------------- Simple styling --------------------
PRIMARY = "#5a3c2e"  # cocoa
ACCENT = "#d6a77a"   # caramel
BG_SOFT = "#fff8f3"  # soft cream

st.markdown(
    f"""
    <style>
    .main {{background:{BG_SOFT};}}
    .hero {{
        background: linear-gradient(135deg, {BG_SOFT} 0%, #ffffff 100%);
        border: 1px solid #eee; padding: 2.2rem; border-radius: 18px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
    }}
    .title {{ font-size: 2.2rem; font-weight: 800; color: {PRIMARY}; line-height: 1.15; }}
    .subtitle {{ font-size: 1.05rem; color: #573c2a; }}
    .badge {{
        display:inline-block; padding:.35rem .7rem; border-radius:999px;
        background:{ACCENT}; color:#3a2a20; font-weight:700; font-size:.85rem; margin-right:.3rem;
    }}
    .card {{
        background:white; border:1px solid #eee; border-radius:16px; padding:1.1rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.05);
        height:100%;
    }}
    .metric {{font-size: 1.6rem; font-weight: 800; color:{PRIMARY};}}
    .section-title {{font-size:1.6rem; font-weight:800; color:{PRIMARY}; margin-top: .5rem;}}
    .pill {{background:#faf4ef; color:{PRIMARY}; padding:.45rem .8rem; border-radius:999px; border:1px solid #eadfd7; font-size:.9rem; margin:.15rem; display:inline-block;}}
    .footnote {{font-size:.9rem; color:#6b615b;}}
    a, a:visited {{ color: {PRIMARY}; }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- Sidebar --------------------
with st.sidebar:
    st.image("https://placehold.co/420x180/5a3c2e/ffffff?text=Cacau+Nobre", use_container_width=True)
    st.markdown("### Navegação")
    st.markdown("[🏠 Home](#apresentacao)")
    st.markdown("[🍫 Nossos Brownies](#produtos)")
    st.markdown("[🌱 Sustentabilidade](#sustentabilidade)")
    st.markdown("[💛 Impacto Social](#impacto-social)")
    st.markdown("[📖 Nossa Origem](#origem)")
    st.markdown("[📞 Fale Conosco](#contato)")
    st.divider()
    st.caption("© 2025 Cacau Nobre — Brownies Artesanais de Goiânia-GO")

# -------------------- Hero --------------------
st.markdown('<div class="hero" id="apresentacao">', unsafe_allow_html=True)
c1, c2 = st.columns([1.4, 1])
with c1:
    st.markdown('<div class="title">Cacau Nobre</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Brownies artesanais, com ingredientes selecionados e um sabor inesquecível — '
        'pensados para encantar pessoas e negócios.</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <span class="badge">🍫 Artesanal</span>
        <span class="badge">🌱 Embalagens recicláveis</span>
        <span class="badge">💛 Doação para caridade</span>
        """,
        unsafe_allow_html=True
    )
    st.write("")
    st.write("Oferecemos brownies de alta qualidade, preparados com cuidado, processos controlados e seleção rigorosa de insumos.")
with c2:
    st.image("https://placehold.co/600x420/dbc2a4/3a2a20?text=Brownies+Artesanais", caption="Sabor e propósito em cada pedaço.", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# -------------------- Quick metrics --------------------
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('<div class="card"><div class="metric">120</div><div>Unidades por lote artesanal</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="card"><div class="metric">100%</div><div>Embalagens recicláveis e de baixo impacto</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="card"><div class="metric">5%</div><div>Do faturamento doado para caridade*</div></div>', unsafe_allow_html=True)

st.caption("* Percentual ajustável conforme campanhas sociais vigentes.")

st.write("")

# -------------------- Produtos --------------------
st.markdown('<div class="section-title" id="produtos">🍫 Nosso Brownie</div>', unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)
with p1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Clássico Intenso")
    st.write("Cacau nobre, textura úmida e casquinha crocante. Ideal para quem ama o sabor tradicional.")
    st.markdown('<span class="pill">70% cacau</span> <span class="pill">Sem corantes</span> <span class="pill">Artesanal</span>', unsafe_allow_html=True)
    st.image("https://placehold.co/480x320/5a3c2e/ffffff?text=Classico+Intenso", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


st.write("")

# -------------------- Sustentabilidade --------------------
st.markdown('<div class="section-title" id="sustentabilidade">🌱 Sustentabilidade</div>', unsafe_allow_html=True)
s1, s2 = st.columns([1, 1])
with s1:
    st.markdown(
        """
        <div class="card">
        <h4>Embalagens que respeitam o meio ambiente</h4>
        <p>Usamos embalagens <strong>recicláveis</strong> e de <strong>baixo impacto ambiental</strong>. Além de proteger nossos brownies,
        elas demonstram nosso compromisso com responsabilidade socioambiental.</p>
        <ul>
            <li>Papel e papelão de fontes responsáveis;</li>
            <li>Plásticos recicláveis quando necessários;</li>
            <li>Design otimizado para reduzir desperdícios.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
with s2:
    st.markdown(
        """
        <div class="card">
        <h4>Sabor com propósito</h4>
        <p>Uma parte do nosso faturamento é doada para <strong>iniciativas de caridade</strong>. A cada compra, você ajuda a
        ampliar o impacto positivo em nossa comunidade.</p>
        <ul>
            <li>Transparência em campanhas e metas;</li>
            <li>Parcerias locais e prestação de contas;</li>
            <li>Foco em alimentação, educação e dignidade.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# -------------------- Origem --------------------
st.markdown('<div class="section-title" id="origem">📖 Nossa Origem</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
    <p>A <strong>Cacau Nobre</strong> nasceu durante um seminário do <strong>Empretec</strong>, na cidade de <strong>Goiânia (GO)</strong>.
    Em um ambiente de desafios práticos, espírito empreendedor e foco em execução, transformamos a paixão por
    confeitaria artesanal em um negócio com propósito claro: unir <strong>excelência em sabor</strong> com <strong>responsabilidade socioambiental</strong>.</p>
    <p>Desde os primeiros testes de receita até as primeiras vendas, aprendemos a ouvir o cliente,
    melhorar processos e construir uma marca que entrega <strong>experiências memoráveis</strong>.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- Impacto Social --------------------
st.markdown('<div class="section-title" id="impacto-social">💛 Impacto Social</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
    <p>Nossa meta é destinar parte do faturamento para projetos sociais que geram efeito multiplicador na comunidade.
    Priorizamos iniciativas de alimentação, educação e dignidade. Divulgamos resultados e parceiros periodicamente.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- Como Comprar / Canais --------------------
st.markdown('<div class="section-title">🛒 Como comprar</div>', unsafe_allow_html=True)
ch1, ch2, ch3 = st.columns(3)
with ch1:
    st.markdown('<div class="card"><h4>Pedidos Diretos</h4><p>Atendimento via WhatsApp e Instagram.</p><p class="footnote">Defina horários, mínimos e prazos de entrega.</p></div>', unsafe_allow_html=True)
with ch2:
    st.markdown('<div class="card"><h4>Eventos & Parcerias</h4><p>Personalização de kits para eventos, coffee breaks e lembranças.</p><p class="footnote">Embale sua marca com a nossa qualidade.</p></div>', unsafe_allow_html=True)
with ch3:
    st.markdown('<div class="card"><h4>Revendas</h4><p>Condições especiais para cafeterias e empórios.</p><p class="footnote">Cresça com a gente.</p></div>', unsafe_allow_html=True)

st.write("")

# -------------------- FAQ --------------------
st.markdown('<div class="section-title">❓ Perguntas Frequentes</div>', unsafe_allow_html=True)
with st.expander("As embalagens são realmente recicláveis?"):
    st.write("Sim. Priorizamos papel/papelão e plásticos com identificação para reciclagem. Evitamos misturas que dificultem o processo.")
with st.expander("Vocês entregam em Goiânia?"):
    st.write("Sim. Consulte taxas e disponibilidade por bairro. Também trabalhamos com retirada agendada.")
with st.expander("Qual é o percentual doado?"):
    st.write("Trabalhamos com uma meta sugerida de 5% do faturamento, ajustável conforme campanhas e períodos.")

# -------------------- Contato --------------------
st.markdown('<div class="section-title" id="contato">📞 Fale Conosco</div>', unsafe_allow_html=True)
with st.form("contato_form"):
    colA, colB = st.columns(2)
    with colA:
        nome = st.text_input("Seu nome")
        email = st.text_input("Seu e-mail")
    with colB:
        assunto = st.text_input("Assunto")
        telefone = st.text_input("Telefone / WhatsApp")
    mensagem = st.text_area("Mensagem", height=150, placeholder="Conte como podemos ajudar.")

    enviar = st.form_submit_button("Enviar mensagem")
    if enviar:
        if nome and (email or telefone) and mensagem:
            st.success("Obrigado! Recebemos sua mensagem. Responderemos em breve.")
        else:
            st.error("Por favor, preencha ao menos: nome, um contato (e-mail/telefone) e a mensagem.")

st.write("")
st.caption("Cacau Nobre • Brownies artesanais feitos com carinho e responsabilidade.")

