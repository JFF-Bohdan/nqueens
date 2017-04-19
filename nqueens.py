#!/usr/bin/env python3

from optparse import OptionParser
from system.logs_support import init_logger
from system.stopwatch import Stopwatch
import signal
from system.solver_impl import NQueensProblemSolverWrapper

def signal_handler(signal, frame):
    """
    Handler for Ctrl-C combination. Terminates program execution

    :param signal:
    :param frame:
    :return: None
    """
    print()
    print("Quit by Ctrl-C")
    print()
    exit(0)

def solution_log_printer(solution, logger):
    """
    Prints solution to log file

    :param solution: solution data
    :param logger: logger
    :return: None
    """
    sz = len(solution)
    s = []
    for i in range(sz):
        s.append(" ".join(['Q' if v else '_' for v in solution[i]]))

    logger.info("solution:\n{}".format("\n".join(s)))

def main():
    logger = init_logger()

    # parsing command line
    parser = OptionParser()
    parser.add_option("-d", "--dimensions", type=int, dest="dimensions", default=8, help="Dimensions for chess board")
    parser.add_option("-p", "--printsolutions", action="store_true", dest="print_solutions", default=False, help="Prints solutions")

    (cmd_line_options, args) = parser.parse_args()
    if (cmd_line_options.dimensions is None) or (cmd_line_options.dimensions < 0):
        logger.error("Error: please specify correct value for chessboard size.")
        return -1

    # initializing solver wrapper
    watch = Stopwatch(True, True, True)
    solver = NQueensProblemSolverWrapper(logger, cmd_line_options.dimensions)

    # tuning to print solutiong to log if necessary
    if cmd_line_options.print_solutions:
        solver.solution_handler_kwargs = {
            "logger": logger
        }
        solver.solution_handler = solution_log_printer

    # looking for solutions
    if not solver.process():
        logger.error("Solving error: {}".format(solver.errorText))
        return -2

    # printing work time
    logger.info("total solutions count - {}".format(solver.total_solutions_count))
    logger.info("done at {}".format(watch))
    return 0

if __name__ == "__main__":
    # initializing Ctrl-C handler
    signal.signal(signal.SIGINT, signal_handler)

    ret = main()
    print("Done")
    exit(0)
