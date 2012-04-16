import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from polls.models import Poll, Choice

class PollsViewsTestCase(TestCase):
    fixtures = ['polls_views_testdata.json']

    def test_index(self):

        resp = self.client.get(reverse('polls_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_poll_list' in resp.context)
        self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']],[1])
        poll_1 = resp.context['latest_poll_list'][0]
        self.assertEqual(poll_1.question, 'What\'s new?')
        self.assertEqual(poll_1.choice_set.count(), 3)
        choices = poll_1.choice_set.all()
        self.assertEqual(choices[0].choice, 'Not Much')
        self.assertEqual(choices[0].votes, 0)
        self.assertEqual(choices[1].choice, 'The Sky')
        self.assertEqual(choices[1].votes, 3)
        self.assertEqual(choices[2].choice, 'Just hacking again')
        self.assertEqual(choices[2].votes, 1)

    def test_detail(self):
          resp = self.client.get(reverse('polls_detail', kwargs={'pk': 1}))
          self.assertEqual(resp.status_code, 200)
          self.assertEqual(resp.context['poll'].pk, 1)
          self.assertEqual(resp.context['poll'].question, 'What\'s new?')

          # Ensure that non-existent polls throw a 404.
          resp = self.client.get('/polls/2/')
          self.assertEqual(resp.status_code, 404) 

    def test_results(self):
          resp = self.client.get(reverse('polls_detail', kwargs={'pk': 1}))
          self.assertEqual(resp.status_code, 200)
          self.assertEqual(resp.context['poll'].pk, 1)
          self.assertEqual(resp.context['poll'].question, 'What\'s new?')

          # Ensure that non-existent polls throw a 404.
          resp = self.client.get(reverse('polls_detail', kwargs={'pk': 2}))
          self.assertEqual(resp.status_code, 404)   
          
    def test_good_vote(self):
          poll_1 = Poll.objects.get(pk=1)
          self.assertEqual(poll_1.choice_set.get(pk=1).votes, 0)

          resp = self.client.post(reverse('polls_vote', kwargs={'poll_id': 1}), {'choice': 1})
          self.assertEqual(resp.status_code, 302)
          self.assertEqual(resp['Location'], 'http://testserver/polls/1/results/')

          self.assertEqual(poll_1.choice_set.get(pk=1).votes, 1)      
          
    def test_bad_votes(self):
          # Ensure a non-existant PK throws a Not Found.
          resp = self.client.post(reverse('polls_vote', kwargs={'poll_id': 1000000}))
          self.assertEqual(resp.status_code, 404)

          # Sanity check.
          poll_1 = Poll.objects.get(pk=1)
          self.assertEqual(poll_1.choice_set.get(pk=1).votes, 0)

          # Send no POST data.
          resp = self.client.post(reverse('polls_vote', kwargs={'poll_id': 1}))
          self.assertEqual(resp.status_code, 200)
          self.assertEqual(resp.context['error_message'], "You didn't select a choice.")

          # Send junk POST data.
          resp = self.client.post(reverse('polls_vote', kwargs={'poll_id': 1}), {'foo': 'bar'})
          self.assertEqual(resp.status_code, 200)
          self.assertEqual(resp.context['error_message'], "You didn't select a choice.")

          # Send a non-existant Choice PK.
          resp = self.client.post(reverse('polls_vote', kwargs={'poll_id': 1}), {'choice': 300})
          self.assertEqual(resp.status_code, 200)
          self.assertEqual(resp.context['error_message'], "You didn't select a choice.")
          
                           