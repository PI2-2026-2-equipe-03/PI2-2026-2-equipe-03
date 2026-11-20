// repeteco: manifesto em motion graphics (HyperFrames + studio.js, um relógio só).
// Mesmo t entrando, mesma imagem saindo: nada de Math.random, Date.now ou timers.
// Modos (data-mode no #root): "manifesto" (cenas 1-6) ou "vinheta" (só o logo).
(function () {
  const S = STUDIO, M = window.MARCA, C = M.C;
  const root = S.root, W = S.W, H = S.H, V = S.V;
  const MODE = root.dataset.mode || 'manifesto';
  const SQ = W === H; // 1:1
  const OFF = MODE === 'vinheta' ? 21.35 : 0; // a vinheta começa direto na cena do logo
  const NS = 'http://www.w3.org/2000/svg';

  // ---------- layout por formato ----------
  const L = V
    ? { m: 80, hTop: 210, hSize: 96, hMax: 920, sub: 42, subTop: 0, sand: 1690, amp: 30 }
    : SQ
      ? { m: 80, hTop: 110, hSize: 78, hMax: 920, sub: 34, subTop: 0, sand: 930, amp: 22 }
      : { m: 120, hTop: 120, hSize: 92, hMax: 1500, sub: 36, subTop: 0, sand: 955, amp: 22 };

  // ---------- helpers ----------
  const el = (tag, cls, parent, css) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (css) Object.assign(e.style, css);
    (parent || root).appendChild(e);
    return e;
  };
  const sv = (tag, attrs, parent) => {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  };
  const seg = (t, a, d, e) => S.seg(t, a, d, e);
  const mix = S.mix;
  const bump = (t, a, up, down) => (t < a ? 0 : t < a + up ? seg(t, a, up, 'power2.out') : 1 - seg(t, a + up, down, 'power2.inOut'));

  // headline com palavras mascaradas (sobem por trás de uma borda)
  function headline(parent, parts, opt) {
    const box = el('div', 'hl', parent, {
      left: (opt.x ?? L.m) + 'px', top: (opt.y ?? L.hTop) + 'px', fontSize: (opt.size || L.hSize) + 'px',
      width: (opt.max || L.hMax) + 'px', textAlign: opt.align || 'left',
    });
    const words = [];
    parts.forEach(([txt, color]) => {
      txt.split(' ').filter(Boolean).forEach((w) => {
        const o = el('span', 'w', box); const i = el('span', 'wi', o); i.textContent = w;
        if (color) i.style.color = color;
        box.appendChild(document.createTextNode(' '));
        words.push(i);
      });
    });
    return { box, words };
  }
  function reveal(h, t, start, stagger = 0.06, dur = 0.6) {
    h.words.forEach((w, i) => {
      const p = seg(t, start + i * stagger, dur, 'power3.out');
      w.style.transform = `translateY(${(1 - p) * 112}%)`;
    });
  }
  function sub(parent, lines, x, y, size, align) {
    const b = el('div', 'sub', parent, { left: x + 'px', top: y + 'px', fontSize: size + 'px', textAlign: align || 'left' });
    b.innerHTML = lines.map((l) => `<div class="sl"><span>${l}</span></div>`).join('');
    return { box: b, lines: [...b.querySelectorAll('.sl span')] };
  }
  function revealSub(s, t, start) {
    s.lines.forEach((l, i) => {
      const p = seg(t, start + i * 0.1, 0.55, 'power3.out');
      l.style.transform = `translateY(${(1 - p) * 110}%)`;
    });
  }
  function scene(a, b) {
    const d = el('div', 'scene', root);
    return { d, a, b, on: (t) => t >= a && t < b };
  }
  // saída comum: sobe e some, mais curta que a entrada
  function exitT(t, at) { return seg(t, at, 0.38, 'power2.in'); }

  // ---------- areia (sempre no quadro) ----------
  const sandSvg = sv('svg', { class: 'sand', viewBox: `0 0 ${W} ${H}`, width: W, height: H });
  root.appendChild(sandSvg);
  const sandA = sv('path', { fill: C.yel }, sandSvg);
  const sandB = sv('path', { fill: C.yelDk }, sandSvg);
  function wave(y0, amp, ph, seed, k) {
    let d = `M0,${H} `;
    const N = 32, pts = [];
    for (let i = 0; i <= N; i++) {
      const u = i / N;
      const y = y0 + amp * (0.55 * Math.sin(2 * Math.PI * (k[0] * u + ph)) + 0.3 * Math.sin(2 * Math.PI * (k[1] * u + ph * 1.7 + seed)) + 0.15 * Math.sin(2 * Math.PI * (k[2] * u + seed * 0.3)));
      pts.push([W * u, y]);
    }
    d += `L${pts[0][0]},${pts[0][1].toFixed(1)} `;
    for (let i = 0; i < N; i++) {
      const p0 = pts[Math.max(i - 1, 0)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(i + 2, N)];
      d += `C${(p1[0] + (p2[0] - p0[0]) / 6).toFixed(1)},${(p1[1] + (p2[1] - p0[1]) / 6).toFixed(1)} ${(p2[0] - (p3[0] - p1[0]) / 6).toFixed(1)},${(p2[1] - (p3[1] - p1[1]) / 6).toFixed(1)} ${p2[0].toFixed(1)},${p2[1].toFixed(1)} `;
    }
    return d + `L${W},${H} Z`;
  }

  // ================= CENA 1: o lance =================
  const s1 = scene(0, 4.6);
  const h1 = headline(s1.d, [['Aquele lance'], ['absurdo', C.yel], ['na areia…']], {});
  // quadra vista da lateral, em leve perspectiva: a rede atravessa a quadra "para dentro" da tela,
  // então aparece de quina (poste da frente maior, poste do fundo menor e mais alto). A bola vem
  // da esquerda, passa por cima da fita e cai do outro lado.
  const net = { cx: W / 2, top: V ? 1180 : SQ ? 590 : 580 };
  const nearX = net.cx - (V ? 62 : SQ ? 66 : 84), farX = net.cx + (V ? 62 : SQ ? 66 : 84);
  const nearFoot = L.sand + (V ? 84 : 66), farFoot = L.sand - 8;
  const nearTop = net.top, farTop = farFoot - (nearFoot - nearTop) * 0.66;
  const BAND = 0.34; // a malha ocupa o terço de cima, como na rede de vôlei de praia
  const lerp = (p, q, u) => p + (q - p) * u;
  const netTop = (u) => [lerp(nearX, farX, u), lerp(nearTop + 10, farTop + 7, u)];
  const netBot = (u) => [lerp(nearX, farX, u), lerp(nearTop + BAND * (nearFoot - nearTop), farTop + BAND * (farFoot - farTop), u)];
  const s1svg = sv('svg', { class: 'layer', viewBox: `0 0 ${W} ${H}`, width: W, height: H });
  s1.d.appendChild(s1svg);
  const netG = sv('g', {}, s1svg);
  // poste do fundo (mais apagado, dá profundidade)
  sv('rect', { x: farX - 5, y: farTop - 4, width: 10, height: farFoot - farTop + 4, fill: C.lilac, rx: 4 }, netG);
  sv('ellipse', { cx: farX, cy: farFoot, rx: 20, ry: 6, fill: C.yelDk }, netG);
  // malha
  const q = [netTop(0), netTop(1), netBot(1), netBot(0)];
  sv('polygon', { points: q.map((p) => p.map((v) => v.toFixed(1)).join(',')).join(' '), fill: '#fff', opacity: 0.1 }, netG);
  for (let i = 1; i < 9; i++) {
    const u = i / 9, [x1, y1] = netTop(u), [, y2] = netBot(u);
    sv('line', { x1, y1, x2: x1, y2, stroke: '#fff', 'stroke-width': 2, opacity: 0.6 }, netG);
  }
  for (let j = 1; j < 4; j++) {
    const k = j / 4, a0 = netTop(0), b0 = netBot(0), a1 = netTop(1), b1 = netBot(1);
    sv('line', { x1: a0[0], y1: lerp(a0[1], b0[1], k), x2: a1[0], y2: lerp(a1[1], b1[1], k), stroke: '#fff', 'stroke-width': 2, opacity: 0.6 }, netG);
  }
  sv('line', { x1: q[3][0], y1: q[3][1], x2: q[2][0], y2: q[2][1], stroke: '#fff', 'stroke-width': 4, 'stroke-linecap': 'round' }, netG);
  sv('line', { x1: q[0][0], y1: q[0][1], x2: q[1][0], y2: q[1][1], stroke: '#fff', 'stroke-width': 9, 'stroke-linecap': 'round' }, netG);
  // antenas listradas nas laterais da quadra
  [[0.08, V ? 96 : 84], [0.92, V ? 72 : 62]].forEach(([u, hh]) => {
    const [ax, ay] = netTop(u), [, by] = netBot(u);
    sv('line', { x1: ax, y1: by, x2: ax, y2: ay - hh, stroke: '#fff', 'stroke-width': 6, 'stroke-linecap': 'round' }, netG);
    sv('line', { x1: ax, y1: ay, x2: ax, y2: ay - hh, stroke: C.yel, 'stroke-width': 6, 'stroke-dasharray': '12 12' }, netG);
  });
  // poste da frente, por cima da ponta da rede
  sv('rect', { x: nearX - 7, y: nearTop - 4, width: 14, height: nearFoot - nearTop + 4, fill: '#fff', rx: 5 }, netG);
  sv('ellipse', { cx: nearX, cy: nearFoot, rx: 30, ry: 8, fill: C.yelDk }, netG);
  const BR = V ? 30 : 26;
  const ghosts = [];
  for (let k = 6; k >= 1; k--) ghosts.push(sv('circle', { r: BR * (1 - k * 0.07), fill: '#fff', opacity: 0 }, s1svg));
  const ballG = sv('g', {}, s1svg);
  sv('circle', { r: BR, fill: '#fff' }, ballG);
  sv('path', { d: `M${-BR},${-BR * 0.15} C${-BR * 0.3},${-BR * 0.4} ${BR * 0.3},${BR * 0.1} ${BR * 0.2},${BR}`, fill: 'none', stroke: C.blue, 'stroke-width': BR * 0.16, 'stroke-linecap': 'round' }, ballG);
  sv('path', { d: `M${-BR * 0.4},${-BR * 0.92} C${BR * 0.2},${-BR * 0.5} ${BR * 0.6},${-BR * 0.4} ${BR},${-BR * 0.05}`, fill: 'none', stroke: C.blue, 'stroke-width': BR * 0.16, 'stroke-linecap': 'round' }, ballG);
  const puffs = [];
  for (let i = 0; i < 7; i++) puffs.push(sv('circle', { r: 8, fill: C.yel, opacity: 0 }, s1svg));
  const span = V ? 400 : SQ ? 400 : 560;
  const groundY = L.sand + 6 - BR * 0.55; // a bola afunda um pouco na areia ao cair
  const P0 = [-BR * 3, nearTop + (V ? 60 : 40)], P2 = [net.cx + span * 0.82, groundY];
  const apex = net.top - (V ? 300 : 240);
  const CP = [net.cx - 40, 2 * apex - (P0[1] + P2[1]) / 2];
  const bez = (u) => [
    (1 - u) ** 2 * P0[0] + 2 * u * (1 - u) * CP[0] + u * u * P2[0],
    (1 - u) ** 2 * P0[1] + 2 * u * (1 - u) * CP[1] + u * u * P2[1],
  ];
  function scene1(t) {
    reveal(h1, t, 0.15);
    // "absurdo" pulsa quando a bola cai
    const ab = h1.words[2], pz = Math.sin(Math.PI * seg(t, 2.32, 0.55, 'sine.inOut'));
    if (t > 0.5) ab.style.transform = `translateY(0) scale(${(1 + 0.04 * pz).toFixed(3)}) rotate(${(-1.5 * pz).toFixed(2)}deg)`;
    ab.parentElement.style.overflow = t > 1.5 ? 'visible' : 'hidden';
    ab.style.display = 'inline-block'; ab.style.transformOrigin = '50% 70%';
    const fly = (tt) => seg(tt, 0.85, 1.45, 'none'); // u linear no tempo = parábola de verdade
    const u = fly(t);
    let [bx, by] = bez(u);
    // quique depois do pouso
    if (t > 2.3) { const q = t - 2.3; by -= Math.abs(Math.sin(q * 8)) * 38 * Math.exp(-q * 5); bx += 120 * seg(t, 2.3, 1.6, 'power2.out'); } // areia segura a bola
    ballG.setAttribute('transform', `translate(${bx.toFixed(1)},${by.toFixed(1)}) rotate(${(u * 540 + seg(t, 2.3, 1.6, 'power2.out') * 260).toFixed(1)})`);
    ghosts.forEach((g, i) => {
      const k = 6 - i; const uu = fly(t - k * 0.045); const [gx, gy] = bez(uu);
      const live = t > 0.9 && t < 2.35 ? 1 : 0;
      g.setAttribute('cx', gx.toFixed(1)); g.setAttribute('cy', gy.toFixed(1));
      g.setAttribute('opacity', (live * 0.32 * (1 - k / 7)).toFixed(3));
    });
    puffs.forEach((p, i) => {
      const a = -Math.PI * (0.12 + 0.76 * (i / 6)); const q = seg(t, 2.3, 0.6, 'power2.out');
      p.setAttribute('cx', (P2[0] + Math.cos(a) * 90 * q).toFixed(1));
      p.setAttribute('cy', (P2[1] + BR + Math.sin(a) * 60 * q).toFixed(1));
      p.setAttribute('r', (6 + 6 * (1 - q)).toFixed(1));
      p.setAttribute('opacity', t > 2.3 ? (1 - q).toFixed(2) : 0);
    });
    // o lance some da memória: tudo esmaece antes do corte
    const dim = seg(t, 2.95, 1.25, 'sine.inOut');
    s1.d.style.opacity = 1 - 0.62 * dim;
    s1.d.style.filter = dim > 0.001 ? `saturate(${1 - dim})` : 'none';
    const e = exitT(t, 4.25);
    h1.box.style.transform = `translateY(${-40 * e}px)`; h1.box.style.opacity = 1 - e;
    s1svg.style.opacity = 1 - e;
  }

  // ================= CENA 2: o problema =================
  const s2 = scene(4.6, 9.0);
  const h2 = headline(s2.d, [['…que ninguém conseguiu'], ['rever?', C.yel]], {});
  const sub2 = sub(s2.d, ['Hoje, o replay depende de alguém da arena:'], L.m, V ? 540 : SQ ? 330 : 300, L.sub);
  const chipsBox = el('div', 'chips', s2.d, { left: L.m + 'px', top: (V ? 680 : SQ ? 430 : 430) + 'px', flexDirection: V || SQ ? 'column' : 'row' });
  const chips = ['abrir as câmeras', 'achar o horário', 'mandar pro cliente'].map((txt, i) => {
    const c = el('div', 'chip', chipsBox, { fontSize: (V ? 46 : 40) + 'px' });
    c.innerHTML = `<b>${i + 1}</b><span>${txt}</span><i></i>`;
    return { c, strike: c.querySelector('i') };
  });
  const qmark = el('div', 'qmark', s2.d, V ? { left: '620px', top: '1080px', fontSize: '560px' } : SQ ? { left: '700px', top: '470px', fontSize: '420px' } : { left: '1540px', top: '230px', fontSize: '640px' });
  qmark.textContent = '?';
  function scene2(t) {
    reveal(h2, t, 4.68);
    revealSub(sub2, t, 5.3);
    chips.forEach((c, i) => {
      const p = seg(t, 5.75 + i * 0.16, 0.55, 'back.out(1.4)');
      const k = seg(t, 7.0 + i * 0.22, 0.42, 'power3.inOut');
      c.c.style.transform = `translateY(${(1 - p) * 40}px)`;
      c.c.style.opacity = p * (1 - 0.55 * k);
      c.strike.style.transform = `scaleX(${k})`;
    });
    const q = seg(t, 5.0, 0.9, 'power3.out');
    qmark.style.transform = `translateY(${(1 - q) * 120}px) rotate(${-8 + 6 * S.wave(t, 3)}deg)`;
    qmark.style.opacity = q;
    const e = exitT(t, 8.6);
    s2.d.style.transform = `translateY(${-40 * e}px)`; s2.d.style.opacity = 1 - e;
  }

  // ================= CENA 3: o botão =================
  const s3 = scene(9.0, 13.4);
  const h3 = headline(s3.d, [['Aperta o'], ['botão.', C.yel]], {});
  const sub3 = sub(s3.d, ['Instalado na própria quadra.', 'Um toque e o lance está salvo.'], L.m, V ? 400 : SQ ? 240 : 300, L.sub);
  const btn = { cx: V ? W / 2 : SQ ? 720 : 1390, top: V ? 920 : SQ ? 480 : 400, w: V ? 300 : 250, h: V ? 200 : 168 };
  const s3svg = sv('svg', { class: 'layer', viewBox: `0 0 ${W} ${H}`, width: W, height: H });
  s3.d.appendChild(s3svg);
  const rings = [0, 1, 2].map(() => sv('ellipse', { fill: 'none', stroke: C.yel, 'stroke-width': 5, opacity: 0 }, s3svg));
  const btnG = sv('g', {}, s3svg);
  sv('rect', { x: btn.cx - 22, y: btn.top + btn.h - 10, width: 44, height: L.sand - btn.top, fill: C.blueDeep }, btnG);
  sv('rect', { x: btn.cx - btn.w / 2, y: btn.top, width: btn.w, height: btn.h, rx: 38, fill: '#fff' }, btnG);
  const domeG = sv('g', {}, btnG);
  const dw = btn.w * 0.34, dy = btn.top + btn.h * 0.42;
  sv('path', { d: `M${btn.cx - dw},${dy} v26 a${dw},${dw * 0.32} 0 0 0 ${dw * 2},0 v-26 z`, fill: C.yelDk }, domeG);
  sv('ellipse', { cx: btn.cx, cy: dy, rx: dw, ry: dw * 0.32, fill: C.yel }, domeG);
  const clique = el('div', 'clique', s3.d, { left: btn.cx + btn.w * 0.28 + 'px', top: btn.top - 70 + 'px', fontSize: (V ? 64 : 52) + 'px' });
  clique.textContent = 'clique!';
  const saved = el('div', 'saved', s3.d, { left: L.m + 'px', top: (V ? 560 : SQ ? 380 : 470) + 'px', fontSize: (V ? 44 : 38) + 'px' });
  saved.innerHTML = '<b>✓</b><span>lance salvo</span>';
  const PRESS = 10.85;
  function scene3(t) {
    reveal(h3, t, 9.08);
    revealSub(sub3, t, 9.55);
    const rise = seg(t, 9.25, 0.85, 'power3.out');
    btnG.setAttribute('transform', `translate(0,${((1 - rise) * (L.sand - btn.top + 60) + 7 * S.wave(t, 9)).toFixed(1)})`);
    clique.style.marginTop = (6 * S.wave(t, 11, 0.3)).toFixed(1) + 'px';
    const pr = bump(t, PRESS, 0.07, 0.28);
    domeG.setAttribute('transform', `translate(0,${(pr * 16).toFixed(1)})`);
    rings.forEach((r, i) => {
      const q = seg(t, PRESS + 0.04 + i * 0.13, 0.95, 'power2.out');
      r.setAttribute('cx', btn.cx); r.setAttribute('cy', dy);
      r.setAttribute('rx', (dw + q * btn.w * 1.15).toFixed(1)); r.setAttribute('ry', ((dw + q * btn.w * 1.15) * 0.36).toFixed(1));
      r.setAttribute('opacity', t > PRESS ? (0.95 * (1 - q)).toFixed(2) : 0);
    });
    const c = seg(t, PRESS + 0.06, 0.45, 'back.out(2.2)');
    clique.style.transform = `rotate(-9deg) scale(${c})`; clique.style.opacity = c > 0 ? 1 : 0;
    const sv2 = seg(t, 11.7, 0.5, 'back.out(1.8)');
    saved.style.transform = `translateX(${(-60 * (1 - sv2)).toFixed(1)}px) scale(${(0.9 + 0.1 * sv2).toFixed(3)})`; saved.style.opacity = sv2;
    const kick = t >= PRESS ? Math.exp(-(t - PRESS) / 0.18) : 0;
    const e = exitT(t, 13.0);
    s3.d.style.transform = `translateY(${-40 * e}px) scale(${(1 + 0.035 * kick).toFixed(4)})`; s3.d.style.opacity = 1 - e;
  }

  // ================= CENA 4: 30 s viram clipe =================
  const s4 = scene(13.4, 17.4);
  const h4 = headline(s4.d, [['Os 30 segundos anteriores viram'], ['clipe.', C.yel]], { max: V ? 920 : SQ ? 920 : 1500 });
  const strip = { y: V ? 1000 : SQ ? 520 : 560, fw: V ? 58 : 64, fh: V ? 88 : 96, pitch: V ? 72 : 80, n: 30, ph: V ? 820 : SQ ? 760 : 1440, cap: 8 };
  const s4svg = sv('svg', { class: 'layer', viewBox: `0 0 ${W} ${H}`, width: W, height: H });
  s4.d.appendChild(s4svg);
  const stripG = sv('g', {}, s4svg);
  const frames = [];
  for (let i = 0; i < strip.n; i++) {
    const g = sv('g', {}, stripG);
    const r = sv('rect', { width: strip.fw, height: strip.fh, rx: 10, fill: '#3B5FC8' }, g);
    const sand = sv('rect', { y: strip.fh * 0.66, width: strip.fw, height: strip.fh * 0.34, rx: 0, fill: '#3B5FC8' }, g);
    frames.push({ g, r, sand });
  }
  const bracket = sv('g', { opacity: 0 }, s4svg);
  const brPath = sv('path', { fill: 'none', stroke: C.yel, 'stroke-width': 5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, bracket);
  const brText = sv('text', { 'text-anchor': 'middle', fill: C.yel, 'font-family': 'Bricolage Grotesque', 'font-weight': 800, 'font-size': V ? 48 : 44 }, bracket);
  brText.textContent = '30 s';
  const playhead = sv('g', {}, s4svg);
  sv('line', { x1: 0, y1: -strip.fh * 0.9, x2: 0, y2: strip.fh * 1.5, stroke: '#fff', 'stroke-width': 4, 'stroke-linecap': 'round' }, playhead);
  sv('circle', { cx: 0, cy: -strip.fh * 0.9, r: 11, fill: '#fff' }, playhead);
  const agora = sv('text', { x: 0, y: strip.fh * 1.5 + 44, 'text-anchor': 'middle', fill: C.lilac, 'font-family': 'Bricolage Grotesque', 'font-weight': 600, 'font-size': 30 }, playhead);
  agora.textContent = 'agora';
  const CAP = 14.75;
  function scene4(t) {
    reveal(h4, t, 13.48, 0.05);
    const appear = seg(t, 13.6, 0.6, 'power3.out');
    // a esteira de gravação anda e para no clique
    const travel = 6 * strip.pitch * seg(t, 13.4, CAP - 13.4 + 0.15, 'power2.out');
    const lastX = strip.ph - strip.fw / 2 - 6; // último quadro encosta na agulha
    frames.forEach((f, i) => {
      const fromEnd = strip.n - 1 - i;
      const x = lastX - fromEnd * strip.pitch + 6 * strip.pitch - travel;
      const captured = fromEnd < strip.cap;
      const k = captured ? seg(t, CAP + fromEnd * 0.05, 0.3, 'power2.out') : 0;
      const lift = captured ? -26 * seg(t, 15.75, 0.55, 'power3.out') : 0;
      f.g.setAttribute('transform', `translate(${(x - strip.fw / 2).toFixed(1)},${(strip.y - strip.fh / 2 + lift + (1 - appear) * 60).toFixed(1)})`);
      f.r.setAttribute('fill', k > 0.5 ? C.ice : '#3B5FC8');
      f.r.setAttribute('opacity', (0.55 + 0.45 * k).toFixed(2));
      f.sand.setAttribute('fill', k > 0.5 ? C.yel : '#3B5FC8');
      f.sand.setAttribute('opacity', (k > 0.5 ? 1 : 0).toString());
      f.g.setAttribute('opacity', appear.toFixed(2));
    });
    playhead.setAttribute('transform', `translate(${strip.ph},${strip.y - strip.fh / 2 + (1 - appear) * 60})`);
    playhead.setAttribute('opacity', appear.toFixed(2));
    const b = seg(t, 15.25, 0.45, 'power3.out');
    const x0 = lastX - (strip.cap - 1) * strip.pitch - strip.fw / 2, x1 = lastX + strip.fw / 2, by = strip.y - strip.fh / 2 - 34 - 26 * seg(t, 15.75, 0.55, 'power3.out');
    const xm = (x0 + x1) / 2, half = ((x1 - x0) / 2) * b;
    brPath.setAttribute('d', `M${xm - half},${by + 18} V${by} H${xm + half} V${by + 18}`);
    brText.setAttribute('x', xm); brText.setAttribute('y', by - 20);
    bracket.setAttribute('opacity', b > 0 ? 1 : 0);
    brText.setAttribute('opacity', seg(t, 15.45, 0.3).toFixed(2));
    const e = exitT(t, 16.98);
    s4.d.style.transform = `translateY(${-40 * e}px)`; s4.d.style.opacity = 1 - e;
  }

  // ================= CENA 5: no celular =================
  const s5 = scene(17.4, 21.6);
  const h5 = headline(s5.d, [['Direto no seu'], ['celular.', C.yel]], {});
  const sub5 = sub(s5.d, ['Sem pedir pra ninguém.', 'Download em segundos.'], L.m, V ? 400 : SQ ? 240 : 300, L.sub);
  const ph = V ? { cx: W / 2, w: 560, top: 640 } : SQ ? { cx: 780, w: 440, top: 380 } : { cx: 1390, w: 450, top: 150 };
  const phone = el('div', 'phone', s5.d, { left: ph.cx - ph.w / 2 + 'px', top: ph.top + 'px', width: ph.w + 'px', height: ph.w * 2 + 'px' });
  phone.innerHTML = `<div class="ph-title">Meus replays</div><div class="ph-sub">Arena · Quadra 2</div>` +
    ['19:42', '19:37', '19:21'].map((h, i) => `<div class="card"><div class="thumb"><s></s><u></u></div><div class="meta"><b>${h}</b><span>clipe · 0:30</span></div><div class="dl"><svg viewBox="0 0 52 52"><circle class="ring" cx="26" cy="26" r="23"/><path class="arr" d="M26 15v19M18 27l8 8 8-8"/><path class="chk" d="M16 27l7 7 13-14"/></svg></div></div>`).join('');
  const cards = [...phone.querySelectorAll('.card')];
  const dl = cards[0].querySelector('.dl'), ring = dl.querySelector('.ring'), arr = dl.querySelector('.arr'), chk = dl.querySelector('.chk');
  const RL = 2 * Math.PI * 23;
  ring.style.strokeDasharray = `${RL} ${RL}`;
  const toast = el('div', 'toast', s5.d, V ? { left: L.m + 'px', top: '540px' } : SQ ? { left: L.m + 'px', top: '400px' } : { left: L.m + 'px', top: '460px' });
  toast.innerHTML = '<b>✓</b><span>clipe salvo no celular</span>';
  const DL = 19.4;
  function scene5(t) {
    reveal(h5, t, 17.48);
    revealSub(sub5, t, 17.95);
    const up = seg(t, 17.6, 0.9, 'power3.out') - seg(t, 21.12, 0.42, 'power2.in');
    phone.style.transform = `translateY(${((1 - up) * (H - ph.top + 40) + 10 * S.wave(t, 8)).toFixed(1)}px) rotate(${(-3 * (1 - up) + 1.2 * S.wave(t, 6, 0.25)).toFixed(2)}deg)`;
    const ts = seg(t, DL + 0.85, 0.5, 'back.out(1.8)') - seg(t, 21.1, 0.3, 'power2.in');
    toast.style.transform = `translateY(${(30 * (1 - ts)).toFixed(1)}px) scale(${(0.85 + 0.15 * ts).toFixed(3)})`; toast.style.opacity = Math.max(0, ts);
    cards.forEach((c, i) => {
      const p = seg(t, 18.25 + i * 0.12, 0.55, 'power3.out');
      c.style.transform = `translateY(${(1 - p) * 40}px)`; c.style.opacity = p;
    });
    const prog = seg(t, DL, 0.7, 'power2.inOut');
    ring.style.strokeDashoffset = (RL * (1 - prog)).toFixed(1);
    const done = seg(t, DL + 0.72, 0.35, 'back.out(2)');
    dl.style.background = done > 0 ? C.yel : C.blue;
    dl.style.transform = `scale(${1 + 0.18 * bump(t, DL + 0.72, 0.12, 0.3)})`;
    arr.style.opacity = done > 0 ? 0 : 1;
    chk.style.opacity = done > 0 ? 1 : 0;
    chk.style.strokeDashoffset = (40 * (1 - done)).toFixed(1);
    cards[0].style.boxShadow = done > 0 ? `0 0 0 ${(4 * done).toFixed(1)}px ${C.yel}` : 'none';
    const e = exitT(t, 21.15);
    h5.box.style.transform = sub5.box.style.transform = `translateY(${-40 * e}px)`;
    h5.box.style.opacity = sub5.box.style.opacity = 1 - e;
  }

  // ================= CENA 6: logo =================
  const s6 = scene(21.6, 99);
  const s6svg = sv('svg', { class: 'layer', viewBox: `0 0 ${W} ${H}`, width: W, height: H });
  s6.d.appendChild(s6svg);
  const BBW = M.WORD_BB[2] - M.WORD_BB[0];
  const k = (V ? 700 : SQ ? 640 : 900) / BBW; // escala da palavra (tamanho 350 -> 350k)
  const eS = 1.25 * k;
  const lockW = 208 * eS + 95 * k + BBW * k;
  const baseY = V ? 960 : SQ ? 520 : 560;
  const left = (W - lockW) / 2;
  const eCx = left + 104 * eS, eCy = baseY - 92 * k;
  const wordX = eCx + 104 * eS + 95 * k - 12.6 * k;
  const eG = sv('g', {}, s6svg);
  const eInner = sv('g', {}, eG);
  const ePath = sv('path', { d: M.E_PATH, fill: 'none', stroke: C.yel, 'stroke-width': M.SW, 'stroke-linejoin': 'miter' }, eInner);
  const a = (M.END * Math.PI) / 180, ex = M.R * Math.cos(a), ey = M.R * Math.sin(a);
  const arrowG = sv('g', {}, eInner);
  sv('polygon', { points: M.E_ARROW.map((p) => p.join(',')).join(' '), fill: C.yel, stroke: C.yel, 'stroke-width': 7, 'stroke-linejoin': 'round' }, arrowG);
  ePath.setAttribute('stroke-dasharray', `${M.E_LEN} ${M.E_LEN + 10}`);
  const clip = sv('clipPath', { id: 'wclip' }, s6svg);
  const clipR = sv('rect', { x: wordX - 20, y: baseY - 420 * k, height: 700 * k, width: 0 }, clip);
  const wordG = sv('g', { 'clip-path': 'url(#wclip)' }, s6svg);
  const word = sv('path', { d: M.WORD, fill: '#fff' }, wordG);
  const tag = headline(s6.d, [['Esse lance merece'], ['repeteco.', C.yel]], { x: 0, y: baseY + (V ? 150 : SQ ? 120 : 130), size: V ? 60 : SQ ? 50 : 56, max: W, align: 'center' });
  const ul = el('div', 'ul', tag.box);
  function scene6(t) {
    const tt = t;
    const draw = seg(tt, 21.75, 0.85, 'power2.inOut');
    ePath.setAttribute('stroke-dashoffset', (M.E_LEN * (1 - draw)).toFixed(2));
    const ar = seg(tt, 22.5, 0.4, 'back.out(2.4)');
    arrowG.setAttribute('transform', `translate(${ex},${ey}) scale(${ar.toFixed(3)}) translate(${-ex},${-ey})`);
    // rebobina e vai para o lugar do lockup
    const rew = seg(tt, 22.75, 0.75, 'power3.inOut');
    const mv = seg(tt, 22.9, 0.8, 'expo.inOut');
    const big = 1.45;
    const cx = mix(W / 2, eCx, mv), cy = mix(H / 2 - (V ? 80 : 40), eCy, mv), sc = eS * mix(big, 1, mv);
    const rew2 = seg(tt, 25.2, 0.8, 'power3.inOut');
    const bob = 1 + 0.025 * Math.sin(Math.PI * seg(tt, 24.2, 1.2, 'sine.inOut')) + 0.05 * Math.sin(Math.PI * seg(tt, 26.2, 0.7, 'sine.inOut'));
    eG.setAttribute('transform', `translate(${cx.toFixed(1)},${cy.toFixed(1)}) rotate(${(-360 * (rew + rew2)).toFixed(1)}) scale(${(sc * bob).toFixed(4)})`);
    const wv = seg(tt, 23.35, 0.7, 'power3.out');
    clipR.setAttribute('width', (wv * (BBW * k + 80)).toFixed(1));
    word.setAttribute('transform', `translate(${(wordX - 40 * (1 - wv)).toFixed(1)},${baseY}) scale(${k.toFixed(4)})`);
    reveal(tag, tt, 24.05, 0.07);
    // fechamento: sublinhado corre sob "repeteco." e o "e" acena
    const lw = tag.words[tag.words.length - 1].parentElement;
    const u = seg(tt, 25.75, 0.55, 'power3.inOut');
    ul.style.left = lw.offsetLeft + 'px'; ul.style.top = lw.offsetTop + lw.offsetHeight * 0.9 + 'px';
    ul.style.width = (lw.offsetWidth * 0.94 * u).toFixed(1) + 'px';
  }

  // ---------- socos: um ataque de luz que decai em 0,4 s ----------
  const flash = el('div', 'flash', root);
  const PUNCHES = [10.85, 14.75, 22.5];
  const punch = (t) => PUNCHES.reduce((acc, p) => acc + (t < p ? 0 : t < p + 0.1 ? seg(t, p, 0.1, 'power2.out') : t < p + 0.25 ? 1 : Math.exp(-(t - p - 0.25) / 0.3)), 0);

  // ---------- relógio único ----------
  const SCENES = [[s1, scene1], [s2, scene2], [s3, scene3], [s4, scene4], [s5, scene5], [s6, scene6]];
  S.play(function render(t0) {
    const t = t0 + OFF;
    // areia: deriva lenta e sobe um pouco no final
    const rise = seg(t, 24.0, 1.0, 'power3.inOut') * (V ? 70 : 40);
    const ph = 0.085 * t;
    const breathe = 1 + 0.18 * S.wave(t0, Math.max(1, Math.round(S.D / 4)));
    sandA.setAttribute('d', wave(L.sand - rise, L.amp * breathe, 0.1 + ph, 0.4, [1, 2.3, 0.6]));
    sandB.setAttribute('d', wave(L.sand - rise + L.amp * 1.3, L.amp * 0.7 * (2 - breathe), 0.55 - ph * 0.8, 1.3, [1.4, 0.8, 2.1]));
    flash.style.opacity = Math.min(0.18, 0.18 * punch(t)).toFixed(3);
    for (const [sc, fn] of SCENES) {
      const on = sc.on(t);
      sc.d.style.display = on ? 'block' : 'none';
      if (on) fn(t);
    }
  }, { loop: false });
})();
