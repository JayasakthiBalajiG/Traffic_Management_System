import gpsd

# Function to generate Google Maps link
def generate_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps?q={latitude},{longitude}"


def get_coordinates():
    gpsd.connect()
    packet = gpsd.get_current()
    latitude = packet.lat
    longitude = packet.lon

    return latitude, longitude

def main():
    try:
        latitude, longitude = get_coordinates()
        
        maps_link = generate_google_maps_link(latitude, longitude)
        
        print("Google Maps link:", maps_link)
    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    main()