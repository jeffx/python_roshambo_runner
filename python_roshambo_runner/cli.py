import python_roshambo_runner
import argparse


def process_command_line_args():
    parser = argparse.ArgumentParser(description='RoShamBo')
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    return args


def cli():
    args = process_command_line_args()
    if args.test:
        python_roshambo_runner.RoShamBo.test_bots()
    else:
        rps = python_roshambo_runner.RoShamBo()
        rps.run_tourney()
        rps.generate_results()
        print(rps.result_table)
