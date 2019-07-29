from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):#1

    def setUp(self):#3
        self.browser = webdriver.Firefox()

    def tearDown(self):#3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):#2
        # Edith ouviu falar de uma nova aplicação online interessante
        # para lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o título da página e o cabeçalho mencionam
        # listas de tarefas(to-do)
        self.assertIn('To-Do', self.browser.title)#4
        self.fail('Finish the test!')#5

        # Ela é convidada a inserir um item de tarefa imediatamente
        # Ela digita "Buy peackoc feathers" (Comprar penas de pavão) em uma caixa
        # de texto (o hobby de Edith é fazer icas para pesca com fly)

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Buy peackok feathers" como um item em uma lista de tarefas

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # item. Ela insere "Use peackoc feathers to make a fly" (Usar penas de pavão
        # para fazer um fly - Edith é bem metódica)

        # A página é atualizada novamente e agora mostra os dois itens em sua lista
        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou um URL único para ela -- há um pequeno
        # texto explicativo para isso.

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir
if __name__ == '__main__':#6
    unittest.main(warnings='ignore')#7

