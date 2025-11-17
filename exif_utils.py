import exifread

def extract_gps(image_file):
    """
    Liest EXIF GPS Daten aus und gibt sie als Lat/Long zurück.
    Falls keine Daten vorhanden sind, wird None zurückgegeben.
    """

    tags = exifread.process_file(image_file, details=False)

    try:
        lat = tags.get("GPS GPSLatitude")
        lon = tags.get("GPS GPSLongitude")
        lat_ref = tags.get("GPS GPSLatitudeRef")
        lon_ref = tags.get("GPS GPSLongitudeRef")

        if not lat or not lon:
            return None

        lat_dec = _convert_to_decimal(lat, lat_ref)
        lon_dec = _convert_to_decimal(lon, lon_ref)

        return {"lat": lat_dec, "lon": lon_dec}

    except Exception:
        return None


def _convert_to_decimal(value, ref):
    """
    Hilfsfunktion um EXIF Koordinaten in Dezimalgrad umzuwandeln.
    Beispiel: [52/1, 30/1, 0/1] → 52.5
    """

    coords = [float(x.num) / float(x.den) for x in value.values]

    decimal = coords[0] + coords[1] / 60 + coords[2] / 3600

    if ref in ["S", "W"]:
        decimal = -decimal

    return round(decimal, 6)
