# Vizuál Vydry

## Aktuální motiv

`assets/images/vydra-archivar-tablet-3x2.png` — Vydra jako archivář mezi starými regály s pavučinami. Drží jedno zařízení kombinující sci-fi tablet a čtečku. Poměr stran 3 : 2, rozlišení 1536 × 1024 px.

Obrázek vznikl na výslovný navazující požadavek uživatele úpravou dodaného souboru `postava-vydra-flegmatik.png` pomocí ImageGen. Rozpoznatelná podoba Vydry, sluchátka, šátek a flegmatický výraz zůstaly zachované. Původní portrét je stále uložený a používá se jako záloha.

Historický prostor je pouze součástí úvodní ilustrace. Tlačítka, texty, karty a tabulky zůstávají moderní a tmavé.

## Nastavení

```yaml
archive_image: "/assets/images/vydra-archivar-tablet-3x2.png"
archive_image_alt: "Vydra archivář mezi starými regály s pavučinami drží sci-fi tablet s integrovanou čtečkou"
archive_image_width: 1536
archive_image_height: 1024
```

Stejné nastavení i obrázek udržujte v obou repozitářích. Nastavením `archive_image: null` se vrátí původní dodaný portrét. Při výměně upravte také alternativní popis a rozměry. Obrázek se neanimuje ani automaticky nepřehrává video.

## Rozhraní

Společný styl je v `assets/archive.css`, struktura v `_layouts/default.html` a `_includes/entrance.html`. Inter a Barlow Condensed se načítají z místních souborů v `assets/fonts/`, kde jsou i licence.

Obsah Markdownu a původní adresy zůstávají zachované. Na mobilu se posouvají do stran jen tabulky, nikoliv celá stránka.
