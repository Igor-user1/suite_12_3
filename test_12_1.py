import runner
import unittest


class RunnerTest(unittest.TestCase):
    """Проверим на юниттесте класс Runner из модуля runner.py"""
    is_frozen = False

    def walk_object(self, some_object):     # Метод для вызывания метода walk класса Runner
        for i in range(10):
            some_object.walk()

    def run_object(self, some_object):      # Метод для вызывания метода run класса Runner
        for i in range(10):
            some_object.run()

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        some_object1 = runner.Runner('some_obj1')       # Создаем произвольный объект класса и тестируем его
        self.walk_object(some_object1)
        self.assertEqual(some_object1.distance, 50)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        some_object2 = runner.Runner('some-obj2')       # Создаем произвольный, но другой объект класса и тестируем его
        self.run_object(some_object2)
        self.assertEqual(some_object2.distance, 100)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):                   # Создаем два произвольных объекта класса Runner и тестируем их
        some_object3 = runner.Runner("name1")   # на двух разных методах класса
        some_object4 = runner.Runner("name1")

        self.walk_object(some_object3)
        self.walk_object(some_object3)
        self.run_object(some_object4)
        self.run_object(some_object4)

        self.assertNotEqual(some_object3.distance, some_object4.distance)


if __name__ == '__main__':      # Запускаем наш тест-кейс
    unittest.main()
