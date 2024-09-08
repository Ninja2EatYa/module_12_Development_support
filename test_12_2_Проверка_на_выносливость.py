import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.hussein = runner_and_tournament.Runner('Усейн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nick = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            for place, runner in result.items():
                print(f'{place}: {runner}', end='. ')
            print('')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_1(self):
        race = runner_and_tournament.Tournament(90, self.hussein, self.nick)
        results = race.start()
        self.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_2(self):
        race = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        results = race.start()
        self.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_3(self):
        race = runner_and_tournament.Tournament(90, self.hussein, self.andrey, self.nick)
        results = race.start()
        self.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == self.nick)


if __name__ == '__main__':
    unittest.main()
