import unittest
import test_12_1_Проверка_на_выносливость
import test_12_2_Проверка_на_выносливость

TestSuite_RT = unittest.TestSuite()
TestSuite_RT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1_Проверка_на_выносливость.RunnerTest))
TestSuite_RT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2_Проверка_на_выносливость.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(TestSuite_RT)

