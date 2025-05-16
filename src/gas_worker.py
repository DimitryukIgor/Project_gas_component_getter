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
    def get_area(self) -> tuple[float]:
        area_h2 = 0.0
        area_co = 0.0
        area_co2 = 0.0
        area_ch4 = 0.0
        for i in range(1, len(self._gas_params_list)):
            time_diff = (
                self._gas_params_list[i].trel - self._gas_params_list[i-1].trel
            )
            area_h2 += (
                (self._gas_params_list[i].h_2 + self._gas_params_list[i-1].h_2)
                * time_diff / 2
            )
            area_co += (
                    (self._gas_params_list[i].co + self._gas_params_list[i - 1].co)
                    * time_diff / 2
            )
            area_co2 += (
                    (self._gas_params_list[i].co_2 + self._gas_params_list[i - 1].co_2)
                    * time_diff / 2
            )
            area_ch4 += (
                    (self._gas_params_list[i].ch_4 + self._gas_params_list[i - 1].ch_4)
                    * time_diff / 2
            )
        area = area_h2 + area_co + area_co2 + area_ch4
        return area_h2, area_co, area_co2, area_ch4, area

    @staticmethod
    def print_concentration_results(area_h2, area_co, area_co2, area_ch4, area):
        print(f"Концентрация H2 равна {round(area_h2 * 100 / area, 2)}")
        print(f"Концентрация CO равна {round(area_co * 100 / area, 2)}")
        print(f"Концентрация CO2 равна {round(area_co2 * 100 / area, 2)}")
        print(f"Концентрация CH4 равна {round(area_ch4 * 100 / area, 2)}")

