// repeteco: motions do Teco (HyperFrames + studio.js, um relógio só).
// data-mode="apresenta": "Esse é o Teco" (15 s), em 9:16, 1:1 e 16:9.
// data-mode="loop": o Teco quica e rebobina (4 s, loop perfeito), 1:1.
// Mesmo t entrando, mesma imagem saindo: nada de Math.random, Date.now ou timers.
(function () {
  const S = STUDIO, M = window.MARCA, TC = window.TECO, C = M.C;
  const root = S.root, W = S.W, H = S.H, D = S.D;
  const MODE = root.dataset.mode || 'apresenta';
  const LOOP = MODE === 'loop';
  const V = H > W, SQ = W === H, WIDE = W > H;
  const NS = 'http://www.w3.org/2000/svg';
  const seg = S.seg, mix = S.mix;
  const TAU = Math.PI * 2;

  const sv = (tag, attrs, parent) => {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  };
  const el = (tag, cls, parent, css) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (css) Object.assign(e.style, css);
    (parent || root).appendChild(e);
    return e;
  };
  const html = (g, s) => { if (g._s !== s) { g.innerHTML = s; g._s = s; } };
  const bump = (t, a, up, hold, down) => (t < a ? 0 : t < a + up ? seg(t, a, up, 'power2.out') : t < a + up + hold ? 1 : 1 - seg(t, a + up + hold, down, 'power2.in'));

  // ---------- layout ----------
  // o palco (1080x1080, chão em y=900) é onde o Teco atua; o texto fica numa faixa à parte
  const L = LOOP
    ? { st: { x: 0, y: 40, s: 1 }, tx: null }
    : V ? { st: { x: -81, y: 430, s: 1.15 }, tx: { x: 80, y: 230, size: 104, w: 940 } }
      : SQ ? { st: { x: 76, y: 200, s: 0.86 }, tx: { x: 72, y: 74, size: 78, w: 940 } }
        : { st: { x: 840, y: 0, s: 1 }, tx: { x: 110, y: 540, size: 96, w: 720, mid: true } };
  const st = L.st;
  const FX = (x) => st.x + x * st.s, FY = (y) => st.y + y * st.s;
  const GROUND = FY(900);

  // ---------- fundo: raios + areia (tela toda) ----------
  const bg = sv('svg', { class: 'full', viewBox: `0 0 ${W} ${H}`, width: W, height: H }, root);
  bg.style.left = '0px'; bg.style.top = '0px';
  const raysG = sv('g', {}, bg);
  const RC = [FX(540), FY(700)];
  for (let i = 0; i < 20; i++) {
    const a0 = (i / 20) * TAU, a1 = ((i + 0.5) / 20) * TAU, R = 3200;
    sv('path', { d: `M0,0 L${(R * Math.cos(a0)).toFixed(0)},${(R * Math.sin(a0)).toFixed(0)} L${(R * Math.cos(a1)).toFixed(0)},${(R * Math.sin(a1)).toFixed(0)}Z`, fill: '#1646B4' }, raysG);
  }
  const sandA = sv('path', { fill: C.yel }, bg);
  const sandB = sv('path', { fill: C.yelDk }, bg);
  function wave(y0, amp, ph, seed, k) {
    const N = 32, pts = [];
    for (let i = 0; i <= N; i++) {
      const u = i / N;
      pts.push([W * u, y0 + amp * (0.55 * Math.sin(TAU * (k[0] * u + ph)) + 0.3 * Math.sin(TAU * (k[1] * u + ph * 2 + seed)) + 0.15 * Math.sin(TAU * (k[2] * u + seed * 0.3)))]);
    }
    let d = `M0,${H} L${pts[0][0]},${pts[0][1].toFixed(1)} `;
    for (let i = 0; i < N; i++) {
      const p0 = pts[Math.max(i - 1, 0)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(i + 2, N)];
      d += `C${(p1[0] + (p2[0] - p0[0]) / 6).toFixed(1)},${(p1[1] + (p2[1] - p0[1]) / 6).toFixed(1)} ${(p2[0] - (p3[0] - p1[0]) / 6).toFixed(1)},${(p2[1] - (p3[1] - p1[1]) / 6).toFixed(1)} ${p2[0].toFixed(1)},${p2[1].toFixed(1)} `;
    }
    return d + `L${W},${H} Z`;
  }

  // ---------- palco ----------
  const stage = sv('svg', { class: 'palco', viewBox: '0 0 1080 1080', width: 1080 * st.s, height: 1080 * st.s }, root);
  stage.style.left = st.x + 'px'; stage.style.top = st.y + 'px';
  const defs = sv('defs', {}, stage);
  sv('rect', { x: -2000, y: -3000, width: 5000, height: 3906 }, sv('clipPath', { id: 'acimaDoChao' }, defs));
  const netWrap = sv('g', { 'clip-path': 'url(#acimaDoChao)' }, stage); const netG = sv('g', {}, netWrap); netG.innerHTML = TC.rede;
  const btnWrap = sv('g', { 'clip-path': 'url(#acimaDoChao)' }, stage); const btnG = sv('g', {}, btnWrap); btnG.innerHTML = TC.botao;
  const rings = [0, 1].map(() => sv('ellipse', { cx: 850, cy: 721, rx: 80, ry: 24, fill: 'none', stroke: C.yel, 'stroke-width': 9, opacity: 0 }, stage));
  const clique = sv('text', { x: 0, y: 0, 'font-family': 'Bricolage Grotesque', 'font-weight': 800, 'font-size': 84, fill: C.yel, 'text-anchor': 'middle', opacity: 0 }, stage);
  clique.textContent = 'clique!';
  const ghosts = [];
  for (let k = 5; k >= 1; k--) ghosts.push(sv('circle', { r: 120 * (1 - k * 0.08), fill: C.yel, opacity: 0 }, stage));
  const puffs = [];
  for (let i = 0; i < 8; i++) puffs.push(sv('circle', { r: 10, fill: C.yel, stroke: C.blueDeep, 'stroke-width': 4, opacity: 0 }, stage));
  const shadow = sv('ellipse', { cx: 540, cy: 904, rx: 108, ry: 18, fill: C.blueDeep, opacity: 0.22 }, stage);
  const arcG = sv('g', { opacity: 0 }, stage); arcG.innerHTML = TC.rebobina;
  // o Teco: corpo + rosto + duas mãos, cada parte troca de desenho sem recriar o resto
  const teco = sv('g', {}, stage);
  const tBody = sv('g', {}, teco); tBody.innerHTML = TC.corpo;
  const tFace = sv('g', {}, tBody);
  const hands = [sv('g', {}, teco), sv('g', {}, teco)];
  const phone = sv('g', {}, stage); phone.innerHTML = TC.celular.replace(/id="tc(\d+)"/g, 'id="tcm$1"').replace(/url\(#tc(\d+)\)/g, 'url(#tcm$1)');

  // efeito de rebobinar (tela toda) e flash
  const fx = sv('svg', { class: 'full', viewBox: `0 0 ${W} ${H}`, width: W, height: H }, root);
  fx.style.left = '0px'; fx.style.top = '0px';
  const scan = sv('g', { opacity: 0 }, fx);
  for (let i = 0; i < 14; i++) sv('rect', { x: 0, y: 0, width: W, height: 10 + (i % 3) * 6, fill: '#fff', opacity: 0.1 + (i % 2) * 0.06 }, scan);
  const rew = sv('g', { opacity: 0 }, fx);
  const RWX = WIDE ? W - 230 : W - 200, RWY = WIDE ? 120 : V ? 120 : 110;
  sv('rect', { x: RWX - 20, y: RWY - 52, width: 180, height: 104, rx: 52, fill: C.blueDeep, opacity: 0.85 }, rew);
  sv('path', { d: `M${RWX + 70},${RWY - 28} L${RWX + 30},${RWY} L${RWX + 70},${RWY + 28}Z M${RWX + 120},${RWY - 28} L${RWX + 80},${RWY} L${RWX + 120},${RWY + 28}Z`, fill: C.yel }, rew);
  const flash = el('div', 'flash', root);

  // ---------- texto ----------
  function headline(parts, opt = {}) {
    const box = el('div', 'hl', root, {
      left: L.tx.x + 'px', top: L.tx.y + 'px', fontSize: (opt.size || L.tx.size) + 'px', width: L.tx.w + 'px',
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
  function showHL(h, t, tin, tout) {
    const on = t >= tin - 0.01 && t < tout + 0.4;
    h.box.style.display = on ? 'block' : 'none';
    if (!on) return;
    h.words.forEach((w, i) => {
      const p = seg(t, tin + i * 0.05, 0.5, 'power3.out');
      w.style.transform = `translateY(${(1 - p) * 112}%)`;
    });
    const e = seg(t, tout, 0.32, 'power2.in');
    const mid = L.tx.mid ? ' translateY(-50%)' : '';
    h.box.style.transform = `translateY(${-40 * e}px)${mid}`;
    h.box.style.opacity = 1 - e;
  }
  const Y = C.yel;
  const HL = LOOP ? [] : [
    [headline([['Esse é o'], ['Teco.', Y]]), 0.9, 2.45],
    [headline([['Ele vive fazendo lance'], ['absurdo.', Y]]), 2.75, 5.45],
    [headline([['E odeia quando'], ['ninguém', Y], ['vê.']]), 5.75, 7.85],
    [headline([['Então ele aperta o'], ['botão.', Y]]), 8.1, 10.45],
    [headline([['Repeteco!', Y]], { size: L.tx ? L.tx.size * 1.35 : 0 }), 10.62, 11.6],
    [headline([['O lance volta pra'], ['você.', Y]]), 11.85, 13.15],
  ];

  // ---------- cartão final / logo ----------
  const endSvg = sv('svg', { class: 'full', viewBox: `0 0 ${W} ${H}`, width: W, height: H }, root);
  endSvg.style.left = '0px'; endSvg.style.top = '0px';
  // logo: tile amarelo com o "e" azul + "repeteco" branco
  const LG = LOOP ? { x: 60, y: 60, h: 92 } : V ? { x: 120, y: 250, h: 180 } : SQ ? { x: 150, y: 70, h: 140 } : { x: 110, y: 330, h: 170 };
  const logoG = sv('g', {}, endSvg);
  const tileG = sv('g', {}, logoG);
  const k = LG.h / 380;
  sv('rect', { x: 0, y: 0, width: 380, height: 380, rx: 104, fill: Y }, tileG);
  const eG = sv('g', { transform: 'translate(192,190)' }, tileG);
  sv('path', { d: M.E_PATH, fill: 'none', stroke: C.blue, 'stroke-width': M.SW, 'stroke-linejoin': 'miter' }, eG);
  sv('polygon', { points: M.E_ARROW.map((p) => p.join(',')).join(' '), fill: C.blue, stroke: C.blue, 'stroke-width': 7, 'stroke-linejoin': 'round' }, eG);
  const wmRect = sv('rect', { x: 0, y: -400, width: 0, height: 700 }, sv('clipPath', { id: 'wmClip' }, endSvg));
  const wmG = sv('g', { 'clip-path': 'url(#wmClip)' }, logoG);
  const wm = sv('path', { d: M.WORD, fill: '#fff' }, wmG);
  const tagBox = LOOP ? null : headline([['Esse lance merece'], ['repeteco.', Y]], { size: L.tx.size * 0.62 });
  const ul = sv('rect', { height: 10, rx: 5, fill: Y, opacity: 0 }, endSvg);
  if (tagBox) { tagBox.box.style.fontWeight = '800'; }
  function drawLogo(t, t0) {
    if (t < t0 - 0.01) { logoG.style.display = 'none'; return; }
    logoG.style.display = 'block';
    const p = seg(t, t0, 0.55, 'back.out(1.6)');
    const sc = k * p;
    tileG.setAttribute('transform', `translate(${LG.x + 190 * k},${LG.y + 190 * k}) rotate(${(-1 + p) * 200 - 360 * seg(t, t0 + 0.9, 0.7, 'power2.inOut')}) scale(${sc.toFixed(4)}) translate(-190,-190)`);
    const ws = LG.h / 380 * 350 / 350; // a palavra tem 350 de corpo na grade do tile
    const wx = LG.x + (380 + 85 - 12.6) * k, wy = LG.y + 282 * k;
    wm.setAttribute('transform', `translate(${wx},${wy}) scale(${(k).toFixed(4)})`);
    const wp = seg(t, t0 + 0.25, 0.6, 'power3.out');
    wmRect.setAttribute('x', wx - 20); wmRect.setAttribute('y', wy - 260 * k); wmRect.setAttribute('height', 360 * k);
    wmRect.setAttribute('width', ((M.WORD_BB[2] * k + 60) * wp).toFixed(1));
  }

  // ---------- movimento do Teco ----------
  const GY = 794; // centro do Teco parado no chão (raio 120)
  // chaves das mãos: [t, pose, x, y, rot, escala, aceno, duração da transição]
  const HAND_KEYS = LOOP ? [
    [[0, 'aberta', -135, 0, -20, 1.2, 1], [1.0, 'punho', -128, 30, -10, 1.15, 0, 0.25], [1.3, 'aberta', -110, -80, -35, 1.2, 0, 0.2], [2.45, 'punho', -128, 30, -10, 1.15, 0, 0.25], [3.55, 'aberta', -135, 0, -20, 1.2, 1, 0.4]],
    [[0, 'joinha', 130, 25, 10, 1.2, 0], [1.0, 'punho', 128, 30, 10, 1.15, 0, 0.25], [1.3, 'aberta', 110, -80, 35, 1.2, 0, 0.2], [2.45, 'punho', 128, 30, 10, 1.15, 0, 0.25], [2.75, 'joinha', 132, 10, 12, 1.25, 0, 0.25], [3.55, 'joinha', 130, 25, 10, 1.2, 0, 0.4]],
  ] : [
    [[0, 'aberta', -135, 0, -20, 0, 0], [1.05, 'aberta', -135, 0, -20, 1.2, 1, 0.3], [2.7, 'punho', -128, 30, -10, 1.15, 0, 0.25], [3.4, 'aberta', -110, -80, -35, 1.2, 0, 0.2],
      [4.6, 'aberta', -118, -70, -30, 1.2, 1, 0.3], [5.7, 'punho', -128, 30, -10, 1.15, 0, 0.3], [7.25, 'punho', -116, 78, 12, 1.1, 0, 0.4], [8.1, 'punho', -128, 30, -10, 1.15, 0, 0.3],
      [10.6, 'aberta', -118, -70, -40, 1.2, 0, 0.2], [11.6, 'punho', -128, 30, -10, 1.15, 0, 0.25], [12.2, 'aberta', -135, 0, -20, 1.2, 1, 0.3], [13.3, 'punho', -128, 30, -10, 1.15, 0, 0.25], [13.85, 'joinha', -126, 14, -10, 1.25, 0, 0.3]],
    [[0, 'joinha', 130, 25, 10, 0, 0], [1.45, 'joinha', 130, 25, 10, 1.2, 0, 0.3], [2.7, 'punho', 128, 30, 10, 1.15, 0, 0.25], [3.4, 'aberta', 110, -80, 35, 1.2, 0, 0.2],
      [4.6, 'aberta', 118, -70, 30, 1.2, 1, 0.3], [5.7, 'punho', 128, 30, 10, 1.15, 0, 0.3], [7.25, 'punho', 116, 78, -12, 1.1, 0, 0.4], [8.1, 'punho', 128, 30, 10, 1.15, 0, 0.3],
      [8.95, 'aponta', 129, -150, 142, 1.3, 0, 0.45], [9.3, 'aponta', 129, -150, 142, 1.3, 0, 0.05], [9.42, 'aponta', 129, -108, 142, 1.3, 0, 0.12], [9.75, 'aponta', 129, -150, 142, 1.3, 0, 0.2],
      [10.3, 'punho', 128, 30, 10, 1.15, 0, 0.3], [10.6, 'aberta', 118, -70, 40, 1.2, 0, 0.2], [11.6, 'punho', 128, 30, 10, 1.15, 0, 0.25], [12.2, 'punho', 154, -128, 100, 1.3, 0, 0.3],
      [13.3, 'punho', 128, 30, 10, 1.15, 0, 0.25], [13.85, 'aberta', 132, -24, 22, 1.2, 1, 0.3]],
  ];
  function handAt(keys, t) {
    let i = 0;
    while (i < keys.length - 1 && keys[i + 1][0] <= t) i++;
    let a = keys[i];
    const n = keys[i + 1];
    let p = 0;
    if (n) { const dur = n[7] || 0.3; p = seg(t, n[0] - dur, dur, 'power2.inOut'); }
    const b = n || a;
    const lerp = (j) => mix(a[j], b[j], p);
    const waving = (p < 0.5 ? a[6] : b[6]);
    return { pose: p < 0.5 ? a[1] : b[1], x: lerp(2), y: lerp(3), rot: lerp(4) + (waving ? 14 * Math.sin(TAU * (LOOP ? 1 : 1.5) * t) : 0), s: lerp(5) };
  }
  const FACES = LOOP
    ? [[0, 'feliz'], [1.0, 'focado'], [1.3, 'orgulhoso'], [2.5, 'piscando'], [3.5, 'feliz']]
    : [[0, 'surpreso'], [0.75, 'empolgado'], [2.7, 'focado'], [3.35, 'empolgado'], [4.45, 'orgulhoso'], [5.7, 'feliz'], [6.2, 'olha-esq'], [6.7, 'olha-dir'],
      [7.2, 'triste'], [8.1, 'surpreso'], [8.55, 'focado'], [9.45, 'empolgado'], [10.6, 'orgulhoso'], [11.65, 'feliz'], [12.15, 'apaixonado'], [13.3, 'feliz'], [14.1, 'orgulhoso'], [14.75, 'piscando']];
  const faceAt = (t) => { let f = FACES[0][1]; for (const [a, n] of FACES) if (t >= a) f = n; return f; };
  // impactos no chão: [tempo, força]
  const IMPACTS = LOOP ? [[2.35, 0.24]] : [[0.7, 0.26], [3.1, 0.12], [4.4, 0.24], [6.1, 0.12], [8.4, 0.12], [12.0, 0.12], [13.7, 0.12]];
  function squashAt(t) {
    let sy = 1;
    for (const [ti, A] of IMPACTS) { const q = t - ti; if (q >= 0 && q < 0.7) sy -= A * Math.exp(-q * 8) * Math.cos(q * 26); }
    const ant = LOOP ? [1.0, 1.25] : [3.15, 3.4];
    sy -= 0.16 * bump(t, ant[0], ant[1] - ant[0] - 0.02, 0.02, 0.06);
    return sy;
  }
  // saltinho de lugar a lugar
  function hop(t, a, dur, x0, x1, h) { const p = seg(t, a, dur, 'power2.inOut'); return [mix(x0, x1, p), -h * Math.sin(Math.PI * p), p]; }

  function tecoPose(t) {
    let x = 540, y = GY, rot = 0, air = false;
    if (LOOP) {
      y = GY - 8 * Math.sin(Math.PI * ((t % 1 + 1) % 1)) * (t < 1 || t > 3 ? 1 : 0); // respira devagar
      if (t >= 1.25 && t < 2.35) { const u = (t - 1.25) / 1.1; y = GY - 4 * 420 * u * (1 - u); air = true; rot = -360 * seg(t, 1.25, 1.1, 'power1.inOut'); }
      return { x, y, rot, air };
    }
    if (t < 0.7) { const p = seg(t, 0.1, 0.6, 'power2.in'); y = mix(-380, GY, p); rot = mix(-25, 0, p); air = true; }
    else if (t < 0.95) y = GY;
    else if (t < 1.35) { y = GY - 60 * Math.sin(Math.PI * seg(t, 0.95, 0.4, 'sine.inOut')); }
    else if (t < 2.7) { const q = t - 1.35; y = GY - 22 * Math.abs(Math.sin(Math.PI * 2.2 * q)) * Math.min(1, (2.7 - t) / 0.3); rot = 6 * Math.sin(Math.PI * 2.2 * q); } // comemora quicando
    if (t >= 2.7 && t < 3.4) { const [hx, hy, p] = hop(t, 2.7, 0.4, 540, 270, 70); x = hx; y = GY + hy; rot = -8 * Math.sin(Math.PI * p); }
    if (t >= 3.1 && t < 3.4) x = 270;
    if (t >= 3.4 && t < 4.4) { const u = (t - 3.4) / 1.0; x = mix(270, 830, u); y = GY - 4 * 470 * u * (1 - u); rot = 360 * seg(t, 3.4, 1.0, 'power1.inOut'); air = true; }
    if (t >= 4.4) x = 830;
    if (t >= 5.7) { const [hx, hy, p] = hop(t, 5.7, 0.4, 830, 520, 60); x = hx; if (t < 6.1) { y = GY + hy; rot = -8 * Math.sin(Math.PI * p); } }
    if (t >= 7.2 && t < 8.05) y = GY + 10 * seg(t, 7.2, 0.4, 'power2.out'); // murcha de tristeza
    if (t >= 8.05) { const [hx, hy, p] = hop(t, 8.05, 0.35, 520, 640, 60); x = hx; if (t < 8.4) { y = GY + hy; rot = 8 * Math.sin(Math.PI * p); } }
    if (t >= 10.6 && t < 11.6) { rot = -360 * seg(t, 10.6, 0.9, 'power2.inOut'); y = GY - 90 * Math.sin(Math.PI * seg(t, 10.6, 0.95, 'sine.inOut')); air = true; }
    if (t >= 11.6) { const [hx, hy, p] = hop(t, 11.6, 0.4, 640, 470, 60); x = hx; if (t < 12.0) { y = GY + hy; rot = -8 * Math.sin(Math.PI * p); } }
    if (t >= 13.3) { const [hx, hy, p] = hop(t, 13.3, 0.4, 470, WIDE ? 560 : 540, 70); x = hx; if (t < 13.7) { y = GY + hy; rot = 8 * Math.sin(Math.PI * p); } }
    if (t >= 14.1 && t < 14.75) { rot = -360 * seg(t, 14.1, 0.65, 'power2.inOut'); y = GY - 70 * Math.sin(Math.PI * seg(t, 14.1, 0.65, 'sine.inOut')); air = true; }
    if (t >= 14.75) y = GY - 5 * Math.sin(TAU * 2 * (t - 14.75));
    return { x, y, rot, air };
  }

  // ---------- render ----------
  function render(t) {
    // fundo vivo
    // no 9:16 os raios ocupam quase a tela toda: ficam parados e só dão um tranco nos beats
    const kick = 6 * seg(t, 3.4, 1.0, 'power2.inOut') + 22 * seg(t, 9.42, 0.7, 'power3.out') + 22 * seg(t, 10.6, 0.9, 'power3.out') + 6 * seg(t, 14.1, 0.65, 'power2.inOut');
    raysG.setAttribute('transform', `translate(${RC[0]},${RC[1]}) rotate(${(LOOP ? 18 * t / D : V ? kick : 4 * t).toFixed(2)})`);
    const ph = LOOP ? t / D : (V ? 0.015 : 0.06) * t, amp = 22 * st.s;
    sandA.setAttribute('d', wave(GROUND - 4, amp, ph, 0.4, [1, 2.3, 0.6]));
    sandB.setAttribute('d', wave(GROUND + amp * 1.4, amp * 0.7, -ph, 1.3, [1.4, 0.8, 2.1]));

    // cenário
    const netY = LOOP ? 900 : 600 * (1 - seg(t, 2.6, 0.45, 'power3.out')) + 600 * seg(t, 5.6, 0.35, 'power2.in');
    netG.setAttribute('transform', `translate(0,${netY.toFixed(1)})`);
    const press = bump(t, 9.42, 0.05, 0.1, 0.2);
    const btnY = LOOP ? 900 : 640 * (1 - seg(t, 8.0, 0.45, 'back.out(1.3)')) + 640 * seg(t, 10.7, 0.35, 'power2.in');
    btnG.setAttribute('transform', `translate(0,${btnY.toFixed(1)}) translate(850,880) scale(1,${(1 - 0.04 * press).toFixed(3)}) translate(-850,-880)`);
    rings.forEach((r, i) => {
      const q = seg(t, 9.42 + i * 0.08, 0.55, 'power2.out');
      r.setAttribute('rx', (80 + 120 * q).toFixed(1)); r.setAttribute('ry', (24 + 36 * q).toFixed(1));
      r.setAttribute('opacity', (t > 9.42 && !LOOP ? (1 - q) * 0.95 : 0).toFixed(2));
    });
    const cq = LOOP ? 0 : seg(t, 9.46, 0.35, 'back.out(2)') * (1 - seg(t, 10.3, 0.25, 'power2.in'));
    clique.setAttribute('opacity', cq.toFixed(2));
    clique.setAttribute('transform', `translate(905,610) rotate(-10) scale(${(0.6 + 0.4 * cq).toFixed(3)})`);

    // Teco
    const P = tecoPose(t);
    const sy = squashAt(t), sx = 1 / Math.sqrt(sy);
    const yy = P.y + (P.air ? 0 : 120 * (1 - sy));
    const tk = 1.2;
    teco.setAttribute('transform', `translate(${P.x.toFixed(1)},${yy.toFixed(1)}) rotate(${P.rot.toFixed(2)}) scale(${tk})`);
    tBody.setAttribute('transform', `scale(${sx.toFixed(3)},${sy.toFixed(3)})`);
    html(tFace, TC.rostos[faceAt(t)]);
    HAND_KEYS.forEach((keys, i) => {
      const h = handAt(keys, t);
      html(hands[i], (i === 0 ? TC.maosEsp : TC.maos)[h.pose]);  // a mão da esquerda já vem espelhada, com a sombra no lado certo
      hands[i].setAttribute('transform', `translate(${h.x.toFixed(1)},${h.y.toFixed(1)}) rotate(${h.rot.toFixed(1)}) scale(${h.s.toFixed(3)})`);
      hands[i].style.display = h.s < 0.02 ? 'none' : 'block';
    });
    const hgt = Math.max(0, Math.min(1, (GY - P.y) / 470));
    shadow.setAttribute('cx', P.x.toFixed(1));
    shadow.setAttribute('rx', (108 * (1 - 0.55 * hgt)).toFixed(1));
    shadow.setAttribute('opacity', (P.y < -100 ? 0 : 0.22 * (1 - 0.6 * hgt)).toFixed(3));

    // rastro do salto
    const flyA = LOOP ? 1.25 : 3.4, flyD = LOOP ? 1.1 : 1.0;
    ghosts.forEach((g, i) => {
      const kk = 5 - i, tt = t - kk * 0.055;
      const on = t > flyA + 0.05 && t < flyA + flyD + 0.05 && tt > flyA;
      const pp = tecoPose(tt);
      g.setAttribute('cx', pp.x.toFixed(1)); g.setAttribute('cy', pp.y.toFixed(1));
      g.setAttribute('opacity', on ? (0.3 * (1 - kk / 6)).toFixed(3) : 0);
    });
    // areia levantando nos impactos fortes
    const big = IMPACTS.filter(([, A]) => A > 0.2).map(([ti]) => ti);
    let ti = null; for (const b of big) if (t >= b && t < b + 0.7) ti = b;
    puffs.forEach((p, i) => {
      if (ti === null) { p.setAttribute('opacity', 0); return; }
      const q = seg(t, ti, 0.6, 'power2.out'), a = -Math.PI * (0.08 + 0.84 * (i / 7));
      const px = (LOOP ? 540 : tecoPose(ti).x) + Math.cos(a) * 170 * q, py = 902 + Math.sin(a) * 90 * q;
      p.setAttribute('cx', px.toFixed(1)); p.setAttribute('cy', py.toFixed(1)); p.setAttribute('r', (8 + 8 * (1 - q)).toFixed(1));
      p.setAttribute('opacity', (1 - q).toFixed(2));
    });

    // arco de rebobinar em volta do Teco
    const spins = LOOP ? [[1.25, 1.1]] : [[10.6, 0.95], [14.1, 0.65]];
    let ao = 0, as = 1, arot = 0;
    for (const [a, d] of spins) if (t > a - 0.1 && t < a + d + 0.3) { ao = seg(t, a - 0.05, 0.2, 'power2.out') * (1 - seg(t, a + d, 0.25, 'power2.in')); as = (a > 14 ? 0.85 : 1) * (0.7 + 0.3 * seg(t, a - 0.05, 0.35, 'back.out(2)')); arot = -360 * seg(t, a, d, 'power2.inOut'); }
    arcG.setAttribute('opacity', ao.toFixed(2));
    arcG.setAttribute('transform', `translate(${P.x.toFixed(1)},${yy.toFixed(1)}) rotate(${arot.toFixed(1)}) scale(${(as * 1.25).toFixed(3)})`);

    // celular
    if (!LOOP) {
      const pin = seg(t, 11.8, 0.5, 'back.out(1.3)'), pout = seg(t, 13.2, 0.35, 'power2.in');
      const px = mix(1500, 820, pin) + 700 * pout;
      phone.setAttribute('transform', `translate(${px.toFixed(1)},${(650 + 8 * Math.sin(TAU * 0.8 * t)).toFixed(1)}) rotate(${8 + 4 * (1 - pin)}) scale(1.02)`);
      phone.style.display = t > 11.7 && t < 13.6 ? 'block' : 'none';
    } else phone.style.display = 'none';

    // rebobinar: linhas de fita e o selo ◀◀
    const rw = LOOP ? 0 : bump(t, 10.58, 0.08, 0.75, 0.25);
    scan.setAttribute('opacity', (rw * 0.9).toFixed(2));
    [...scan.children].forEach((r, i) => {
      const yv = ((i * 97 + (1 - ((t * 2.6) % 1)) * H * 1.2) % (H * 1.1)) - 40;
      r.setAttribute('y', yv.toFixed(1));
    });
    rew.setAttribute('opacity', (rw * (0.75 + 0.25 * Math.sign(Math.sin(TAU * 4 * t)))).toFixed(2));

    // flash nos picos
    // envelope igual ao do manifesto: sobe 0,1 s, segura 0,15 s e decai devagar (nada pisca rápido demais)
    let fl = 0, punch = 0;
    for (const p of (LOOP ? [2.35] : [0.7, 9.42, 10.6])) {
      const q = t - p;
      if (q >= 0 && q < 1.6) {
        const e = q < 0.1 ? q / 0.1 : q < 0.25 ? 1 : Math.exp(-(q - 0.25) / 0.3);
        fl = Math.max(fl, e); if (p > 9) punch = Math.max(punch, e);
      }
    }
    flash.style.opacity = (fl * (LOOP ? 0.12 : 0.18)).toFixed(3);
    // soco de câmera no clique e no rebobinar
    const pz = 1 + (LOOP ? 0.03 * fl : (V ? 0.18 : 0.07) * punch);
    stage.style.transformOrigin = `${(P.x * st.s).toFixed(0)}px ${(P.y * st.s).toFixed(0)}px`;
    stage.style.transform = `scale(${pz.toFixed(4)})`;

    // texto
    HL.forEach(([h, a, b]) => showHL(h, t, a, b));
    if (LOOP) drawLogo(t + 10, 0); else drawLogo(t, 13.35);
    if (tagBox) {
      const top = LG.y + LG.h + (V ? 70 : SQ ? 40 : 60);
      tagBox.box.style.left = LG.x + 'px'; tagBox.box.style.top = top + 'px'; tagBox.box.style.width = (W - LG.x - 40) + 'px';
      showHL(tagBox, t, 13.85, 99);
      const u = seg(t, 14.45, 0.45, 'power3.inOut');
      const last = tagBox.words[tagBox.words.length - 1];
      if (t > 14.4) {
        const r = last.getBoundingClientRect(), rr = root.getBoundingClientRect();
        ul.setAttribute('x', (r.left - rr.left + 4).toFixed(1)); ul.setAttribute('y', (r.bottom - rr.top + 6).toFixed(1));
        ul.setAttribute('width', ((r.width - 16) * u).toFixed(1)); ul.setAttribute('opacity', 1);
      } else ul.setAttribute('opacity', 0);
    }
  }

  S.play(render, { loop: LOOP });
})();
