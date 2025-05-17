from argparse import ArgumentParser
from pathlib import Path

from src.gas_worker import GasWorker


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        description="Программа для получения концентраций компонентов пиролизного газа полученных в газоанализаторе ТЕСТ-1 (Россия)"
    )
    arg_parser.add_argument(
        "-f", "--file_name", type=Path, help="Путь до файла с замерами"
    )
    args = arg_parser.parse_args()
    file = args.file_name
    gas_worker = GasWorker()
    gas_worker.get_gas_params_from_file(file)
    area = gas_worker.get_area()
    gas_worker.print_concentration_results(*area)