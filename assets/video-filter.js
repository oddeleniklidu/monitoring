(() => {
  "use strict";
  const search = document.getElementById("q");
  const status = document.getElementById("f");
  const reset = document.getElementById("reset-filters");
  const count = document.getElementById("filter-count");
  const rows = Array.from(document.querySelectorAll("#video-table tbody tr"));
  if (!search || !status || !reset || !count) return;
  const titles = rows.map(row => row.cells[0].textContent.toLocaleLowerCase("cs"));
  function filter() {
    const term = search.value.trim().toLocaleLowerCase("cs");
    let visible = 0;
    rows.forEach((row, index) => {
      const matches = titles[index].includes(term) && (!status.value || row.dataset.status === status.value);
      row.hidden = !matches;
      if (matches) visible++;
    });
    count.textContent = `Zobrazeno ${visible} z ${rows.length} videí.`;
  }
  search.addEventListener("input", filter);
  status.addEventListener("change", filter);
  reset.addEventListener("click", () => { search.value = ""; status.value = ""; filter(); search.focus(); });
  filter();
})();
