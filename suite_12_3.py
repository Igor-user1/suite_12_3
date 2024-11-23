import unittest         #Импортируем нужные библиотеке и модули с предыдущими заданиями
import test_12_1
import modul_12_2

runner1 = unittest.TestSuite()          # создаем нужные объекты класса TestSuite, один для тестов Runner
                                        #другой для тестов Tournament
tournament = unittest.TestSuite()
#Далее добавляем соответствующие тесты для объектов класса TestSuite
runner1.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
tournament.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_2.TournamentTest))
#создаем объект класса TexttestRunner с уровнем 2
runner = unittest.TextTestRunner(verbosity=2)
#запускаем для ранее созданных объектов
runner.run(runner1)
runner.run(tournament)
