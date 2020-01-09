from django.test import TestCase
from answers.models import Answer

class CreateAnswerTest(TestCase):
    def test_create_answer_should_save_model(self):
        response = self.client.post('/create_answer/add', data={'text':'yes','image':'http://yesno.wtf/api/?force=yes'})
        actual = Answer.objects.last()
        expected = {'text' : 'yes','image':'http://yesno.wtf/api/?force=yes'}
        self.assertEqual(actual.text, expected['text'])
        self.assertEqual(actual.image, expected['image'])

    def (parameter_list):
        pass