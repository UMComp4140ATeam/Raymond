from tst import evaluate_test
import unittest

suite = unittest.TestLoader().loadTestsFromTestCase(evaluate_test.EvaluateLayerTest)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(evaluate_test.EvaluateCircuitTest)
unittest.TextTestRunner(verbosity=2).run(suite)
