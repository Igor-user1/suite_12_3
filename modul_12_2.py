import unittest         # импортируем библеотеку unittest и задания из модуля runner
import runner


class TournamentTest(unittest.TestCase):        #Создаем класс унаследованный от класса TestCase

    is_frozen = True
    def setUp(self):
        self.runner1 = runner.Runner('Usain', 10)       #Создаем объекты с которыми будем рабоать
        self.runner2 = runner.Runner('Андрей', 9)
        self.runner3 = runner.Runner('Nik', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}        # создаем список со всеми результатами

    @classmethod
    def tearDownClass(cls):         #Выводим список с результатами на экран
        dict_ = {}                  # ключ - это номер прибытия, а значение - это имя
        for result in cls.all_results:
            dict_[result] = cls.all_results[result].name
        print(dict_)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_start1(self):      # первое тестирование Usain и Nik
        tournament_object = runner.Tournament(90, self.runner1, self.runner3)
        self.all_results.update(tournament_object.start())
        self.assertTrue(self.all_results[2] == self.runner3.name)
        self.tearDownClass()

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_start2(self):      # второе тестирование Андрей и Nik
        tournament_object = runner.Tournament(90, self.runner2, self.runner3)
        self.all_results.update(tournament_object.start())
        self.assertTrue(self.all_results[2] == self.runner3.name)
        self.tearDownClass()

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_start3(self):      # третье тестирование Usain, Андрей  и Nik
        tournament_object = runner.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.update(tournament_object.start())
        self.assertTrue(self.all_results[3] == self.runner3.name)
        self.tearDownClass()


if __name__ == '__main__':      # Запускаем наш тест-кейс
    unittest.main()
