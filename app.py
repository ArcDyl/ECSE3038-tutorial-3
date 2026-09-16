from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

@app.get("/devices")
async def get_devices():
    return readings

# return the average temperature
def average_temp(devices):
    sum_temp = 0
    for device in devices:
        sum_temp+= device['temp']
        avg_temp = sum_temp / len(devices)
    return avg_temp

# return the whole dictionary of the hottest device
def hottest(devices):
    hottest_temp = 0.0
    hottest_device = None
    for device in devices:
        if device['temp'] > hottest_temp:
            hottest_temp = device['temp']
            hottest_device = device
    return hottest_device
