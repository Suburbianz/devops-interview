import requests
from datetime import datetime, timezone
import pytz

# Coordinates
latitude = 50.930581
longitude = 5.780691

# Timezone office
timezone_cet = pytz.timezone('Europe/Amsterdam')

# API call
api_url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
response = requests.get(api_url)
data = response.json()

# Retrieve sunrise and sunset (UTC)
sunrise_utc = datetime.fromisoformat(data['results']['sunrise'])
sunset_utc = datetime.fromisoformat(data['results']['sunset'])

# Convert to CET/CEST
sunrise_cet = sunrise_utc.astimezone(timezone_cet)
sunset_cet = sunset_utc.astimezone(timezone_cet)

# Current time in CET/CEST
current_time = datetime.now(timezone_cet)

# Determine lights status
if sunset_cet <= current_time or current_time < sunrise_cet:
    print("ON")
else:
    print("OFF")