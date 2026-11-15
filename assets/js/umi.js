// UMI Stuttgart – kleines Skript: Menü auf dem Handy, Platzhalter-Knöpfe
(function () {
  var t = document.querySelector('.menu-toggle');
  var n = document.getElementById('hauptmenue');
  if (t && n) {
    t.addEventListener('click', function () {
      var open = n.classList.toggle('open');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  // Knöpfe, deren Ziel noch fehlt (z. B. Gutschein-Shop), lösen nichts aus
  document.querySelectorAll('a[aria-disabled="true"]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); });
  });
})();
