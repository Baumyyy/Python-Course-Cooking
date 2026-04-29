# Mauricio Ragebait
Selaimessa pelattava Mauricio-ragebait-peli, jossa Python-backend vastaa käyttäjän viesteihin.

## Projektin rakenne
- `app.py` — Flask-backend, joka palvelee HTML-sivua ja käsittelee viestit
- `index.html` — chat-käyttöliittymä Mauricio-pelin selaimessa pelaamiseen
- `styles.css` — sivun tyylit
- `PROJECT_SPEC.md` — kurssin projektityön vaatimukset ja spesifikaatio
- `requirements.txt` — Python-riippuvuudet

## Käyttö
Asenna riippuvuudet:

```bash
python -m pip install -r requirements.txt
```

Käynnistä backend:

```bash
python app.py
```

Avaa selaimessa:

```
http://127.0.0.1:5000
```

## Mitä projekti tekee
- Pelaaja kirjoittaa provosoivia viestejä Mauriciolle.
- Python-backend analysoi viestin ja palauttaa Mauricion vastauksen.
- Rauhallisuusmittari muuttuu vastauksen mukaan.
- Jos rauhallisuus laskee nollaan, Mauricio ragebaittuu kokonaan ja peli päättyy.

## Huomio
Tämä projekti käyttää oikeaa Python-backendiä, eikä komentoriviversiota enää tarvita.
