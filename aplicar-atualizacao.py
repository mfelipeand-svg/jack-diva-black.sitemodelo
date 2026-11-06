from pathlib import Path

path = Path('index.html')
if not path.exists():
    raise SystemExit('index.html não encontrado. Execute na raiz do projeto Jack Diva Black.')
html = path.read_text(encoding='utf-8')

old_hero = '<img src="assets/hero-turbante.webp" alt="Imagem ilustrativa de mulher usando turbante estampado e acessórios afro">'
new_hero = '<img src="assets/jack-turbante-vermelho.webp" alt="Jack Diva Black usando turbante vermelho e acessórios">'
if old_hero in html:
    html = html.replace(old_hero, new_hero, 1)
elif 'assets/jack-turbante-vermelho.webp' not in html:
    raise SystemExit('Não encontrei a imagem do banner esperada. Nenhuma alteração aplicada.')

# Navegação para a nova seção de produtos.
nav_old = '<a href="#colecoes">Coleções</a><a href="#historia">Nossa essência</a>'
nav_new = '<a href="#colecoes">Coleções</a><a href="#leques">Leques africanos</a><a href="#historia">Nossa essência</a>'
html = html.replace(nav_old, nav_new, 1)

# Corrige o texto da área de coleções: as imagens ilustrativas continuam identificadas,
# enquanto as novas fotos reais aparecem em seções próprias.
html = html.replace(
    'Conheça algumas das expressões da Jack Diva Black. As imagens desta demonstração são ilustrativas e serão substituídas pelas fotografias oficiais da marca.',
    'Conheça algumas das expressões da Jack Diva Black. Explore também os produtos reais apresentados pela marca.'
)

extra_css = '''
.jack-gallery{background:#fff4df}
.jack-gallery-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px}
.jack-gallery-card{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:0 10px 28px #29140d12}
.jack-gallery-card img{width:100%;aspect-ratio:4/5;object-fit:cover;object-position:center 28%}
.jack-gallery-card figcaption{padding:12px 10px;text-align:center;color:var(--brown);font:18px Georgia,serif}
.jack-gallery-note{text-align:center;color:var(--muted);font-size:12px;margin:20px auto 0}
.product-section{background:#fffaf0}
.product-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:17px}
.product-card{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 12px 32px #29140d12}
.product-card img{width:100%;aspect-ratio:4/5;object-fit:cover;background:#171313}
.product-info{padding:16px}
.product-info h3{font:22px Georgia,serif;color:var(--brown);margin:0 0 5px}
.product-info p{font-size:12px;color:var(--muted);margin:0 0 10px}
.product-price{font-size:20px;font-weight:900;color:var(--red);margin-bottom:13px}
.product-action{display:inline-flex;background:var(--black);color:white;padding:10px 13px;border-radius:6px;font-size:12px;font-weight:850}
@media(max-width:850px){.jack-gallery-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.product-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:520px){.jack-gallery-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.jack-gallery-card figcaption{font-size:16px}.product-grid{gap:12px}.product-info{padding:12px}.product-info h3{font-size:19px}}
'''
if '.product-grid{' not in html:
    marker = '</style>'
    if marker not in html:
        raise SystemExit('Bloco de estilos não encontrado. Nenhuma alteração aplicada.')
    html = html.replace(marker, extra_css + '\n' + marker, 1)

gallery_html = '''
<section class="section jack-gallery" id="turbantes">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Fotos reais da marca</div>
      <h2>Um turbante, muitas formas de expressão.</h2>
      <p>Conheça alguns dos looks apresentados pela Jack Diva Black. Cada amarração valoriza a beleza, a cor e a personalidade de quem usa.</p>
    </div>
    <div class="jack-gallery-grid">
      <figure class="jack-gallery-card"><img src="assets/jack-turbante-vermelho.webp" alt="Jack usando turbante vermelho e brincos dourados" loading="lazy"><figcaption>Turbante vermelho</figcaption></figure>
      <figure class="jack-gallery-card"><img src="assets/jack-turbante-preto.webp" alt="Jack usando turbante preto e acessórios" loading="lazy"><figcaption>Turbante preto</figcaption></figure>
      <figure class="jack-gallery-card"><img src="assets/jack-turbante-amarelo.webp" alt="Jack usando turbante amarelo com laço" loading="lazy"><figcaption>Turbante amarelo</figcaption></figure>
      <figure class="jack-gallery-card"><img src="assets/jack-turbante-azul.webp" alt="Jack usando turbante azul e brinco azul" loading="lazy"><figcaption>Turbante azul</figcaption></figure>
      <figure class="jack-gallery-card"><img src="assets/jack-turbante-pink.webp" alt="Jack usando turbante pink" loading="lazy"><figcaption>Turbante pink</figcaption></figure>
    </div>
    <p class="jack-gallery-note">Fotografias reais fornecidas pela marca.</p>
  </div>
</section>
'''
if 'id="turbantes"' not in html:
    marker = '<section class="section story" id="historia">'
    if marker not in html:
        raise SystemExit('Seção Nossa essência não encontrada. Nenhuma alteração aplicada.')
    html = html.replace(marker, gallery_html + '\n' + marker, 1)

product_html = '''
<section class="section product-section" id="leques">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Peças da marca</div>
      <h2>Leque Africano</h2>
      <p>Confeccionado em tecido Ankara africano com acabamento em couro. Escolha a estampa que combina com você e consulte a disponibilidade diretamente com a Jack Diva Black.</p>
    </div>
    <div class="product-grid">
      <article class="product-card"><img src="assets/leque-africano-1.webp" alt="Leque Africano em tecido Ankara com estampa azul e branca" loading="lazy"><div class="product-info"><h3>Leque Africano</h3><p>Estampa azul e branca · acabamento em couro</p><div class="product-price">R$ 75,00</div><a class="product-action" href="https://linktr.ee/Jackdivablack" target="_blank" rel="noopener">Consultar / pedir ↗</a></div></article>
      <article class="product-card"><img src="assets/leque-africano-2.webp" alt="Leque Africano em tecido Ankara multicolorido" loading="lazy"><div class="product-info"><h3>Leque Africano</h3><p>Estampa multicolorida · acabamento em couro</p><div class="product-price">R$ 75,00</div><a class="product-action" href="https://linktr.ee/Jackdivablack" target="_blank" rel="noopener">Consultar / pedir ↗</a></div></article>
      <article class="product-card"><img src="assets/leque-africano-3.webp" alt="Leque Africano em tecido Ankara azul, amarelo e vinho" loading="lazy"><div class="product-info"><h3>Leque Africano</h3><p>Estampa azul, amarelo e vinho · acabamento em couro</p><div class="product-price">R$ 75,00</div><a class="product-action" href="https://linktr.ee/Jackdivablack" target="_blank" rel="noopener">Consultar / pedir ↗</a></div></article>
      <article class="product-card"><img src="assets/leque-africano-4.webp" alt="Leque Africano em tecido Ankara amarelo e azul" loading="lazy"><div class="product-info"><h3>Leque Africano</h3><p>Estampa amarela e azul · acabamento em couro</p><div class="product-price">R$ 75,00</div><a class="product-action" href="https://linktr.ee/Jackdivablack" target="_blank" rel="noopener">Consultar / pedir ↗</a></div></article>
    </div>
    <p class="jack-gallery-note">Preço informado pela marca: R$ 75,00. Confirme disponibilidade e condições diretamente com a empresa.</p>
  </div>
</section>
'''
if 'id="leques"' not in html:
    marker = '<section class="section story" id="historia">'
    html = html.replace(marker, product_html + '\n' + marker, 1)

# Mantém as seções ilustrativas identificadas para não sugerir estoque inexistente.
html = html.replace(
    'Demonstração visual: fotos ilustrativas, não representam necessariamente produtos disponíveis, preços ou estoque.',
    'As imagens desta seção são referências ilustrativas. Consulte a marca para conhecer os produtos disponíveis.'
)

path.write_text(html, encoding='utf-8')
print('Atualização aplicada: banner, galeria real de turbantes e seção Leque Africano.')
