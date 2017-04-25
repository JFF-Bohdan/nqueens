from system.shared import LastErrorHolder


class NQueensProblemRecursiveSolver(LastErrorHolder):
    """
    N-Queens problem solver. Recursive implementation
    """
    def __init__(self, dimensions):
        if dimensions <= 0:
            raise ValueError("dimenstions must be > 0")

        super().__init__()
        self.dimensions = dimensions

        # initializing empty board
        self.board = [[0] * self.dimensions for stub in range(self.dimensions)]

    def __canSet(self, row, col):
        """
        Checks ability to set 1 in needful row and column
        :param row: row number
        :param col: column number
        :return: True when 1 can be set in given row and column, otherwise returns False
        """

        if self.board[row][col]:
            return False

        # checking in this row on left side
        for i in range(0, col):
            if self.board[row][i]:
                return False

        # checking upper diagonal on left side
        i = row
        j = col
        while (i >= 0) and (j >= 0):
            if self.board[i][j]:
                return False

            i -= 1
            j -= 1

        # checking lower diagonal on left side
        i = row
        j = col
        while (j >= 0) and (i < self.dimensions):
            if self.board[i][j]:
                return False

            i += 1
            j -= 1

        return True

    def __solve_worker(self, col=0):
        """
        Low level generator of solutions
        :param col: column to calculate
        :return: solutions
        """

        if col == self.dimensions:
            yield self.board
            return

        for i in range(0, self.dimensions):
            if self.__canSet(i, col):
                self.board[i][col] = 1

                yield from self.__solve_worker(col + 1)

                self.board[i][col] = 0

    def solve(self):
        """
        Soltions generator. Calculates all solutions and returns them

        :return: problem solutions
        """
        yield from self.__solve_worker(0)


class NQueensProblemSolverWrapper(LastErrorHolder):
    """
    Wrapper for N-Queens problem solution. Can find all solutions, count total solutions
    count and execute callback function.

    Callback function can process solutions. For example: print them to log, print to
    file or save int database
    """
    def __init__(self, logger, dimensions, cls=NQueensProblemRecursiveSolver):
        """
        Initializer for wrapper

        :param logger: logger
        :param dimensions: chessboard dimensions
        :param cls: worker class
        """
        super().__init__()

        self.dimensions = dimensions

        self.worker = cls(self.dimensions)

        self.logger = logger
        self.total_solutions_count = 0

        self.solution_handler = None
        self.solution_handler_kwargs = None

    def __handle_solution(self, solution):
        if self.solution_handler is None:
            return

        if self.solution_handler_kwargs is None:
            self.solution_handler(solution)
            return

        self.solution_handler(solution, **self.solution_handler_kwargs)

    def process(self):
        self.logger.debug("solver initialized for chessboard size: {}".format(self.dimensions))

        have_callback = (self.solution_handler is not None)

        for solution in self.worker.solve():
            if have_callback:
                self.__handle_solution(solution)

            self.total_solutions_count += 1

        if self.total_solutions_count == 0:
            return self.setError("no solutions found")

        self.logger.info("solutions search complete, found solutions count: {}".format(self.total_solutions_count))
        return True
