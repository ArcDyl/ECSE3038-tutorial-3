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

@app.post("/devices")
async def add_device(device: dict):
    readings.append(device)
    return device

@app.get("/rooms/{room}/devices")
async def get_devices_by_room(room):
    devices = []
    for device in readings:
        if device["room"] == room:
            devices.append(device)
    if devices == []:
        raise HTTPException(status_code=404, detail="Room not found")
    return devices

# return the average temperature
@app.get("/devices/average")
async def average_temp():
    sum_temp = 0
    for device in readings:
        sum_temp+= device['temp']
        avg_temp = sum_temp / len(readings)
    return avg_temp

@app.get("/devices/{name}")
async def get_device(name):
    for device in readings:
        if device["name"] == name:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.get("/devices/online")
async def online():
    devices = []
    for device in readings:
        if device["online"] == True:
            devices.append(device)
    return devices

# return the whole dictionary of the hottest device
@app.get("/devices/hottest")
async def hottest():
    hottest_temp = 0.0
    hottest_device = None
    for device in readings:
        if device['temp'] > hottest_temp:
            hottest_temp = device['temp']
            hottest_device = device
    return hottest_device
