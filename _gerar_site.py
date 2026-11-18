# -*- coding: utf-8 -*-
"""
Gera o site das Casas em Pipa (HTML estático + sitemap.xml + robots.txt).

Como usar: edite os dados abaixo e rode:
    python _gerar_site.py
Os arquivos .html são recriados nesta mesma pasta. Ao final, o script lista
os dados que ainda faltam (bloco PENDENTE).
"""
import json, html, datetime, os
from urllib.parse import quote

AQUI = os.path.dirname(os.path.abspath(__file__))

# ====== CONFIGURAÇÃO GERAL ======
DOMINIO   = "https://clau219.github.io/casas-pipa"   # troque por "https://www.casafridapipa.com.br" quando o domínio estiver registrado e ligado
MARCA     = "Casas em Pipa"
WHATSAPP  = "5584996011991"                    # só números, com 55 + DDD
TELEFONE  = "+55 84 99601-1991"
EMAIL     = os.environ.get("SITE_EMAIL", "")   # opcional: defina SITE_EMAIL para mostrar um e-mail no site
INSTAGRAM = "casafridapipa"
ANFITRIAO = "Claudio Roberto"
ENDERECO  = {"rua": "Condomínio Pipa Natureza, Quinta do Sol", "cidade": "Tibau do Sul",
             "uf": "RN", "cep": "59178-000", "pais": "BR", "bairro": "Praia da Pipa"}
GEO       = (-6.229008, -35.072477)            # do link de mapa do cartão de boas-vindas
CHECKIN, CHECKOUT = "14:00", "11:00"
MIN_NOITES = 2                                 # mesma regra configurada no Stays
NOTAS_DATA = "nov/2026"                        # quando as notas do Airbnb abaixo foram conferidas
HOJE = datetime.date.today().isoformat()

# ====== PENDENTE — preencha quando tiver a informação ======
# Enquanto estiver vazio, o item NÃO aparece no site (nada é inventado).
PENDENTE = {
    "formas_pagamento": "Pagamento por Pix, transferência ou cartão de crédito. Para confirmar a reserva, paga-se um sinal de 50%; o restante, até 7 dias antes da entrada.",
    "politica_cancelamento": "Cancelamento até 30 dias antes da entrada: reembolso integral. Entre 30 e 7 dias antes: reembolso de 50% do valor pago. A menos de 7 dias da entrada: sem reembolso.",
    "animais": "Animais de estimação são bem-vindos, com taxa (a mesma praticada no Airbnb) informada na consulta. Avise ao reservar.",   # >>> valor da taxa: informar quando souber
    "taxa_limpeza": "Sem taxa de limpeza na reserva direta.",
    "criancas_berco": "Crianças são bem-vindas. As casas não têm berço.",
    "eventos_festas": "Não são permitidos eventos ou festas.",
}

# ====== AS CASAS ======
CASAS = [
  {
    "slug": "casa-terracota", "nome": "Casa Terracota", "numero": "50", "cor": "terracota",
    "titulo_seo": "Casa Terracota – casa com piscina para 7 pessoas na Praia da Pipa",
    "descricao_seo": "Casa de temporada com piscina, 3 suítes com ar-condicionado e varanda gourmet no Condomínio Pipa Natureza, Praia da Pipa (RN). Até 7 hóspedes. Reserve direto pelo WhatsApp.",
    "resumo": "Arquitetura moderna com cobogós terracota, piscina privativa e varanda gourmet integrada à sala e à cozinha.",
    "ideal": "Famílias e grupos de amigos que gostam de cozinhar e reunir todo mundo à mesa.",
    "hospedes": 7, "quartos": 3, "suites": 3, "banheiros": "3,5",
    "camas": "1 cama de casal e 5 de solteiro",
    "quartos_detalhe": [],        # >>> PREENCHER: camas de cada quarto, ex.: [("Suíte", "1 cama de casal · ar-condicionado"), ...]
    "piscina": True,
    "nota": "4,9", "airbnb": "https://www.airbnb.com.br/rooms/28283599",
    "hero": "terracota-varanda-gourmet", "card": "terracota-jardim",
    "comodidades": ["Piscina privativa", "Varanda gourmet com mesa para 8", "Ar-condicionado nos quartos",
                     "Cozinha completa com bancada", "Wi-Fi", "Smart TV", "Jardim gramado",
                     "Vaga para 1 carro", "Roupa de cama e banho"],
    "bom_saber": ["A piscina é limpa às segundas, quartas e sextas."],
    "texto": [
      "A Casa Terracota é uma casa de temporada em Pipa pensada para famílias e grupos de amigos que querem espaço, privacidade e conforto a poucos minutos das praias mais bonitas do litoral potiguar.",
      "A sala, a cozinha e a varanda gourmet formam um único ambiente aberto para a piscina, com pé-direito alto e muita luz natural. São 3 suítes com ar-condicionado, cada uma com seu banheiro, e 3,5 banheiros no total, acomodando até 7 pessoas.",
      "Fica no Condomínio Pipa Natureza, em meio à mata atlântica, com trilha de cerca de 20 minutos até a Praia do Madeiro, famosa pelos golfinhos e pelo mar calmo.",
    ],
    "fotos": [("terracota-varanda-gourmet", "Varanda gourmet com mesa de jantar ao lado da piscina da Casa Terracota"),
              ("terracota-piscina", "Piscina e varanda gourmet da Casa Terracota em Pipa"),
              ("terracota-fachada", "Fachada com cobogós terracota no Condomínio Pipa Natureza"),
              ("terracota-piscina-cobogo", "Piscina, gramado e cobogó terracota"),
              ("terracota-sala-cozinha", "Sala integrada à cozinha, aberta para o jardim"),
              ("terracota-cozinha", "Cozinha completa com bancada vermelha"),
              ("terracota-sala-integrada", "Ambiente integrado de sala, cozinha e varanda"),
              ("terracota-sala", "Sala de estar com sofás e TV"),
              ("terracota-quarto-casal", "Quarto de casal com ar-condicionado"),
              ("terracota-quarto-solteiro", "Quarto com camas de solteiro e ar-condicionado"),
              ("terracota-quarto-solteiro-2", "Outro quarto com camas de solteiro"),
              ("terracota-banheiro", "Banheiro com parede terracota"),
              ("terracota-entrada", "Entrada da casa"),
              ("terracota-cobogo", "Corredor de entrada com cobogós terracota"),
              ("terracota-jardim", "Cobogó terracota e jardim ao pôr do sol"),
              ("terracota-caminho", "Caminho do jardim até o portão")],
  },
  {
    "slug": "casa-frida", "nome": "Casa Frida", "numero": "39", "cor": "frida",
    "titulo_seo": "Casa Frida – casa de temporada com piscina e churrasqueira em Pipa",
    "descricao_seo": "Casa Frida: 3 suítes (uma com cama king), piscina, churrasqueira e adega no Condomínio Pipa Natureza, Praia da Pipa (RN). Até 8 hóspedes. Reserve pelo WhatsApp.",
    "resumo": "Casa moderna e colorida, com piscina, deck com espreguiçadeiras, churrasqueira e suíte com cama king.",
    "ideal": "Grupos de até 8 pessoas que querem área externa ampla, churrasco e piscina.",
    "hospedes": 8, "quartos": 3, "suites": 3, "banheiros": "3,5",
    "camas": "1 cama king, 1 queen e 4 de solteiro",
    "quartos_detalhe": [("Suíte 1", "1 cama king · banheiro privativo · ar-condicionado · ventilador de teto · TV"),
                        ("Suíte 2", "1 cama queen e 1 de solteiro · banheiro privativo · ar-condicionado · ventilador de teto · TV com Chromecast"),
                        ("Suíte 3", "3 camas de solteiro · banheiro privativo · ar-condicionado")],
    "piscina": True,
    "nota": "4,73", "airbnb": "https://www.airbnb.com.br/rooms/45895549",
    "hero": "frida-piscina", "card": "frida-fachada",
    "comodidades": ["Duas piscinas", "Churrasqueira de inox na varanda", "Mesa de jantar para 6",
                     "Suíte com cama king", "Ar-condicionado e ventilador de teto", "TV 50\" e Chromecast",
                     "Adega de vinhos", "Air fryer, cafeteira e forno elétrico", "Wi-Fi",
                     "Vaga para 1 carro", "Roupa de cama e banho"],
    "bom_saber": [],
    "texto": [
      "A Casa Frida é uma hospedagem em Pipa com personalidade: cores, arte e uma área externa feita para aproveitar o clima do Rio Grande do Norte o ano inteiro.",
      "São 3 suítes — uma com cama king, uma com cama queen e uma com camas de solteiro — e 3,5 banheiros, para até 8 hóspedes. A varanda tem churrasqueira de inox e mesa redonda para 6, de frente para a piscina.",
      "A cozinha é completa (cooktop, forno elétrico, micro-ondas, air fryer, cafeteira, adega) e a sala tem TV de 50 polegadas. Tudo isso no Condomínio Pipa Natureza, a poucos minutos do centro de Pipa e com trilha até a Praia do Madeiro.",
    ],
    "fotos": [("frida-piscina", "Piscina da Casa Frida no Condomínio Pipa Natureza, Pipa RN"),
              ("frida-piscina-casa", "Piscina e jardim com a casa ao fundo"),
              ("frida-fachada", "Fachada moderna da Casa Frida"),
              ("frida-deck", "Deck com espreguiçadeiras ao lado da piscina"),
              ("frida-sala-jantar", "Sala de jantar integrada à cozinha"),
              ("frida-cozinha", "Cozinha completa com bancada amarela"),
              ("frida-sala", "Sala de estar com vista para a piscina"),
              ("frida-sala-integrada", "Ambiente integrado de sala e cozinha"),
              ("frida-suite-king", "Suíte com cama king e ar-condicionado"),
              ("frida-quarto", "Quarto com cama de casal e sofá"),
              ("frida-quarto-solteiro", "Quarto com camas de solteiro"),
              ("frida-banheiro", "Banheiro da suíte"),
              ("frida-area-externa", "Área externa com piscina e pergolado"),
              ("frida-lateral", "Jardim lateral da casa")],
  },
  {
    "slug": "casa-azul", "nome": "Casa Azul", "numero": "40", "cor": "azul",
    "titulo_seo": "Casa Azul – casa com 3 suítes e piscina para alugar em Pipa",
    "descricao_seo": "Casa Azul: 3 suítes e piscina no Condomínio Pipa Natureza, Praia da Pipa (RN). Ideal para casais e famílias, até 6 hóspedes. Reserve direto pelo WhatsApp.",
    "resumo": "Piscina privativa, varanda com mesa ao ar livre e três suítes — perfeita para casais viajando juntos ou famílias.",
    "ideal": "Casais viajando juntos ou famílias que querem um banheiro para cada quarto.",
    "hospedes": 6, "quartos": 3, "suites": 3, "banheiros": "3,5",
    "camas": "2 camas de casal e 2 de solteiro",
    "quartos_detalhe": [("Suíte 1", "1 cama de casal · banheiro privativo · ar-condicionado"),
                        ("Suíte 2", "1 cama de casal · banheiro privativo · ar-condicionado"),
                        ("Suíte 3", "2 camas de solteiro · banheiro privativo · ar-condicionado")],
    "piscina": True,
    "nota": "4,82", "airbnb": "https://www.airbnb.com.br/rooms/1315796557769332463",
    "hero": "azul-piscina", "card": "azul-fachada",
    "comodidades": ["Piscina privativa", "Varanda com mesa de jantar", "Churrasqueira",
                     "3 suítes com banheiro privativo e ar-condicionado", "Cozinha equipada", "Geladeira com freezer",
                     "Cervejeira", "Smart TV na sala", "Wi-Fi", "Vaga para 1 carro",
                     "Roupa de cama e banho"],
    "bom_saber": [],
    "texto": [
      "A Casa Azul é a opção ideal para quem procura casa para alugar em Pipa com privacidade para cada casal: são 3 suítes, cada uma com seu próprio banheiro.",
      "Acomoda até 6 pessoas (2 camas de casal e 2 de solteiro). A casa tem piscina privativa cercada de jardim, varanda com mesa de jantar ao ar livre, churrasqueira, cozinha equipada com cervejeira, TV na sala e vaga para 1 carro.",
      "Fica no Condomínio Pipa Natureza, ao lado da Casa Frida, em uma região tranquila e arborizada, com acesso por trilha à Praia do Madeiro e a poucos minutos do centro de Pipa.",
    ],
    "fotos": [("azul-piscina", "Piscina da Casa Azul no Condomínio Pipa Natureza, Pipa RN"),
              ("azul-fachada", "Casa Azul com cobogós brancos e jardim"),
              ("azul-entrada", "Entrada da casa com caminho de pedras"),
              ("azul-varanda", "Varanda com mesa de jantar ao lado da piscina"),
              ("azul-sala", "Sala de estar integrada"),
              ("azul-cozinha", "Cozinha com bancada azul"),
              ("azul-sala-jantar", "Sala de jantar e cozinha"),
              ("azul-sala-estar", "Sala com vista para a piscina"),
              ("azul-suite-1", "Suíte com cama de casal"),
              ("azul-suite-2", "Suíte com acesso à área da piscina"),
              ("azul-suite-3", "Suíte com cama de casal e ar-condicionado"),
              ("azul-banheiro", "Banheiro de uma das suítes"),
              ("azul-piscina-jardim", "Piscina e jardim arborizado"),
              ("azul-jardim", "Jardim gramado da Casa Azul")],
  },
]
CAP_TOTAL = sum(c["hospedes"] for c in CASAS)

# ====== INFORMAÇÕES DA ESTADIA (dos cartões de boas-vindas) ======
REGRAS = [
  "Não fume dentro de casa.",
  "Cuide da casa: mantenha as áreas comuns limpas e arrume tudo depois de usar.",
  "Horário de silêncio do condomínio: das 22h às 9h.",
  "Visitas e hóspedes extras só com autorização prévia do anfitrião.",
  "Siga as instruções de segurança e não use aparelhos elétricos perigosos ou não autorizados.",
  "Desligue luzes, eletrodomésticos e ar-condicionado ao sair de casa.",
  "Avise o anfitrião imediatamente sobre qualquer problema ou dano.",
]
CHECKOUT_LISTA = ["Confira se não esqueceu nada.", "Desligue luzes, ar-condicionado e aparelhos.",
                  "Descarte todo o lixo.", "Feche portas e janelas.", "Deixe as chaves no cofre.",
                  "Deixe roupas de cama e toalhas usadas no chão."]
DICAS_PRAIA = [
  ("Praia do Madeiro pela trilha", "Do fim da rua do bosque, no condomínio, uma trilha de cerca de 20 minutos leva ao Madeiro. Peça ao anfitrião a senha do portão."),
  ("Confira a tábua das marés", "Programe os passeios de praia pelo horário da maré."),
  ("Pôr do sol", "Restaurante Lagoa (Tibau do Sul), Marinas, Mirante Sunset Bar, Praia do Centro e Abacate Casa do Mar."),
]
RESTAURANTES = [
  ("Lagoa Restaurante", "@lagoa.pipa", "12 min de carro", "Um dos lugares mais lindos para ver o pôr do sol, com gastronomia impecável."),
  ("Tapas Restaurante", "@tapasrestaurantepipa", "10 min de carro", "Clássico de Pipa, com cozinha de vários países. Chegue cedo!"),
  ("Cicchetti Pipa", "@cicchettipipa", "10 min de carro", "Alta gastronomia em pequenas porções e drinks diferenciados."),
]
BARES = [
  ("Taipa Brasil", "@taipabrasilpipa", "8 min de carro", "Música, drinks e cerveja gelada. Samba às quintas, a partir das 17h."),
  ("Fonte da Pipa", "@fontedapipa", "10 min de carro", "Bar intimista com DJs, bons drinks, aperitivos e sanduíches."),
  ("Ágora Club", "@agorapipa", "10 min de carro", "Balada com DJs e música ao vivo. Programação no Instagram."),
  ("Nativos Bar", "@nativosbar", "10 min de carro", "Na vila mais charmosa de Pipa, para sentar e tomar drinks."),
]
SERVICOS = [
  ("Caixa eletrônico", "Galeria Kanto da Pipa."),
  ("Posto de gasolina", "Posto Petrobras, virando à direita em direção a Goianinha."),
  ("Farmácia", "Farmácia Vidal – Av. Baía dos Golfinhos, 1285, Pipa."),
  ("Saúde", "Unidade Mista de Saúde de Tibau do Sul – Av. Três Poderes, s/n."),
  ("Coleta de lixo", "Segundas, quartas e sextas. Deixe o lixo na parte externa da casa."),
  ("Táxi e transfer 24h", "Transfer Pipa – (84) 98118-0658."),
]

def faq_lista():
    f = [
      ("Onde ficam as casas?", "As três casas ficam no Condomínio Pipa Natureza (Quinta do Sol), na Praia da Pipa, município de Tibau do Sul (RN). O centro de Pipa fica a poucos minutos de carro e há uma trilha de cerca de 20 minutos até a Praia do Madeiro."),
      ("Como faço a reserva?", "Preencha datas e número de hóspedes no formulário do site: ele abre o WhatsApp com a mensagem pronta. O anfitrião responde com a disponibilidade e o valor, e a reserva é formalizada com contrato de locação por temporada."
         + (" " + PENDENTE["formas_pagamento"] if PENDENTE["formas_pagamento"] else "")),
      ("Quanto custa a diária?", "O valor varia conforme as datas, o número de noites e de hóspedes. Você recebe o valor exato na resposta da consulta pelo WhatsApp, sem compromisso."),
      ("Qual é a estadia mínima?", f"A estadia mínima é de {MIN_NOITES} noites."),
      ("Qual o horário de check-in e check-out?", f"O check-in é a partir das {CHECKIN[:2]}h e o check-out até as {CHECKOUT[:2]}h. A entrada é autônoma: as chaves ficam em um cofre ao lado da porta, e o código é enviado um dia antes da chegada. Chegada antecipada ou saída tardia podem ser combinadas conforme a disponibilidade."),
      ("Como chegar a Pipa saindo do aeroporto de Natal?", "São cerca de 95 km (1h30 de carro) pela BR-101 Sul até Goianinha e depois em direção a Pipa. Há locadoras no aeroporto, e também é possível contratar transfer (em média R$ 250 a R$ 400 por veículo) — podemos indicar um motorista de confiança."),
      ("As casas têm estacionamento?", "Sim, cada casa tem vaga para 1 carro, e é permitido estacionar na rua em frente à casa, no sentido correto da via."),
      ("Roupa de cama e toalhas estão incluídas?", "Sim. As casas têm roupa de cama e banho para todos os hóspedes."),
      ("Dá para alugar mais de uma casa?", f"Sim. As três casas ficam no mesmo condomínio e, juntas, recebem até {CAP_TOTAL} pessoas — ótimo para famílias grandes e grupos. Escolha “Mais de uma casa” no formulário."),
    ]
    extra = [("Aceitam animais de estimação?", "animais"), ("Qual é a política de cancelamento?", "politica_cancelamento"),
             ("Há taxa de limpeza?", "taxa_limpeza"), ("Crianças e berço?", "criancas_berco"), ("Posso fazer eventos ou festas?", "eventos_festas")]
    f += [(q, PENDENTE[k]) for q, k in extra if PENDENTE[k]]
    return f

# ====== HELPERS ======
e = html.escape
try:
    from PIL import Image
except ImportError:
    Image = None
_dim = {}
def dims(nome):
    if nome not in _dim:
        try:
            _dim[nome] = Image.open(os.path.join(AQUI, "img", nome + ".webp")).size
        except Exception:
            _dim[nome] = (1200, 1600)
    return _dim[nome]

def img(nome, alt, sizes="100vw", eager=False, cls=""):
    w, h = dims(nome)
    sm = os.path.exists(os.path.join(AQUI, "img", "sm", nome + ".webp"))
    srcset = f' srcset="img/sm/{nome}.webp 640w, img/{nome}.webp {w}w" sizes="{sizes}"' if sm and w > 640 else ""
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="img/{nome}.webp"{srcset} alt="{e(alt)}" width="{w}" height="{h}"{load}{c}>'

def wa(msg):
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"

def ic(nome):
    p = {
      "hosp": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M16 14.2c2.9.3 5 2.6 5 5.8"/>',
      "cama": '<path d="M3 18V7M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.8"/>',
      "banho": '<path d="M4 12h16v2a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5v-2zM6 12V6a2 2 0 0 1 4 0M7 19l-1 2M17 19l1 2"/>',
      "piscina": '<path d="M2 15c2 0 2-1.5 4-1.5s2 1.5 4 1.5 2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5M2 19c2 0 2-1.5 4-1.5s2 1.5 4 1.5 2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5M8 12V5a2 2 0 0 1 4 0M16 12V5a2 2 0 0 0-4 0M8 8h8"/>',
      "relogio": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
      "chave": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
      "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
      "regras": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>',
      "carro": '<path d="M5 16h14v-4l-2-5H7l-2 5v4zM5 16v2M19 16v2M5 12h14"/><circle cx="8" cy="14" r=".6"/><circle cx="16" cy="14" r=".6"/>',
      "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
    }[nome]
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{p}</svg>'

WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/></svg>'
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.5 1.3 6.6L12 17.2l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
LOGO = '<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="16" fill="#b04a26"/><path d="M14 33 32 17l18 16v15H14z" fill="#faf6f0"/><path d="M14 52c4 0 4-3 9-3s5 3 9 3 5-3 9-3 5 3 9 3" stroke="#faf6f0" stroke-width="3" fill="none"/><rect x="27" y="35" width="10" height="13" rx="1" fill="#b04a26"/></svg>'
NEXT_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 15h-2v-6h2zm0-8h-2V7h2z"/></svg>'

def facts(c, full=False):
    s = f"{c['suites']} suíte{'s' if c['suites'] > 1 else ''}"
    li = [("hosp", f"Até {c['hospedes']} hóspedes"), ("cama", f"{c['quartos']} quartos ({s})" if full else f"{c['quartos']} quartos"),
          ("banho", f"{c['banheiros']} banheiros")]
    if c["piscina"]:
        li.append(("piscina", "Piscina"))
    return '<ul class="facts">' + "".join(f"<li>{ic(i)}{t}</li>" for i, t in li) + "</ul>"

def rating(c, link=True):
    if not c.get("nota"):
        return ""
    src = f' <a href="{c["airbnb"]}" rel="noopener" target="_blank">no Airbnb</a>' if link else " no Airbnb"
    return f'<span class="rating">{STAR}{c["nota"]}<span class="sr"> de 5</span>{src}</span>'

def booking_form(casa=None, wide=False, titulo="Consulte disponibilidade"):
    fid = "f-" + (casa["slug"] if casa else ("home" if wide else "geral"))
    if casa:
        sel = f'<input type="hidden" name="casa" value="{e(casa["nome"])}" data-max="{casa["hospedes"]}">'
    else:
        opts = "".join(f'<option value="{c["slug"]}" data-max="{c["hospedes"]}" data-nome="{e(c["nome"])}">{c["nome"]} (até {c["hospedes"]})</option>' for c in CASAS)
        opts += f'<option value="varias" data-max="{CAP_TOTAL}">Mais de uma casa</option>'
        opts += f'<option value="indefinida" data-max="{CAP_TOTAL}">Ainda não sei</option>'
        sel = f'<div class="field"><label for="{fid}-casa">Casa</label><select id="{fid}-casa" name="casa">{opts}</select></div>'
    obs = "" if wide else f'<div class="field full"><label for="{fid}-obs">Observações (opcional)</label><textarea id="{fid}-obs" name="obs" rows="2" placeholder="Ex.: horário de chegada, crianças"></textarea></div>'
    head = "" if wide else f'<h2 id="{fid}-t">{titulo}</h2><p class="sub">Valores e datas confirmados pelo anfitrião no WhatsApp.</p>'
    return f"""<form class="booking reserva{' booking-wide' if wide else ''}" id="{'reservar' if wide or casa else fid}" novalidate aria-label="Consultar disponibilidade">
  {head}
  <div class="fields">
    {sel}
    <div class="field"><label for="{fid}-ent">Entrada</label><input type="date" id="{fid}-ent" name="entrada" required></div>
    <div class="field"><label for="{fid}-sai">Saída</label><input type="date" id="{fid}-sai" name="saida" required></div>
    <div class="field"><label for="{fid}-hos">Hóspedes</label><input type="number" id="{fid}-hos" name="hospedes" min="1" value="2" inputmode="numeric" required></div>
    {obs}
    <div class="actions{'' if wide else ' field full'}"><button class="btn wa block" type="submit">{WA_SVG} Consultar no WhatsApp</button></div>
  </div>
  <p class="form-msg" role="status" aria-live="polite"></p>
  <noscript><p><a class="btn wa" href="{wa('Olá! Gostaria de consultar disponibilidade das casas em Pipa.')}">Falar no WhatsApp</a></p></noscript>
  <p class="next-step">{NEXT_SVG}<span>O WhatsApp abre com sua mensagem pronta. O anfitrião responde com disponibilidade e valor — nada é cobrado nesta etapa. Estadia mínima de {MIN_NOITES} noites.</span></p>
</form>"""

# ====== JSON-LD ======
def endereco_ld():
    return {"@type": "PostalAddress", "streetAddress": ENDERECO["rua"], "addressLocality": ENDERECO["cidade"],
            "addressRegion": ENDERECO["uf"], "postalCode": ENDERECO["cep"], "addressCountry": ENDERECO["pais"]}

def geo_ld():
    return {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]}

def casa_ld(c):
    d = {"@type": "LodgingBusiness", "@id": f"{DOMINIO}/{c['slug']}.html#casa",
         "name": f"{c['nome']} – Pipa Natureza", "description": c["descricao_seo"],
         "url": f"{DOMINIO}/{c['slug']}.html", "telephone": TELEFONE, **({"email": EMAIL} if EMAIL else {}),
         "address": endereco_ld(), "geo": geo_ld(),
         "checkinTime": CHECKIN, "checkoutTime": CHECKOUT, "numberOfRooms": c["quartos"],
         "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in c["comodidades"]],
         "containedInPlace": {"@type": "Place", "name": "Condomínio Pipa Natureza, Praia da Pipa"},
         "image": [f"{DOMINIO}/img/{f}.webp" for f, _ in c["fotos"]]}
    return d

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

# ====== MOLDURA ======
NAV = [("./#casas", "As casas", "index"), ("estadia.html", "A estadia", "estadia"),
       ("estadia.html#chegada", "Como chegar", None), ("./#duvidas", "Dúvidas", None), ("#contato", "Contato", None)]

def head(title, desc, path, og_img, ld, atual="", preload=""):
    url = f"{DOMINIO}/{path}" if path else f"{DOMINIO}/"
    nav = "".join(f'<a href="{h}"{" aria-current=page" if k and k == atual else ""}>{t}</a>' for h, t, k in NAV)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="BR-RN"><meta name="geo.placename" content="Praia da Pipa, Tibau do Sul"><meta name="geo.position" content="{GEO[0]};{GEO[1]}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="{e(MARCA)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/{og_img}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#faf6f0">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
{preload}<link rel="stylesheet" href="style.css">
{jsonld(ld)}
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="./" aria-label="{MARCA} – início">{LOGO}<span class="txt">Casas em <span>Pipa</span></span></a>
    <nav class="menu" aria-label="Menu principal">{nav}</nav>
    <a class="btn sm" href="#reservar">Reservar</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Abrir menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
  </div>
  <div class="drawer" id="drawer"><nav aria-label="Menu">{nav}<a href="{wa('Olá! Vim pelo site das casas em Pipa.')}" rel="nofollow">WhatsApp {TELEFONE}</a></nav></div>
</header>
<main id="conteudo">
"""

def foot(cta_casa=None):
    msg = f"Olá! Vim pelo site e tenho uma dúvida sobre a {cta_casa['nome']}." if cta_casa else "Olá! Vim pelo site e tenho uma dúvida sobre as casas em Pipa."
    casas = "".join(f'<p><a href="{c["slug"]}.html">{c["nome"]}</a> – até {c["hospedes"]} hóspedes</p>' for c in CASAS)
    mail = f'<p>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>' if EMAIL else ""
    return f"""
<section id="contato" aria-labelledby="ct"><div class="wrap">
  <div class="cta-band">
    <div><p class="eyebrow" style="color:#e9b79f">Atendimento direto</p><h2 id="ct">Fale com o anfitrião</h2>
      <p>{ANFITRIAO} responde pessoalmente pelo WhatsApp: datas, valores, dúvidas sobre as casas e dicas de Pipa.</p></div>
    <div class="row"><a class="btn wa" href="{wa(msg)}" rel="nofollow">{WA_SVG} WhatsApp {TELEFONE}</a>
      <a class="btn light" href="https://instagram.com/{INSTAGRAM}" rel="noopener" target="_blank">Instagram @{INSTAGRAM}</a></div>
  </div>
</div></section>
</main>
<footer><div class="wrap">
  <div class="cols">
    <div><h4>{MARCA}</h4><p>Casas de temporada com piscina no Condomínio Pipa Natureza, Praia da Pipa – Tibau do Sul/RN.</p>
      <p>{ENDERECO['rua']}, {ENDERECO['bairro']}<br>{ENDERECO['cidade']}/{ENDERECO['uf']} – CEP {ENDERECO['cep']}</p></div>
    <div><h4>As casas</h4>{casas}<p><a href="estadia.html">Informações da estadia</a></p></div>
    <div><h4>Contato</h4><p>WhatsApp: <a href="{wa('Olá! Vim pelo site das casas em Pipa.')}" rel="nofollow">{TELEFONE}</a></p>{mail}
      <p>Instagram: <a href="https://instagram.com/{INSTAGRAM}" rel="noopener" target="_blank">@{INSTAGRAM}</a></p>
      <p>Check-in {CHECKIN[:2]}h · Check-out {CHECKOUT[:2]}h</p></div>
  </div>
  <p class="fine">© {datetime.date.today().year} {MARCA}. Reserva direta com o anfitrião.</p>
</div></footer>
<div class="mbar"><a class="btn" href="#reservar">Consultar datas</a><a class="btn wa" href="{wa(msg)}" rel="nofollow" aria-label="Falar no WhatsApp">{WA_SVG}</a></div>
<script>window.SITE={{whatsapp:"{WHATSAPP}",minNoites:{MIN_NOITES}}};</script>
<script src="site.js" defer></script>
</body></html>
"""

# ====== PÁGINA INICIAL ======
def pagina_inicial():
    title = "Casas com piscina para alugar em Pipa (RN) – Condomínio Pipa Natureza"
    desc = (f"Três casas de temporada com piscina no Condomínio Pipa Natureza, Praia da Pipa (RN): Terracota, Frida e Azul, todas com 3 suítes. "
            f"De 6 a 8 hóspedes por casa, até {CAP_TOTAL} juntas. Reserve direto com o anfitrião pelo WhatsApp.")
    faq = faq_lista()
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": f"{DOMINIO}/#site", "url": f"{DOMINIO}/", "name": MARCA, "inLanguage": "pt-BR"},
        {"@type": "LodgingBusiness", "@id": f"{DOMINIO}/#negocio", "name": MARCA, "description": desc, "url": f"{DOMINIO}/",
         "telephone": TELEFONE, **({"email": EMAIL} if EMAIL else {}), "image": f"{DOMINIO}/img/{CASAS[0]['hero']}.webp",
         "address": endereco_ld(), "geo": geo_ld(), "checkinTime": CHECKIN, "checkoutTime": CHECKOUT,
         "areaServed": "Praia da Pipa, Tibau do Sul, RN", "sameAs": [f"https://instagram.com/{INSTAGRAM}"],
         "makesOffer": [{"@type": "Offer", "itemOffered": {"@id": f"{DOMINIO}/{c['slug']}.html#casa"}} for c in CASAS]},
        *[casa_ld(c) for c in CASAS],
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
    ]}
    hero_cols = "".join(f"""<a class="hero-col" href="{c['slug']}.html">{img(c['hero'], c['fotos'][0][1] if c['fotos'][0][0] == c['hero'] else f"Piscina da {c['nome']} em Pipa", sizes="(min-width:900px) 34vw, 86vw", eager=(i == 0))}
      <span class="hero-tag"><b>{c['nome']}</b><small>Até {c['hospedes']} hóspedes · {c['quartos']} quartos</small></span></a>""" for i, c in enumerate(CASAS))
    cards = "".join(f"""
    <article class="house acc-{c['cor']}">
      <a class="ph" href="{c['slug']}.html" tabindex="-1" aria-hidden="true">{img(c['card'], '', sizes="(min-width:760px) 33vw, 100vw")}{f'<span class="badge">{STAR}{c["nota"]}</span>' if c.get("nota") else ''}</a>
      <div class="body">
        <h3><a href="{c['slug']}.html" style="color:inherit;text-decoration:none">{c['nome']}</a></h3>
        {facts(c)}
        <p>{e(c['resumo'])}</p>
        <p class="ideal"><b>Ideal para:</b> {e(c['ideal'])}</p>
        <div class="ctas"><a class="btn" href="{c['slug']}.html">Ver a casa</a>
          <a class="btn ghost" href="{wa(f"Olá! Gostaria de saber a disponibilidade da {c['nome']} em Pipa.")}" rel="nofollow">Consultar</a></div>
      </div>
    </article>""" for c in CASAS)
    linhas = [("Hóspedes", lambda c: f"até {c['hospedes']}"), ("Quartos", lambda c: f"{c['quartos']} ({c['suites']} suíte{'s' if c['suites'] > 1 else ''})"),
              ("Banheiros", lambda c: c["banheiros"]), ("Camas", lambda c: c["camas"]),
              ("Destaque", lambda c: c["comodidades"][1])]
    tabela = ("<thead><tr><td></td>" + "".join(f'<th scope="col"><a href="{c["slug"]}.html" style="color:inherit">{c["nome"]}</a></th>' for c in CASAS) + "</tr></thead><tbody>"
              + "".join(f'<tr><th scope="row">{r}</th>' + "".join(f"<td>{e(str(f(c)))}</td>" for c in CASAS) + "</tr>" for r, f in linhas) + "</tbody>")
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq[:6])
    pre = f'<link rel="preload" as="image" href="img/sm/{CASAS[0]["hero"]}.webp" media="(max-width:899px)">\n'
    return head(title, desc, "", f"img/{CASAS[1]['hero']}.webp", ld, "index", pre) + f"""
<section class="hero" aria-label="As três casas" style="padding:0">
  <div class="hero-media">{hero_cols}</div>
  <div class="hero-copy"><div class="wrap">
    <p class="eyebrow">Praia da Pipa · Rio Grande do Norte</p>
    <h1>Três casas com piscina entre a mata e o mar</h1>
    <p>Casas de temporada no Condomínio Pipa Natureza, a uma trilha da Praia do Madeiro. Reserve direto com o anfitrião.</p>
    <div class="hero-ctas"><a class="btn" href="#reservar">Consultar disponibilidade</a><a class="btn ghost" href="#casas">Conhecer as casas</a></div>
  </div></div>
</section>

<div class="wrap">{booking_form(wide=True)}</div>

<section id="casas" aria-labelledby="casas-t"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">As casas</p><h2 id="casas-t">Escolha a casa ideal</h2></div>
    <p class="lead">Três casas no mesmo condomínio, cada uma com piscina e personalidade própria. Para grupos grandes, dá para reservar mais de uma.</p></div>
  <div class="houses">{cards}</div>
  <p class="note mt">Notas dos hóspedes no Airbnb, conferidas em {NOTAS_DATA}.</p>
  <h3 class="mt" style="margin-bottom:12px">Compare lado a lado</h3>
  <div class="table-scroll"><table class="compare">{tabela}</table></div>
</div></section>

<section class="alt" aria-labelledby="exp-t"><div class="wrap split">
  <div class="pair">{img('frida-deck', 'Deck com espreguiçadeiras e piscina no Pipa Natureza', sizes="(min-width:900px) 25vw, 50vw")}{img('azul-varanda', 'Varanda com mesa de jantar ao ar livre', sizes="(min-width:900px) 25vw, 50vw")}</div>
  <div>
    <p class="eyebrow">A experiência</p>
    <h2 id="exp-t">Pipa Natureza: sossego perto de tudo</h2>
    <p class="lead">Um condomínio cercado de mata atlântica, com dias de piscina, churrasco na varanda e a praia a uma caminhada. O centro de Pipa, com restaurantes e bares, fica a poucos minutos de carro.</p>
    <ul class="highlights">
      <li><b>20 min</b><span>de trilha até a Praia do Madeiro</span></li>
      <li><b>Golfinhos</b><span>na Baía dos Golfinhos e no Madeiro</span></li>
      <li><b>~10 min</b><span>de carro até restaurantes e bares</span></li>
      <li><b>1h30</b><span>do Aeroporto Internacional de Natal</span></li>
    </ul>
  </div>
</div></section>

<section aria-labelledby="como-t"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">Reserva direta</p><h2 id="como-t">Como funciona a reserva</h2></div>
    <p class="lead">Simples e sem taxa de plataforma: você fala direto com quem cuida das casas.</p></div>
  <ol class="steps">
    <li><h3>Envie suas datas</h3><p>Escolha casa, datas e número de hóspedes. O WhatsApp abre com a mensagem pronta.</p></li>
    <li><h3>Receba o valor</h3><p>O anfitrião confirma a disponibilidade e informa o valor total da estadia.</p></li>
    <li><h3>Confirme a reserva</h3><p>A reserva é formalizada com contrato de locação por temporada.{(' ' + e(PENDENTE['formas_pagamento'])) if PENDENTE['formas_pagamento'] else ''}</p></li>
  </ol>
  <p class="center mt"><a class="btn" href="#reservar">Consultar disponibilidade</a></p>
</div></section>

<section class="alt" aria-labelledby="info-t"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">Antes de chegar</p><h2 id="info-t">Informações da estadia</h2></div>
    <a class="link" href="estadia.html">Ver todas as informações</a></div>
  <div class="tiles">
    <a class="tile" href="estadia.html#checkin">{ic('relogio')}<b>Check-in {CHECKIN[:2]}h</b><span>Entrada autônoma com cofre de chaves</span></a>
    <a class="tile" href="estadia.html#checkout">{ic('chave')}<b>Check-out {CHECKOUT[:2]}h</b><span>Saída tardia sob consulta</span></a>
    <a class="tile" href="estadia.html#regras">{ic('regras')}<b>Regras da casa</b><span>Silêncio das 22h às 9h</span></a>
    <a class="tile" href="estadia.html#chegada">{ic('pin')}<b>Como chegar</b><span>95 km do aeroporto de Natal</span></a>
  </div>
</div></section>

<section id="duvidas" aria-labelledby="faq-t"><div class="wrap">
  <p class="eyebrow">Dúvidas</p><h2 id="faq-t">Perguntas frequentes</h2>
  <div class="faq">{faq_html}</div>
  <p class="mt"><a class="link" href="estadia.html#duvidas">Mais perguntas e respostas</a></p>
</div></section>
""" + foot()

# ====== PÁGINA DE CADA CASA ======
def pagina_casa(c):
    others = [o for o in CASAS if o is not c]
    bc = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{DOMINIO}/"},
        {"@type": "ListItem", "position": 2, "name": c["nome"], "item": f"{DOMINIO}/{c['slug']}.html"}]}
    ld = {"@context": "https://schema.org", "@graph": [casa_ld(c), bc]}
    fotos = [(c["hero"], next(a for f, a in c["fotos"] if f == c["hero"]))] + [(f, a) for f, a in c["fotos"] if f != c["hero"]]
    gal = "".join(f'<button type="button" data-lb="img/{f}.webp" aria-label="Ampliar foto: {e(a)}">'
                  + (img(f, a, sizes="(min-width:900px) 50vw, 88vw", eager=(i == 0)) if i == 0 or i > 4
                     else img(f, a, sizes="(min-width:900px) 25vw, 88vw").replace(' loading="lazy"', ''))
                  + '</button>' for i, (f, a) in enumerate(fotos))
    texto = "".join(f"<p>{e(p)}</p>" for p in c["texto"])
    if c["quartos_detalhe"]:
        rooms = '<div class="rooms">' + "".join(f'<div class="room"><b>{e(n)}</b><span>{e(d)}</span></div>' for n, d in c["quartos_detalhe"]) + "</div>"
    else:
        rooms = f'<div class="rooms"><div class="room"><b>{c["quartos"]} quartos</b><span>{e(c["camas"])}</span></div><div class="room"><b>{c["banheiros"]} banheiros</b><span>{c["suites"]} suíte{"s" if c["suites"] > 1 else ""}</span></div></div>'
    amen = "".join(f"<li>{e(a)}</li>" for a in c["comodidades"])
    bom = [("Check-in", f"a partir das {CHECKIN[:2]}h"), ("Check-out", f"até as {CHECKOUT[:2]}h"),
           ("Estadia mínima", f"{MIN_NOITES} noites"), ("Estacionamento", "1 vaga + rua")]
    bom_html = '<div class="know">' + "".join(f"<div><b>{k}</b><span>{v}</span></div>" for k, v in bom) + "</div>"
    extras = [*c["bom_saber"], *(PENDENTE[k] for k in ("animais", "politica_cancelamento", "taxa_limpeza") if PENDENTE[k])]
    extras_html = ('<ul class="amen" style="columns:1">' + "".join(f"<li>{e(x)}</li>" for x in extras) + "</ul>") if extras else ""
    outras = "".join(f"""
    <article class="house acc-{o['cor']}">
      <a class="ph" href="{o['slug']}.html" tabindex="-1" aria-hidden="true">{img(o['card'], '', sizes="(min-width:760px) 50vw, 100vw")}</a>
      <div class="body"><h3><a href="{o['slug']}.html" style="color:inherit;text-decoration:none">{o['nome']}</a></h3>{facts(o)}<p>{e(o['resumo'])}</p>
        <div class="ctas"><a class="btn ghost" href="{o['slug']}.html">Ver a {o['nome']}</a></div></div></article>""" for o in others)
    mapa = f"https://maps.google.com/maps?q={GEO[0]},{GEO[1]}&z=15&output=embed"
    pre = f'<link rel="preload" as="image" href="img/sm/{c["hero"]}.webp" media="(max-width:899px)">\n'
    return head(c["titulo_seo"], c["descricao_seo"], f"{c['slug']}.html", f"img/{c['hero']}.webp", ld, c["slug"], pre) + f"""
<div class="wrap acc-{c['cor']}">
  <nav class="crumbs" aria-label="Você está em"><a href="./">Início</a> › <a href="./#casas">As casas</a> › {c['nome']}</nav>
  <div class="house-head">
    <div><p class="eyebrow" style="color:var(--accent)">Casa {c['numero']} · Condomínio Pipa Natureza</p>
      <h1>{c['nome']}</h1>{facts(c, full=True)}</div>
    {rating(c)}
  </div>
  <div class="gal">
    <div class="gal-grid">{gal}</div>
    <span class="gal-count" aria-hidden="true">1 / {len(fotos)}</span>
    <button class="btn light sm gal-all" type="button" data-lb-open>Ver as {len(fotos)} fotos</button>
  </div>

  <div class="house-layout">
    <div>
      <div class="block"><h2>Sobre a casa</h2><p class="lead" style="margin-bottom:14px">{e(c['resumo'])}</p>{texto}
        <p class="ideal" style="margin-top:8px"><b>Ideal para:</b> {e(c['ideal'])}</p></div>
      <div class="block"><h2>Quartos e camas</h2>{rooms}</div>
      <div class="block"><h2>Comodidades</h2><ul class="amen">{amen}</ul></div>
      <div class="block"><h2>Bom saber</h2>{bom_html}{extras_html}
        <p class="mt">Entrada autônoma: as chaves ficam em um cofre ao lado da porta, e o código é enviado um dia antes da chegada.
        <a class="link" href="estadia.html">Regras e informações da estadia</a></p></div>
      <div class="block"><h2>Localização</h2>
        <p>{ENDERECO['rua']}, Casa {c['numero']} – {ENDERECO['bairro']}, {ENDERECO['cidade']}/{ENDERECO['uf']}. Trilha de cerca de 20 minutos até a Praia do Madeiro.</p>
        <iframe class="map" src="{mapa}" title="Mapa: Condomínio Pipa Natureza, Praia da Pipa" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        <p class="mt"><a class="link" href="https://www.google.com/maps/search/?api=1&query={GEO[0]},{GEO[1]}" rel="noopener" target="_blank">Abrir no Google Maps</a> &nbsp; <a class="link" href="estadia.html#chegada">Como chegar</a></p></div>
    </div>
    <aside aria-label="Consultar disponibilidade da {c['nome']}">{booking_form(c, titulo=f"Consulte a {c['nome']}")}</aside>
  </div>
</div>

<section class="alt" aria-labelledby="out-t" style="margin-top:40px"><div class="wrap">
  <h2 id="out-t">Outras casas no Pipa Natureza</h2>
  <p class="lead">Viajando em grupo? As casas ficam no mesmo condomínio e podem ser reservadas juntas.</p>
  <div class="houses" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{outras}</div>
</div></section>

<dialog class="lb" aria-label="Fotos da {c['nome']}">
  <div class="lb-top"><span class="lb-n" aria-live="polite"></span><button class="lb-btn lb-close" type="button" aria-label="Fechar">✕</button></div>
  <button class="lb-btn lb-prev" type="button" aria-label="Foto anterior">‹</button>
  <div class="lb-stage"><img alt=""></div>
  <button class="lb-btn lb-next" type="button" aria-label="Próxima foto">›</button>
  <p class="lb-cap"></p>
</dialog>
""" + foot(c)

# ====== INFORMAÇÕES DA ESTADIA ======
def pagina_estadia():
    title = "Informações da estadia – check-in, regras e como chegar | Casas em Pipa"
    desc = "Check-in, check-out, regras da casa, como chegar do aeroporto de Natal, dicas de praias, restaurantes e bares em Pipa e telefones úteis."
    faq = faq_lista()
    bc = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{DOMINIO}/"},
        {"@type": "ListItem", "position": 2, "name": "A estadia", "item": f"{DOMINIO}/estadia.html"}]}
    ld = {"@context": "https://schema.org", "@graph": [bc,
          {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    chips = "".join(f'<a href="#{a}">{t}</a>' for a, t in [("checkin", "Check-in"), ("checkout", "Check-out"), ("regras", "Regras"),
        ("incluido", "O que está incluído"), ("chegada", "Como chegar"), ("dicas", "Dicas em Pipa"), ("servicos", "Serviços e emergências"), ("duvidas", "Dúvidas")])
    regras = "".join(f"<li>{e(r)}</li>" for r in REGRAS + [PENDENTE[k] for k in ("animais", "eventos_festas") if PENDENTE[k]])
    saida = "".join(f"<li>{e(x)}</li>" for x in CHECKOUT_LISTA)
    def lugares(lst):
        return '<div class="places">' + "".join(f'<div class="place"><b>{e(n)}</b><small>{e(t)}</small> · <a href="https://instagram.com/{ig[1:]}" rel="noopener" target="_blank">{e(ig)}</a><p>{e(d)}</p></div>' for n, ig, t, d in lst) + "</div>"
    praias = '<div class="places">' + "".join(f'<div class="place"><b>{e(n)}</b><p>{e(d)}</p></div>' for n, d in DICAS_PRAIA) + "</div>"
    serv = '<div class="places">' + "".join(f'<div class="place"><b>{e(n)}</b><p>{e(d)}</p></div>' for n, d in SERVICOS) + "</div>"
    incl = ["Roupa de cama e banho", "Wi-Fi", "Cozinha equipada com louças, panelas e utensílios", "Vaga para 1 carro"]
    incl += [PENDENTE[k] for k in ("taxa_limpeza", "criancas_berco") if PENDENTE[k]]
    incl_html = "".join(f"<li>{e(x)}</li>" for x in incl)
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq)
    rota = f"https://www.google.com/maps/dir/?api=1&origin={quote('Aeroporto Internacional de Natal')}&destination={GEO[0]},{GEO[1]}"
    return head(title, desc, "estadia.html", f"img/{CASAS[2]['hero']}.webp", ld, "estadia") + f"""
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="./">Início</a> › A estadia</nav>
  <div style="padding:16px 0 8px"><p class="eyebrow">Guia do hóspede</p><h1 style="font-size:clamp(2rem,5vw,3.2rem);margin-bottom:10px">Informações da estadia</h1>
    <p class="lead" style="margin-bottom:16px">Tudo o que você precisa saber antes de chegar às casas do Pipa Natureza.</p></div>
  <nav class="chips" aria-label="Nesta página">{chips}</nav>
</div>

<section class="info-sec" id="checkin" style="padding-top:28px"><div class="wrap info-grid">
  <div class="panel"><h2>Check-in</h2><p class="big-time">{CHECKIN[:2]}h</p>
    <p>Entrada autônoma: as chaves ficam em um cofre ao lado da porta da frente. O código do cofre é enviado por mensagem um dia antes da sua chegada.</p>
    <p>Quer chegar mais cedo? Fale com o anfitrião — faremos o possível para atender.</p></div>
  <div class="panel info-sec" id="checkout"><h2>Check-out</h2><p class="big-time">{CHECKOUT[:2]}h</p>
    <p>Antes de sair:</p><ul>{saida}</ul><p class="mt">Precisa sair mais tarde? Consulte o anfitrião.</p></div>
</div></section>

<section class="alt info-sec" id="regras"><div class="wrap">
  <h2>Regras da casa</h2><p class="lead">Valem para as três casas. Obrigado por ajudar a manter o Pipa Natureza tranquilo.</p>
  <ul class="rules">{regras}</ul>
</div></section>

<section class="info-sec" id="incluido"><div class="wrap info-grid">
  <div class="panel"><h2>O que está incluído</h2><ul>{incl_html}</ul>
    <p class="mt muted">As comodidades de cada casa estão na página dela.</p></div>
  <div class="panel"><h2>Estacionamento</h2><p>Cada casa tem vaga para 1 carro. Também é permitido estacionar na rua em frente à casa, desde que no sentido correto da via.</p></div>
</div></section>

<section class="alt info-sec" id="chegada"><div class="wrap split">
  <div>
    <p class="eyebrow">Como chegar</p><h2>Do aeroporto de Natal até Pipa</h2>
    <div class="panel" style="margin-bottom:14px"><h3>De carro</h3><p>Cerca de 95 km (1h30). Siga pela BR-101 Sul até Goianinha e entre em direção a Pipa. Há locadoras no próprio aeroporto.</p></div>
    <div class="panel" style="margin-bottom:14px"><h3>Transfer particular</h3><p>O motorista busca você no desembarque e leva até a porta da casa. O trajeto leva de 1h30 a 2h; o valor médio é de R$ 250 a R$ 400 por veículo, conforme o número de passageiros. Se preferir, indicamos um motorista de confiança.</p></div>
    <p><a class="btn" href="{rota}" rel="noopener" target="_blank">Traçar rota no Google Maps</a></p>
  </div>
  <iframe class="map" style="height:100%;min-height:360px" src="https://maps.google.com/maps?q={GEO[0]},{GEO[1]}&z=12&output=embed" title="Mapa da localização das casas em Pipa" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div></section>

<section class="info-sec" id="dicas"><div class="wrap">
  <p class="eyebrow">Recomendações do anfitrião</p><h2>Dicas em Pipa</h2>
  <h3 class="mt" style="margin-bottom:12px">Praia e pôr do sol</h3>{praias}
  <h3 class="mt" style="margin-bottom:12px">Restaurantes</h3>{lugares(RESTAURANTES)}
  <h3 class="mt" style="margin-bottom:12px">Bares e vida noturna</h3>{lugares(BARES)}
</div></section>

<section class="alt info-sec" id="servicos"><div class="wrap">
  <h2>Serviços e emergências</h2>
  <div class="emerg" style="margin:18px 0 24px"><a href="tel:192"><b>192</b><span>SAMU</span></a><a href="tel:190"><b>190</b><span>Polícia</span></a><a href="tel:193"><b>193</b><span>Bombeiros</span></a></div>
  {serv}
</div></section>

<section class="info-sec" id="duvidas"><div class="wrap">
  <h2>Perguntas frequentes</h2><div class="faq">{faq_html}</div>
</div></section>

<section class="alt" aria-labelledby="res-t"><div class="wrap" style="max-width:720px">
  {booking_form(titulo="Consulte disponibilidade")}
</div></section>
""".replace('id="f-geral"', 'id="reservar"') + foot()

def pagina_404():
    return head("Página não encontrada | Casas em Pipa", "Página não encontrada.", "404.html", f"img/{CASAS[0]['hero']}.webp",
                {"@context": "https://schema.org", "@type": "WebPage", "name": "404"}).replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">').replace('href="./', f'href="{DOMINIO}/').replace('href="estadia', f'href="{DOMINIO}/estadia') + f"""
<section><div class="wrap center"><h1>Página não encontrada</h1><p class="lead" style="margin:16px auto 24px">O endereço pode ter mudado. Veja as casas ou fale com o anfitrião.</p>
<p><a class="btn" href="{DOMINIO}/">Ver as casas</a></p></div></section>
<div id="reservar"></div>
""" + foot()

def favicon():
    return LOGO.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"')

def sitemap():
    urls = [("", "1.0")] + [(f"{c['slug']}.html", "0.9") for c in CASAS] + [("estadia.html", "0.6")]
    body = "".join(f"<url><loc>{DOMINIO}/{u}</loc><lastmod>{HOJE}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'

if __name__ == "__main__":
    files = {"index.html": pagina_inicial(), "estadia.html": pagina_estadia(), "404.html": pagina_404(),
             "favicon.svg": favicon(), "sitemap.xml": sitemap(),
             "robots.txt": f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n"}
    for c in CASAS:
        files[f"{c['slug']}.html"] = pagina_casa(c)
    for name, content in files.items():
        with open(os.path.join(AQUI, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        print("ok", name)
    falta = [k for k, v in PENDENTE.items() if not v] + [f"quartos_detalhe ({c['nome']})" for c in CASAS if not c["quartos_detalhe"]]
    if falta:
        print("\nPENDENTE (não aparece no site até ser preenchido):\n  - " + "\n  - ".join(falta))
