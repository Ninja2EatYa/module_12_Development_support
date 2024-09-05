import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_obj_1 = runner.Runner('John')
        for i in range(10):
            runner_obj_1.walk()
        self.assertEqual(runner_obj_1.distance, 50)

    def test_run(self):
        runner_obj_2 = runner.Runner('Mike')
        for i in range(10):
            runner_obj_2.run()
        self.assertEqual(runner_obj_2.distance, 100)

    def test_challenge(self):
        runner_obj_3 = runner.Runner('Katie')
        runner_obj_4 = runner.Runner('Maggie')
        for i in range(10):
            runner_obj_3.run()
            runner_obj_4.walk()
        self.assertNotEqual(runner_obj_3.distance, runner_obj_4.distance)


if __name__ == '__main__':
    unittest.main()