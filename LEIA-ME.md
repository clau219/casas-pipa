# Site – Casas em Pipa

No ar em: https://clau219.github.io/casas-pipa/ (GitHub Pages, repositório clau219/casas-pipa)

## Como editar
Todos os textos, comodidades, fotos e contatos estão em `_gerar_site.py`.
Depois de editar, rode `python _gerar_site.py` nesta pasta para recriar as páginas e publique com:

    git add -A
    git commit -m "Atualiza site"
    git push

O GitHub Pages atualiza o site em 1–2 minutos.

- **E-mail no site**: fica de fora por padrão. Para mostrar, defina a variável `SITE_EMAIL` antes de rodar o gerador.
- **Fotos**: ficam em `img/` (.webp) e são listadas em `"fotos"` de cada casa. A primeira é a capa.
  As fotos da Azul e da Frida foram copiadas dos anúncios do Airbnb em 18/11/2026.

## Domínio próprio (casasempipa.com.br)
1. Registre o domínio em https://registro.br (~R$ 40/ano).
2. No registro.br, em DNS, crie:
   - `www` tipo CNAME → `clau219.github.io`
   - registros A para o domínio sem www → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
3. Troque `DOMINIO` em `_gerar_site.py` para `https://www.casasempipa.com.br`, crie o arquivo `CNAME` com
   `www.casasempipa.com.br`, rode o gerador e faça o push.
4. No GitHub (Settings > Pages) marque "Enforce HTTPS".

## Como aparecer no Google
1. **Google Search Console** (https://search.google.com/search-console): adicione a propriedade
   (prefixo de URL `https://clau219.github.io/casas-pipa/`, ou o domínio próprio depois), verifique
   (método "Arquivo HTML": baixe o arquivo, coloque nesta pasta e faça push) e envie `sitemap.xml` em "Sitemaps".
   Use também "Inspeção de URL" > "Solicitar indexação" na página inicial e nas 3 casas.
2. **Perfil da Empresa no Google** (https://business.google.com): crie o perfil como "Casa de temporada",
   com endereço no Condomínio Pipa Natureza, fotos, WhatsApp e o link do site. É o que faz aparecer no Google Maps.
3. Peça aos hóspedes avaliações no Perfil da Empresa e coloque o link do site na bio do Instagram e nos anúncios.
4. Teste os dados estruturados em https://search.google.com/test/rich-results.
