# Site – Casas em Pipa

## Como editar
Todos os textos, comodidades, fotos e contatos estão em `_gerar_site.py`.
Depois de editar, rode `python _gerar_site.py` nesta pasta para recriar as páginas.

- **Domínio**: troque `DOMINIO` no topo do arquivo antes de publicar (é usado no sitemap e nas tags do Google).
- **Fotos da Casa Frida e Casa Azul**: coloque as fotos em `img/` (formato .webp ou .jpg) e liste-as em `"fotos"` da casa, como na Terracota.

## Como publicar (grátis)
1. Crie uma conta em https://app.netlify.com e arraste a pasta `SITE` para a área "Deploy manually".
2. (Opcional, ~R$ 40/ano) Registre um domínio em https://registro.br e conecte no Netlify (Domain settings).

## Como aparecer no Google
1. **Google Search Console** (https://search.google.com/search-console): adicione o domínio, verifique e envie `sitemap.xml` em "Sitemaps".
2. **Perfil da Empresa no Google** (https://business.google.com): crie o perfil como "Casa de temporada" ou "Pousada", com endereço no Condomínio Pipa Natureza, fotos, WhatsApp e o link do site. É o que faz aparecer no Google Maps.
3. Peça aos hóspedes avaliações no Perfil da Empresa e coloque o link do site na bio do Instagram e nos anúncios.
4. Teste os dados estruturados em https://search.google.com/test/rich-results.
