from argparse import ArgumentParser
from pathlib import Path

from src.gas_worker import GasWorker

def process_file(gas_worker, file_path):
    file = Path(file_path)
    if not file.exists():
        print(f"❌ Ошибка: файл {file} не найден!")
        return False

    try:
        gas_worker.get_gas_params_from_file(file)
        area = gas_worker.get_area()
        gas_worker.print_concentration_results(*area)
        return True
    except Exception as e:
        print(f"❌ Ошибка при обработке файла: {e}")
        return False

def main():
    parser = ArgumentParser(
        description="Программа для анализа пиролизного газа (TEST-1)"
    )
    parser.add_argument(
        "-f", "--file",
        type=Path,
        help="Путь к файлу (если не указан, программа перейдет в интерактивный режим)"
    )
    args = parser.parse_args()

    gas_worker = GasWorker()

    # Режим с аргументом (без цикла)
    if args.file:
        success = process_file(gas_worker, args.file)
        if not success:
            print("Завершение с ошибкой.")
        return  # Выход после обработки файла

    # Интерактивный режим (с циклом)
    while True:
        print("\n" + "=" * 50)
        file_path = input("Введите путь к файлу (или 'exit' для выхода): ").strip().replace('"', '').replace("'", "")

        if file_path.lower() in ('exit', 'quit', 'q'):
            print("Завершение программы...")
            break

        process_file(gas_worker, file_path)

if __name__ == "__main__":
    main()