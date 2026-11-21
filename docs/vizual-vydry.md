# Vizuál Vydry s lucernou

V době úpravy M1.1 není v tomto repozitáři dodaný obrázek ani video. Web proto používá typografický titulní list na tmavém pozadí. Nejde o hotovou náhradu dodaného vizuálu.

## Kam nahrát obrázek

1. Nahrajte obrázek do `assets/images/vydra-archiv.webp` (lze použít také JPG nebo PNG).
2. V `_config.yml` změňte `archive_image: null` na `archive_image: "/assets/images/vydra-archiv.webp"`.
3. Obrázek a změnu nastavení zveřejněte ve větvi `main`. GitHub Pages web znovu sestaví.

Stejné soubory a nastavení použijte v repozitářích `Sanony` i `monitoring`.

Motiv: Vydra s lucernou ve starobylém archivu. Prostor pro text je vlevo; postava a lucerna by měly být spíše vpravo. Doporučená šířka alespoň 1600 px, poměr přibližně 16 : 9, velikost ideálně do 500 kB. Na telefonu se výřez zúží; ověřte, že zůstane vidět postava i lucerna. Obrázek je dekorativní, veškeré informace jsou samostatně v textu.

Rozložení už obsahuje vrstvu pro obrázek a ztmavení pod textem. Dokud je nastavení `null`, nevzniká žádný neplatný požadavek na chybějící soubor. Video se automaticky nepřehrává; pokud má být později použito, zachovejte statický obrázek a respektujte omezení pohybu uživatele.
