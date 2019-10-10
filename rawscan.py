""" Test script of bosch_thermostat_http. """
import asyncio

import aiohttp
import json
import bosch_thermostat_http as bosch
from bosch_thermostat_http.const import FIRMWARE_VERSION, DATE
# from bosch_thermostat_http.db import bosch_sensors


async def main():
    """
    Provide data_file.txt with ip, access_key, password and check
    if you can retrieve data from your thermostat.
    """
    async with aiohttp.ClientSession() as session:
        data_file = open("data_file_ka.txt", "r")
        data = data_file.read().splitlines()
        gateway = bosch.Gateway(session=session,
                                host=data[0],
                                access_key=data[1])
                                # password=data[2])
        await gateway.check_connection()
        #sensors = bosch_sensors(gateway.get_info(FIRMWARE_VERSION))
        #print(sensors)
        #await gateway.initialize_sensors(sensors)
        #print(gateway.sensors)
        #
        rawscan = await gateway.smallscan()
        print(rawscan)
        print(hc.schedule.get_temp_for_date(gateway.get_info(DATE)))
        to_file = "kamika_raw.json"
        with open(to_file, 'w') as logfile:
            json.dump(rawscan, logfile, indent=4)
        await session.close()


asyncio.get_event_loop().run_until_complete(main())