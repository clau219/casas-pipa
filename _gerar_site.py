# -*- coding: utf-8 -*-
"""
Gera o site das Casas em Pipa (HTML estático + sitemap.xml + robots.txt).

Como usar: edite os dados abaixo (DOMINIO, contato, casas) e rode:
    python _gerar_site.py
Os arquivos .html são recriados nesta mesma pasta.
"""
import json, html, datetime, os

# ====== CONFIGURAÇÃO GERAL ======
DOMINIO   = "https://clau219.github.io/casas-pipa"   # troque por "https://www.casasempipa.com.br" quando o domínio estiver registrado e ligado
MARCA     = "Casas em Pipa"
WHATSAPP  = "5584996011991"                    # só números, com 55 + DDD
TELEFONE  = "+55 84 99601-1991"
EMAIL     = os.environ.get("SITE_EMAIL", "")   # opcional: defina SITE_EMAIL para mostrar um e-mail no site
INSTAGRAM = "casafridapipa"
ANFITRIAO = "Claudio Roberto"
ENDERECO  = {"rua": "Condomínio Pipa Natureza, Quinta do Sol", "cidade": "Tibau do Sul",
             "uf": "RN", "cep": "59178-000", "pais": "BR", "bairro": "Praia da Pipa"}
CHECKIN, CHECKOUT = "14:00", "11:00"
HOJE = datetime.date.today().isoformat()

# ====== AS CASAS ======
CASAS = [
  {
    "slug": "casa-terracota",
    "nome": "Casa Terracota",
    "numero": "50",
    "cor": "terracota",
    "titulo_seo": "Casa Terracota – casa com piscina para 7 pessoas na Praia da Pipa",
    "descricao_seo": "Casa de temporada com piscina, 3 quartos e ar-condicionado no Condomínio Pipa Natureza, Praia da Pipa (RN). Até 7 hóspedes. Reserve direto pelo WhatsApp.",
    "resumo": "Arquitetura moderna com cobogós terracota, piscina privativa e varanda gourmet integrada à sala e à cozinha.",
    "hospedes": 7, "quartos": 3, "suites": 1, "banheiros": "2,5",
    "camas": "1 cama de casal e 5 de solteiro",
    "piscina": True,
    "comodidades": ["Piscina privativa", "Varanda gourmet com mesa para 8", "Ar-condicionado nos quartos",
                     "Cozinha completa com bancada", "Wi-Fi", "Smart TV", "Jardim gramado",
                     "Vaga para 1 carro", "Roupa de cama e banho", "Limpeza incluída"],
    "texto": [
      "A Casa Terracota é uma casa de temporada em Pipa pensada para famílias e grupos de amigos que querem espaço, privacidade e conforto a poucos minutos das praias mais bonitas do litoral potiguar.",
      "A sala, a cozinha e a varanda gourmet formam um único ambiente aberto para a piscina, com pé-direito alto e muita luz natural. São 3 quartos com ar-condicionado — sendo 1 suíte — e 2,5 banheiros, acomodando até 7 pessoas.",
      "Fica no Condomínio Pipa Natureza, em meio à mata atlântica, com trilha de cerca de 20 minutos até a Praia do Madeiro, famosa pelos golfinhos e pelo mar calmo.",
    ],
    "fotos": [("terracota-piscina", "Piscina e varanda gourmet da Casa Terracota em Pipa"),
              ("terracota-fachada", "Fachada com cobogós terracota no Condomínio Pipa Natureza"),
              ("terracota-varanda-gourmet", "Varanda gourmet com mesa de jantar ao lado da piscina"),
              ("terracota-sala-cozinha", "Sala integrada à cozinha"),
              ("terracota-cozinha", "Cozinha completa com bancada"),
              ("terracota-sala", "Sala de estar com sofás e TV"),
              ("terracota-quarto-casal", "Quarto de casal com ar-condicionado"),
              ("terracota-quarto-solteiro", "Quarto com camas de solteiro"),
              ("terracota-banheiro", "Banheiro da suíte"),
              ("terracota-jardim", "Jardim e área externa ao pôr do sol"),
              ("terracota-sala-integrada", "Ambiente integrado com vista para o jardim"),
              ("terracota-entrada", "Entrada da casa")],
  },
  {
    "slug": "casa-frida",
    "nome": "Casa Frida",
    "numero": "39",
    "cor": "frida",
    "titulo_seo": "Casa Frida – casa de temporada com piscina e churrasqueira em Pipa",
    "descricao_seo": "Casa Frida: 3 quartos com suíte king, piscina, churrasqueira e adega no Condomínio Pipa Natureza, Praia da Pipa (RN). Até 8 hóspedes. Reserve pelo WhatsApp.",
    "resumo": "Casa moderna e colorida, com piscina, deck com espreguiçadeiras, churrasqueira e suíte com cama king.",
    "hospedes": 8, "quartos": 3, "suites": 1, "banheiros": "3,5",
    "camas": "1 cama king, 1 queen e 4 de solteiro",
    "piscina": True,
    "comodidades": ["Piscina", "Churrasqueira de inox na varanda", "Mesa de jantar para 6",
                     "Suíte com cama king", "Ar-condicionado e ventilador de teto", "TV 50\" e Chromecast",
                     "Adega de vinhos", "Air fryer, cafeteira e forno elétrico", "Wi-Fi",
                     "Vaga para 1 carro", "Roupa de cama e banho", "Limpeza incluída"],
    "texto": [
      "A Casa Frida é uma hospedagem em Pipa com personalidade: cores, arte e uma área externa feita para aproveitar o clima do Rio Grande do Norte o ano inteiro.",
      "São 3 quartos — uma suíte com cama king, um quarto com cama queen e um quarto com camas de solteiro — e 3,5 banheiros, para até 8 hóspedes. A varanda tem churrasqueira de inox e mesa redonda para 6, de frente para a piscina.",
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
    "slug": "casa-azul",
    "nome": "Casa Azul",
    "numero": "40",
    "cor": "azul",
    "titulo_seo": "Casa Azul – casa com 3 suítes e piscina para alugar em Pipa",
    "descricao_seo": "Casa Azul: 3 suítes e piscina no Condomínio Pipa Natureza, Praia da Pipa (RN). Ideal para casais e famílias, até 6 hóspedes. Reserve direto pelo WhatsApp.",
    "resumo": "Três suítes independentes e piscina — perfeita para casais viajando juntos ou famílias que querem privacidade.",
    "hospedes": 6, "quartos": 3, "suites": 3, "banheiros": "3,5",
    "camas": "2 camas de casal e 2 de solteiro",
    "piscina": True,
    "comodidades": ["Piscina privativa", "Varanda com mesa de jantar", "Churrasqueira",
                     "3 suítes com banheiro privativo e ar-condicionado", "Cozinha equipada", "Geladeira com freezer",
                     "Cervejeira", "Smart TV na sala", "Wi-Fi", "Vaga para 1 carro",
                     "Roupa de cama e banho", "Limpeza incluída"],
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

FAQ = [
  ("Onde ficam as casas?", "As três casas ficam no Condomínio Pipa Natureza (Quinta do Sol), na Praia da Pipa, município de Tibau do Sul, Rio Grande do Norte. O centro de Pipa fica a poucos minutos de carro e há uma trilha de cerca de 20 minutos até a Praia do Madeiro."),
  ("Como reservar?", "A reserva é feita direto com o anfitrião pelo WhatsApp: informe as datas e o número de hóspedes que respondemos com a disponibilidade e o valor. A reserva é formalizada com contrato de locação por temporada."),
  ("Qual o horário de check-in e check-out?", f"O check-in é a partir das {CHECKIN[:2]}h e o check-out até as {CHECKOUT[:2]}h. Chegada antecipada ou saída tardia podem ser combinadas conforme a disponibilidade."),
  ("Como chegar a Pipa saindo do aeroporto de Natal?", "São cerca de 95 km (1h30 de carro) pela BR-101 Sul até Goianinha e depois em direção a Pipa. Também é possível contratar transfer no aeroporto — podemos indicar um motorista de confiança."),
  ("As casas têm estacionamento?", "Sim, cada casa tem vaga para 1 carro, e é permitido estacionar na rua em frente à casa."),
  ("Roupa de cama e toalhas estão incluídas?", "Sim. As casas são entregues limpas, com roupa de cama e banho, e a limpeza já está incluída no valor da diária."),
]

# ====== HELPERS ======
e = html.escape
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/></svg>'

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"

def endereco_ld():
    return {"@type": "PostalAddress", "streetAddress": ENDERECO["rua"], "addressLocality": ENDERECO["cidade"],
            "addressRegion": ENDERECO["uf"], "postalCode": ENDERECO["cep"], "addressCountry": ENDERECO["pais"]}

def amenities_ld(c):
    return [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in c["comodidades"]]

def casa_ld(c):
    d = {"@type": "LodgingBusiness", "@id": f"{DOMINIO}/{c['slug']}.html#casa",
         "name": f"{c['nome']} – Pipa Natureza", "description": c["descricao_seo"],
         "url": f"{DOMINIO}/{c['slug']}.html", "telephone": TELEFONE, **({"email": EMAIL} if EMAIL else {}),
         "address": endereco_ld(), "priceRange": "$$",
         "checkinTime": CHECKIN, "checkoutTime": CHECKOUT,
         "numberOfRooms": c["quartos"], "petsAllowed": False,
         "amenityFeature": amenities_ld(c),
         "containedInPlace": {"@type": "Place", "name": "Condomínio Pipa Natureza, Praia da Pipa"}}
    imgs = [f"{DOMINIO}/img/{f}.webp" for f, _ in c["fotos"]] or [f"{DOMINIO}/img/og-casas-pipa.jpg"]
    d["image"] = imgs
    return d

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, indent=1) + '</script>'

def head(title, desc, path, og_img="img/og-casas-pipa.jpg", extra_ld=""):
    url = f"{DOMINIO}/{path}" if path else f"{DOMINIO}/"
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="BR-RN"><meta name="geo.placename" content="Praia da Pipa, Tibau do Sul">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{e(MARCA)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#c4552f">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
{extra_ld}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="logo" href="./">Casas em <span>Pipa</span></a>
  <nav class="menu" aria-label="Menu principal">
    {''.join(f'<a href="{c["slug"]}.html">{c["nome"]}</a>' for c in CASAS)}
    <a href="./#localizacao">Localização</a><a href="./#perguntas">Dúvidas</a>
  </nav>
  <a class="btn" href="{wa('Olá! Gostaria de saber a disponibilidade das casas em Pipa.')}" rel="nofollow">Reservar</a>
</div></header>
"""

def foot():
    return f"""
<footer><div class="wrap cols">
  <div><h4>{MARCA}</h4><p>Hospedagem em Pipa: casas de temporada no Condomínio Pipa Natureza, Praia da Pipa – Tibau do Sul/RN.</p></div>
  <div><h4>As casas</h4>{'<br>'.join(f'<a href="{c["slug"]}.html">{c["nome"]}</a> – até {c["hospedes"]} hóspedes' for c in CASAS)}</div>
  <div><h4>Contato</h4>
    WhatsApp: <a href="{wa('Olá! Vim pelo site das casas em Pipa.')}" rel="nofollow">{TELEFONE}</a><br>
    {f'E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>' if EMAIL else ''}
    Instagram: <a href="https://instagram.com/{INSTAGRAM}" rel="noopener">@{INSTAGRAM}</a><br>
    {ENDERECO['rua']}, {ENDERECO['bairro']} – {ENDERECO['cidade']}/{ENDERECO['uf']}</div>
</div></footer>
<a class="wa-float" href="{wa('Olá! Gostaria de reservar uma casa em Pipa.')}" rel="nofollow" aria-label="Falar no WhatsApp">{WA_SVG}<span>WhatsApp</span></a>
</body></html>
"""

def capa(c, cls=""):
    if c["fotos"]:
        f, alt = c["fotos"][0]
        return f'<img src="img/{f}.webp" alt="{e(alt)}" loading="lazy" width="800" height="600">'
    return f'<div class="placeholder ph-{c["cor"]}">{e(c["nome"])}<small>Fotos em breve</small></div>'

def facts(c):
    p = "Piscina · " if c["piscina"] else ""
    return (f'<ul class="facts"><li>Até {c["hospedes"]} hóspedes</li><li>{c["quartos"]} quartos'
            f'{" (" + str(c["suites"]) + " suíte" + ("s" if c["suites"] > 1 else "") + ")" if c["suites"] else ""}</li>'
            f'<li>{c["banheiros"]} banheiros</li>{"<li>Piscina</li>" if c["piscina"] else ""}</ul>')

# ====== PÁGINA INICIAL ======
def pagina_inicial():
    title = "Hospedagem em Pipa – Casas com piscina para alugar na Praia da Pipa (RN)"
    desc = ("Casas de temporada para alugar em Pipa, RN: Casa Terracota, Casa Frida e Casa Azul no Condomínio "
            "Pipa Natureza. Piscina, 3 quartos, até 8 hóspedes. Reserve direto com o anfitrião pelo WhatsApp.")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": f"{DOMINIO}/#site", "url": f"{DOMINIO}/", "name": MARCA, "inLanguage": "pt-BR"},
        {"@type": "LodgingBusiness", "@id": f"{DOMINIO}/#negocio", "name": MARCA,
         "description": desc, "url": f"{DOMINIO}/", "telephone": TELEFONE, **({"email": EMAIL} if EMAIL else {}),
         "image": f"{DOMINIO}/img/og-casas-pipa.jpg", "address": endereco_ld(), "priceRange": "$$",
         "checkinTime": CHECKIN, "checkoutTime": CHECKOUT,
         "areaServed": "Praia da Pipa, Tibau do Sul, RN",
         "sameAs": [f"https://instagram.com/{INSTAGRAM}"],
         "makesOffer": [{"@type": "Offer", "itemOffered": {"@id": f"{DOMINIO}/{c['slug']}.html#casa"}} for c in CASAS]},
        *[casa_ld(c) for c in CASAS],
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
    ]}
    cards = "".join(f"""
    <article class="card">
      <a class="ph" href="{c['slug']}.html">{capa(c)}</a>
      <div class="body">
        <h3><a href="{c['slug']}.html" style="color:inherit;text-decoration:none">{c['nome']}</a></h3>
        {facts(c)}
        <p>{e(c['resumo'])}</p>
        <a class="btn ghost" href="{c['slug']}.html">Ver a {c['nome']}</a>
      </div>
    </article>""" for c in CASAS)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    return head(title, desc, "", extra_ld=jsonld(ld)) + f"""
<main>
<section class="hero" aria-label="Apresentação">
  <img src="img/terracota-piscina.webp" alt="Casa com piscina para alugar na Praia da Pipa, RN" width="788" height="525" fetchpriority="high">
  <div class="wrap">
    <h1>Hospedagem em Pipa com piscina e privacidade</h1>
    <p>Três casas de temporada no Condomínio Pipa Natureza, entre a mata atlântica e a Praia do Madeiro. Reserve direto com o anfitrião, sem taxas de plataforma.</p>
    <a class="btn" href="{wa('Olá! Gostaria de saber a disponibilidade das casas em Pipa.')}" rel="nofollow">{WA_SVG} Consultar datas</a>
  </div>
</section>

<section id="casas"><div class="wrap">
  <h2>Casas para alugar em Pipa</h2>
  <p class="lead">Escolha a casa ideal para sua viagem. Todas ficam lado a lado no mesmo condomínio — ótimo também para grupos grandes que queiram alugar mais de uma casa.</p>
  <div class="cards">{cards}</div>
</div></section>

<section class="alt" id="localizacao"><div class="wrap grid2">
  <div>
    <h2>Pipa Natureza: tranquilidade perto de tudo</h2>
    <p>O Condomínio Pipa Natureza fica na Praia da Pipa, em Tibau do Sul (RN), cercado de verde e a poucos minutos de carro do centro de Pipa, com seus restaurantes, bares e lojinhas.</p>
    <ul class="check">
      <li>Trilha de ~20 minutos até a Praia do Madeiro</li>
      <li>Perto da Baía dos Golfinhos e da Praia do Amor</li>
      <li>~1h30 (95 km) do Aeroporto Internacional de Natal</li>
      <li>Pôr do sol na Lagoa de Guaraíras, em Tibau do Sul</li>
    </ul>
  </div>
  <img src="img/terracota-fachada.webp" alt="Casa de temporada no Condomínio Pipa Natureza, Pipa RN" loading="lazy" width="788" height="525">
</div></section>

<section><div class="wrap grid2">
  <img src="img/terracota-varanda-gourmet.webp" alt="Varanda gourmet de casa de temporada em Pipa" loading="lazy" width="1050" height="1400" style="aspect-ratio:4/3">
  <div>
    <h2>Por que reservar direto?</h2>
    <ul class="check">
      <li>Atendimento direto com o anfitrião, {ANFITRIAO}</li>
      <li>Sem taxa de serviço de plataforma</li>
      <li>Contrato de locação por temporada</li>
      <li>Casas entregues limpas, com roupa de cama e banho</li>
      <li>Dicas de passeios, restaurantes e transfer</li>
    </ul>
    <p><a class="btn" href="{wa('Olá! Gostaria de fazer uma reserva em Pipa.')}" rel="nofollow">Falar no WhatsApp</a></p>
  </div>
</div></section>

<section class="alt" id="perguntas"><div class="wrap">
  <h2>Perguntas frequentes</h2>
  <p class="lead">Tudo o que você precisa saber antes de reservar sua hospedagem em Pipa.</p>
  {faq}
</div></section>
</main>
""" + foot()

# ====== PÁGINA DE CADA CASA ======
def pagina_casa(c):
    others = [o for o in CASAS if o is not c]
    bc = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{DOMINIO}/"},
        {"@type": "ListItem", "position": 2, "name": c["nome"], "item": f"{DOMINIO}/{c['slug']}.html"}]}
    ld = {"@context": "https://schema.org", "@graph": [casa_ld(c), bc]}
    og = f"img/{c['fotos'][0][0]}.webp" if c["fotos"] else "img/og-casas-pipa.jpg"
    if c["fotos"]:
        gal = '<div class="gallery">' + "".join(
            f'<a href="img/{f}.webp"><img src="img/{f}.webp" alt="{e(alt)}" loading="{"eager" if i == 0 else "lazy"}"></a>'
            for i, (f, alt) in enumerate(c["fotos"])) + "</div>"
    else:
        gal = f'<div class="card" style="aspect-ratio:16/7">{capa(c)}</div>'
    texto = "".join(f"<p>{e(p)}</p>" for p in c["texto"])
    amen = "".join(f"<li>{e(a)}</li>" for a in c["comodidades"])
    msg = f"Olá! Gostaria de saber a disponibilidade da {c['nome']} em Pipa."
    outras = "".join(f"""
    <article class="card"><a class="ph" href="{o['slug']}.html">{capa(o)}</a>
      <div class="body"><h3>{o['nome']}</h3>{facts(o)}<a class="btn ghost" href="{o['slug']}.html">Ver a {o['nome']}</a></div></article>""" for o in others)
    return head(c["titulo_seo"], c["descricao_seo"], f"{c['slug']}.html", og_img=og, extra_ld=jsonld(ld)) + f"""
<main class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="./">Início</a> › {c['nome']}</nav>
  <div class="page-head">
    <h1>{e(c['titulo_seo'])}</h1>
    <p class="lead" style="margin-bottom:16px">{e(c['resumo'])}</p>
  </div>
  {gal}
  <div class="specs">
    <div class="spec"><b>{c['hospedes']}</b><span>hóspedes</span></div>
    <div class="spec"><b>{c['quartos']}</b><span>quartos{f" ({c['suites']} suíte{'s' if c['suites'] > 1 else ''})" if c['suites'] else ''}</span></div>
    <div class="spec"><b>{c['banheiros']}</b><span>banheiros</span></div>
    <div class="spec"><b>{'Sim' if c['piscina'] else '—'}</b><span>piscina</span></div>
  </div>
  <section style="padding-top:16px" class="grid2">
    <div><h2>Sobre a {c['nome']}</h2>{texto}<p><strong>Camas:</strong> {e(c['camas'])}.</p>
      <p><a class="btn" href="{wa(msg)}" rel="nofollow">{WA_SVG} Consultar disponibilidade</a></p></div>
    <div><h2>Comodidades</h2><ul class="check">{amen}</ul>
      <p style="color:var(--muted)">Check-in a partir das {CHECKIN[:2]}h · Check-out até {CHECKOUT[:2]}h<br>
      {ENDERECO['rua']}, Casa {c['numero']} – {ENDERECO['bairro']}, {ENDERECO['cidade']}/{ENDERECO['uf']}</p></div>
  </section>
  <section style="padding-top:0"><h2>Outras casas em Pipa</h2><div class="cards">{outras}</div></section>
</main>
""" + foot()

def favicon():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#c4552f"/><path d="M14 34 32 18l18 16v14H14z" fill="#fbf7f2"/><rect x="27" y="36" width="10" height="12" fill="#c4552f"/></svg>'

def sitemap():
    urls = [("", "1.0")] + [(f"{c['slug']}.html", "0.8") for c in CASAS]
    body = "".join(f"<url><loc>{DOMINIO}/{u}</loc><lastmod>{HOJE}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    files = {"index.html": pagina_inicial(), "favicon.svg": favicon(), "sitemap.xml": sitemap(),
             "robots.txt": f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n"}
    for c in CASAS:
        files[f"{c['slug']}.html"] = pagina_casa(c)
    for name, content in files.items():
        with open(os.path.join(here, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        print("ok", name)
