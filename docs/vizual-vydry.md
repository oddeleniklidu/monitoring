# Vizuál Vydry

## M1.2 — použitý originál

Web používá dodaný soubor `assets/images/postava-vydra-flegmatik.png`: Vydru se sluchátky a mikrofonem. Obrázek je beze změn, nejde o novou ani upravenou AI ilustraci. Jeho původní barevné pozadí je součástí obrázku, nikoli barvou rozhraní.

V repozitáři není původní obraz Vydry s lucernou ve starobylém archivu. Historické prostředí proto není doplněné náhradním obrázkem. Pokud bude originál dodaný, nahrajte jej například do `assets/images/vydra-archiv.webp` a v `_config.yml` nastavte:

```yaml
archive_image: "/assets/images/vydra-archiv.webp"
archive_image_alt: "Vydra s lucernou ve starobylém archivu"
```

Nastavení proveďte v obou repozitářích. Obrázek se použije výhradně v úvodní části; nemění vzhled digitálních karet, filtrů ani tabulek. Při `archive_image: null` zůstává zobrazený dodaný portrét. Obrázky se automaticky neanimují a videa se nepřehrávají.

## Rozhraní

Společný styl je v `assets/archive.css`, struktura v `_layouts/default.html` a `_includes/entrance.html`. Inter a Barlow Condensed se načítají z místních souborů v `assets/fonts/`, kde jsou i licence. Stejné prezentační soubory se udržují v `Sanony` i `monitoring`.

Obsah Markdownu a původní adresy zůstávají zachované. Na šířce mobilu se posouvají do stran jen tabulky, nikoliv celá stránka.
