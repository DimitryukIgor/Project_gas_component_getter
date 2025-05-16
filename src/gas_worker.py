from csv import DictReader
from datetime import datetime
from pathlib import Path

from src.gas_parametrs import GasParametrs


class GasWorker:
    def __init__(self):
        self._gas_params_list: list[GasParametrs] = []

    def get_gas_params_from_file(self, filename: str | Path):
        with open(filename, "r") as csvfile:
            dict_reader = DictReader(csvfile, delimiter="\t", quotechar="|")
            self._gas_params_list = []
            for line in dict_reader:
                obj = GasParametrs(
                    tabs=datetime.strptime(line["Tabs"],"%d.%m.%Y %H:%M:%S"),
                    trel=int(line["Trel"]),
                    h_2=float(line["H2(%)"]),
                    co=float(line["CO(%)"]),
                    co_2=float(line["CO2(%)"]),
                    ch_4=float(line["CH4(%)"]),
                    comments=line["Comments"],
                )
                self._gas_params_list.append(obj)


