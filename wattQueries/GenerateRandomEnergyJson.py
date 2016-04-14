from datetime import datetime, timedelta
import random, json

def createTime(timestamp):
    year = str(timestamp.year)
    month = str(timestamp.month) if len(str(timestamp.month)) == 2 else "0" + str(timestamp.month)
    day = str(timestamp.day) if len(str(timestamp.day)) == 2 else "0" + str(timestamp.day)
    hour =  str(timestamp.hour) if len(str(timestamp.hour)) == 2 else "0" + str(timestamp.hour)
    minute = str(timestamp.minute) if len(str(timestamp.minute)) == 2 else "0" + str(timestamp.minute)
    second = str(timestamp.second) if len(str(timestamp.second)) == 2 else "0" + str(timestamp.second)
    time = year+"-"+month+"-"+day+"T"+hour+":"+minute+":"+second+".000000Z"

    return time

def createFakeRecords(BA, yearsBack):
    fakeData = []
    timestamp = datetime.now()
    now = createTime(datetime.now())
    interval = timedelta(minutes=5)
    records = yearsBack * 365 * 24 * 60 / 5

    for i in range(records):
        timestamp = timestamp - interval
        data={}
        data["genmix_biogas_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["market"] = "RT5M"
        data["genmix_biomass_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["genmix_solar_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["genmix_nonwind_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["genmix_renewable_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["genmix_wind_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["genmix_nuclear_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["ba"] = BA
        data["genmix_thermal_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["timestamp"] = createTime(timestamp)
        data["genmix_coal_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["carbon"] = str(round(abs(random.gauss(10000,5000))))
        data["freq"] = "5m"
        data["genmix_refuse_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["genmix_other_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["genmix_natgas_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        data["url"] = "https://api.watttime.org/api/v1/datapoints/4682208/"
        data["created_at"] = now
        data["genmix_hydro_gen_MW"] = str(round(abs(random.gauss(10000,5000))))
        fakeData.append(data)

    return fakeData


missing = ["WAUE",
"DEAA",
"EKPC",
"WAUW",
"CLEC",
"OVEC",
"WKPL",
"IID",
"PLUM",
"SPS",
"OPPD",
"HST",
"RC",
"TAL",
"SPA",
"NEVP",
"AEPW",
"OKGE",
"WMUC",
"PACW",
"PUPP",
"PACE",
"MPCO",
"SCEG",
"LGEE",
"EES",
"TID",
"AEC",
"EEI",
"SCL",
"GVL",
"CEA",
"BUBA",
"GCPD",
"NPPD",
"WFEC",
"AMPL",
"BREC",
"MPS",
"GRDA",
"KCPL",
"SPPC",
"BCA",
"OMLP",
"SMUD",
"SECI",
"TEC",
"SEC",
"HGMA",
"TVA",
"LAFA",
"DUK",
"TEPC",
"ELE",
"SRP",
"JEA",
"HEC",
"LEPA",
"EDE",
"SOCO"
"LES",
"PSCO",
"SC",
"CPLW",
"WALC",
"PSEI",
"DERS",
"DPC",
"CNWY",
"PGE",
"NLRK",
"LDWP",
"KACY",
"FPC",
"AECI",
"AZPS",
"FPL",
"SMEE",
"DOPD",
"NYISO",
"GRIF",
"AVA",
"WACM",
"IPCO",
"TPWR",
"PNM",
"CHPD"]

for name in missing:
    fakes = createFakeRecords(name, 3)
    with open(name + "_fake_data.json", "w") as f:
        for fake in fakes:
            f.write(json.dumps(fake) + "\n")