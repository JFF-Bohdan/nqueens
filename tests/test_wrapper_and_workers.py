import unittest
import logging
from system.solver_impl import NQueensProblemSolverWrapper


class TestSharedFunctions(unittest.TestCase):
    def test_n_queens_solver(self):

        logger = logging.getLogger(__name__)

        # testing correct solutions count
        correct_answers_counts = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
        sz = len(correct_answers_counts)
        for i in range(sz):
            wrapper = NQueensProblemSolverWrapper(logger, i + 1)
            ok = wrapper.process()

            # checking wrapper response (returns True when at least 1 solution found)
            if correct_answers_counts[i]:
                self.assertEqual(ok, True)

            # checking solutions count
            self.assertEqual(wrapper.total_solutions_count, correct_answers_counts[i])

        # checking for exception in case when dimensions count is less or equal to 0
        with self.assertRaises(ValueError):
            NQueensProblemSolverWrapper(logger, -1)

        with self.assertRaises(ValueError):
            NQueensProblemSolverWrapper(logger, 0)


if __name__ == "__main__":
    unittest.main()
