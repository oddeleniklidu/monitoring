# Monitoring

Kontroly dostupnosti veřejného internetového obsahu.

## Web

[Otevřít web Monitoring](https://oddeleniklidu.github.io/monitoring/)

Web publikuje GitHub Pages z kořene větve `main`. Úvodní stránky případů načítají obsah příslušného `README.md`; úpravy podkladů se tedy projeví i na webu po novém sestavení.

## Vydřin archiv

Společný vzhled se spravuje v `assets/archive.css`, `_layouts/default.html` a `_includes/entrance.html` obou repozitářů. Obsah šanonů zůstává v Markdownu. [Kam nahrát vizuál Vydry](docs/vizual-vydry.md).

Kontrola PR sestaví Jekyll, prověří místní odkazy a nabídne sestavený web jako artefakt `vydrin-archiv-preview`. Publikování na GitHub Pages nadále probíhá z větve `main`.
