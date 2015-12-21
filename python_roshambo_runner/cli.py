import python_roshambo_runner

def cli():
    rps = python_roshambo_runner.RoShamBo()
    rps.run_tourney()
    rps.generate_results()
    print(rps.result_table)
