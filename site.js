/* Casas em Pipa — menu, consulta via WhatsApp e galeria. Sem dependências. */
(function () {
  "use strict";
  var cfg = window.SITE || {};

  /* ---- menu do celular ---- */
  var mb = document.querySelector(".menu-btn"), dr = document.getElementById("drawer");
  if (mb && dr) {
    mb.addEventListener("click", function () {
      var open = dr.classList.toggle("open");
      mb.setAttribute("aria-expanded", open ? "true" : "false");
    });
    dr.addEventListener("click", function (e) { if (e.target.tagName === "A") { dr.classList.remove("open"); mb.setAttribute("aria-expanded", "false"); } });
  }

  /* ---- consulta de disponibilidade -> WhatsApp ---- */
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function iso(d) { return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); }
  function br(s) { var p = s.split("-"); return p[2] + "/" + p[1] + "/" + p[0]; }
  function parse(s) { var p = s.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function addDays(d, n) { var x = new Date(d); x.setDate(x.getDate() + n); return x; }
  var MIN = cfg.minNoites || 1;

  document.querySelectorAll("form.reserva").forEach(function (f) {
    var casa = f.querySelector("[name=casa]"), ent = f.querySelector("[name=entrada]"),
        sai = f.querySelector("[name=saida]"), hos = f.querySelector("[name=hospedes]"),
        obs = f.querySelector("[name=obs]"), msg = f.querySelector(".form-msg");
    var hoje = iso(new Date());
    ent.min = hoje; sai.min = iso(addDays(new Date(), MIN));

    function capacidade() {
      var opt = casa.tagName === "SELECT" ? casa.options[casa.selectedIndex] : casa;
      return +(opt.getAttribute("data-max") || 0);
    }
    function syncMax() {
      var m = capacidade();
      if (m) { hos.max = m; } else { hos.removeAttribute("max"); }
    }
    function syncSaida() {
      if (!ent.value) return;
      var minS = iso(addDays(parse(ent.value), MIN));
      sai.min = minS;
      if (!sai.value || sai.value < minS) sai.value = minS;
    }
    if (casa.tagName === "SELECT") casa.addEventListener("change", function () { syncMax(); say(""); });
    ent.addEventListener("change", function () { syncSaida(); say(""); });
    syncMax();

    function say(t, err) { if (!msg) return; msg.textContent = t; msg.className = "form-msg" + (err ? " err" : ""); }

    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var op = casa.tagName === "SELECT" ? casa.options[casa.selectedIndex] : null;
      var nomeCasa = op ? (op.getAttribute("data-nome") || op.text) : casa.value;
      var h = parseInt(hos.value, 10), max = capacidade();
      if (!ent.value || !sai.value) { say("Escolha as datas de entrada e saída.", true); (ent.value ? sai : ent).focus(); return; }
      if (ent.value < hoje) { say("A data de entrada já passou.", true); ent.focus(); return; }
      var noites = Math.round((parse(sai.value) - parse(ent.value)) / 864e5);
      if (noites < MIN) { say("A estadia mínima é de " + MIN + " noite" + (MIN > 1 ? "s" : "") + ".", true); sai.focus(); return; }
      if (!h || h < 1) { say("Informe o número de hóspedes.", true); hos.focus(); return; }
      if (max && h > max) {
        say("A " + nomeCasa + " recebe até " + max + " hóspedes. Para grupos maiores, escolha “Mais de uma casa”.", true);
        hos.focus(); return;
      }
      var linhas = [
        "Olá! Vim pelo site e gostaria de consultar disponibilidade e valor:",
        "• Casa: " + nomeCasa,
        "• Entrada: " + br(ent.value),
        "• Saída: " + br(sai.value) + " (" + noites + " noite" + (noites > 1 ? "s" : "") + ")",
        "• Hóspedes: " + h
      ];
      if (obs && obs.value.trim()) linhas.push("• Observações: " + obs.value.trim());
      var url = "https://wa.me/" + cfg.whatsapp + "?text=" + encodeURIComponent(linhas.join("\n"));
      say("Abrindo o WhatsApp com sua mensagem pronta…");
      var w = window.open(url, "_blank", "noopener");
      if (!w) window.location.href = url;
    });
  });

  /* ---- galeria em tela cheia ---- */
  var lb = document.querySelector("dialog.lb");
  if (lb && typeof lb.showModal === "function") {
    var fotos = [].slice.call(document.querySelectorAll("[data-lb]")).map(function (b) {
      return { src: b.getAttribute("data-lb"), alt: b.querySelector("img") ? b.querySelector("img").alt : "" };
    });
    var img = lb.querySelector(".lb-stage img"), cap = lb.querySelector(".lb-cap"), cnt = lb.querySelector(".lb-n"), i = 0, opener = null;
    function show(n) {
      i = (n + fotos.length) % fotos.length;
      img.src = fotos[i].src; img.alt = fotos[i].alt; cap.textContent = fotos[i].alt;
      cnt.textContent = (i + 1) + " / " + fotos.length;
    }
    function open(n) { opener = document.activeElement; show(n); lb.showModal(); }
    document.querySelectorAll("[data-lb]").forEach(function (b, n) { b.addEventListener("click", function () { open(n); }); });
    document.querySelectorAll("[data-lb-open]").forEach(function (b) { b.addEventListener("click", function () { open(0); }); });
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(i - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(i + 1); });
    lb.querySelector(".lb-close").addEventListener("click", function () { lb.close(); });
    lb.addEventListener("close", function () { if (opener) opener.focus(); });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") show(i - 1);
      if (e.key === "ArrowRight") show(i + 1);
    });
    var x0 = null;
    lb.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  /* ---- contador da galeria no celular ---- */
  var gg = document.querySelector(".gal-grid"), gc = document.querySelector(".gal-count");
  if (gg && gc) {
    var total = gg.children.length;
    gg.addEventListener("scroll", function () {
      var w = gg.children[0].getBoundingClientRect().width + 8;
      gc.textContent = Math.min(total, Math.round(gg.scrollLeft / w) + 1) + " / " + total;
    }, { passive: true });
  }
})();
