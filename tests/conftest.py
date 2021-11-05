from pytest import fixture


@fixture
def get_panel_response():
    return {
    "rigs": {
        "xxxxxx": {
            "miner": "XXXXXXXXXXXX",
            "version": "X.X.X",
            "condition": "XXXXXXXXXXXX",
            "rig_watts": 1000,
            "driver": "amdgpu",
            "gpus": "6",
            "miner_instance": "6",
            "miner_hashes": "32.71 27.96 30.92 30.19 24.93 31.34",
            "bioses": "xxx-xxx-xxxx xxx-xxx-xxxx xxx-xxx-xxxx xxx-xxx-xxxx xxx-xxx-xxxx xxx-xxx-xxxx",
            "meminfo": "GPU0:01.00.0:Radeon RX 580:XXX-XXXXXXX-XXX:Micron XXXXXXXXXXX:GDDR5:Polaris10\nGPU1:03.00.0:Radeon RX 580:XXX-XXXXXXXX_XXX:Micron XXXXXXXXXXX:GDDR5:Polaris10\nGPU2:05.00.0:Radeon RX 580:XXX-XXXXXX-XXX:SK Hynix XXXXXXXXXXX:GDDR5:Polaris10\nGPU3:06.00.0:Radeon RX 580:XXX-XXXXXXX-XXX:Samsung XXXXXXXXX:GDDR5:Polaris10\nGPU4:07.00.0:Radeon RX 580:xxx-xxx-xxxx:Samsung XXXXXXXXXX:GDDR5:Polaris10\nGPU5:08.00.0:Radeon RX 580:XXX-XXXX-XXX:Micron XXXXXXXXXXX:GDDR5:Polaris10",
            "vramsize": "8 8 8 8 8 8",
            "drive_name": "XXXXXXXXXXXXXXXXXX",
            "mobo": "XXXXXXXXXXXXX",
            "biosversion": "XXXXXX",
            "lan_chip": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "connected_displays": null,
            "ram": "4",
            "flags": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
            "rack_loc": "XXXXXX",
            "pdu_name": null,
            "pdu_port": null,
            "pdu_ip": null,
            "ext_temp1": null,
            "ext_temp2": null,
            "ext_temp3": null,
            "ext_temp4": null,
            "ext_temp5": null,
            "ext_temp6": null,
            "ext_temp7": null,
            "ext_temp8": null,
            "ext_temp9": null,
            "ext_temp10": null,
            "ip": "10.0.0.10",
            "server_time": 1636143288,
            "uptime": "703125",
            "miner_secs": 703051,
            "rx_kbps": "0.25",
            "tx_kbps": "0.09",
            "possible_intrusion": null,
            "load": "0.43",
            "cpu_temp": "30",
            "freespace": 0.8,
            "hash": 178.05,
            "pool": "XXXXXXXXXXXXXXXXXX",
            "temp": "58.00 55.00 52.00 54.00 51.00 57.00",
            "powertune": "5 5 5 5 5 5",
            "voltage": "1.040 1.113 1.069 1.053 1.063 1.024",
            "watts": "145 161 161 141 118 170",
            "fanrpm": "2893 2987 3077 3087 4487 4466",
            "fanpercent": "100 100 100 100 100 100",
            "core": "1257 1295 1309 1300 1282 1257",
            "mem": "2250 2000 2150 2125 2000 2150"
        }
    },
    "total_hash": 178.05,
    "total_watts": 946,
    "alive_gpus": 6,
    "total_gpus": 6,
    "alive_rigs": 1,
    "total_rigs": 1,
    "current_version": "X.X.X",
    "avg_temp": 54.5,
    "capacity": "100.0",
    "per_info": {
        "XXXXXXXXXXX": {
            "hash": "178.1",
            "per_alive_gpus": 6,
            "per_total_gpus": 6,
            "per_alive_rigs": 1,
            "per_total_rigs": 1,
            "per_total_watts": 946,
            "per_watts-rig": "946.0",
            "per_hash-gpu": "29.7",
            "per_hash-rig": "178.1",
            "current_time": 1636148368
        }
    },
    "licenses": 1
}


