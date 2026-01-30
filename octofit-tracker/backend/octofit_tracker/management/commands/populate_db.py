from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Delete existing data in dependency order
        models.Activity.objects.all().delete()
        models.Workout.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        get_user_model().objects.all().delete()
        models.Team.objects.all().delete()

        # Create teams
        marvel = models.Team.objects.create(name='Team Marvel')
        dc = models.Team.objects.create(name='Team DC')

        # Create users
        ironman = get_user_model().objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = get_user_model().objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = get_user_model().objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = get_user_model().objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create activities
        models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        models.Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)

        # Create workouts
        models.Workout.objects.create(user=captain, name='Pushups', reps=50)
        models.Workout.objects.create(user=superman, name='Situps', reps=100)

        # Create leaderboard
        models.Leaderboard.objects.create(user=ironman, score=100)
        models.Leaderboard.objects.create(user=batman, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
