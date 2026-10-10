import swisseph as swe

# -------------------------------------------------------
# Birth details
# -------------------------------------------------------
year = 2003
month = 11
day = 29
hour = 23 + 44/60.0   # 23:44 = 23.7333 hours

# Location: Tirupati
lat = 13.63    # North
lon = 79.42    # East

# Time zone: IST = UTC+5:30
timezone = 5.5
ut_hour = hour - timezone

# Compute Julian Day (UT)
jd = swe.julday(year, month, day, ut_hour)

# -------------------------------------------------------
# Planets list
# -------------------------------------------------------
planet_codes = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
    "Rahu (North Node)": swe.TRUE_NODE,
}

# -------------------------------------------------------
# Planetary positions
# -------------------------------------------------------
print(f"Ephemeris for {day}-{month}-{year} {hour:.2f} (IST), Tirupati")
print("-------------------------------------------------------------")

for name, code in planet_codes.items():
    res, _ = swe.calc_ut(jd, code)
    lon, lat_p, dist = res[:3]
    print(f"{name:18s} Lon: {lon:9.5f}°  Lat: {lat_p:8.5f}°  Dist: {dist:.6f}")

# -------------------------------------------------------
# Ketu (South Node) = 180° opposite Rahu
# -------------------------------------------------------
rahu_res, _ = swe.calc_ut(jd, swe.TRUE_NODE)
rahu_lon = rahu_res[0]
ketu_lon = (rahu_lon + 180.0) % 360.0
print(f"{'Ketu (South Node)':18s} Lon: {ketu_lon:9.5f}°")

# -------------------------------------------------------
# Houses (Ascendant + Cusps)
# -------------------------------------------------------
cusps, ascmc = swe.houses(jd, lat, lon, b'P')  # Placidus by default

print("\nHouse Cusps (Placidus System):")
print("-------------------------------------------------------------")
for i, cusp in enumerate(cusps, start=1):
    print(f"House {i:2d}: {cusp:9.5f}°")

print("\nKey Angles:")
print("-------------------------------------------------------------")
print(f"Ascendant (Lagna): {ascmc[0]:9.5f}°")
print(f"MC (10th house cusp): {ascmc[1]:9.5f}°")
print(f"ARMC: {ascmc[2]:9.5f}°")
print(f"Vertex: {ascmc[3]:9.5f}°")
print(f"Equatorial Asc: {ascmc[4]:9.5f}°")
print(f"Co-Asc (Munkasey): {ascmc[5]:9.5f}°")
print(f"Co-Asc (Koch): {ascmc[6]:9.5f}°")
print(f"Polar Asc: {ascmc[7]:9.5f}°")
