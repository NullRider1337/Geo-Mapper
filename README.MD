# PhotoGeo Mapper

Ein kleines Wochenende-Projekt, mit dem ich experimentiert habe, um EXIF-Daten aus Fotos auszulesen und auf einer Karte darzustellen.  
Das Tool kann aktuell nur einfache Location-Daten anzeigen, aber vielleicht baue ich es irgendwann mal weiter aus.

## Features
- Liest EXIF Location Daten aus JPG-Dateien
- Zeigt GPS-Koordinaten in einem einfachen Web-Interface an
- Export als JSON
- Minimalistische UI (Vanilla JS)

## TODO
- Unterstützung für RAW-Formate
- Reverse Geocoding (Adresse → Koordinaten)
- Kartenmarker stylen
- Upload-History speichern (wenn ich Zeit finde 😅)

## Tech Stack
- Python 3.10
- Flask
- exifread
- Leaflet.js

## Installation

```bash
git clone https://github.com/johannesdev/photo-geo-mapper
cd photo-geo-mapper
pip install -r requirements.txt
python app.py

##Contact
twitter/X
@NullRider1337
mail
nullrider1337(at)gmail.com



DISCLAIMER --- This for a CTF Challenge ---
