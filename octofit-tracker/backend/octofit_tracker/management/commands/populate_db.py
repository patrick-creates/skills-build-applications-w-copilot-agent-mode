from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Drop and recreate the database tables to ensure a clean state
        from django.core.management import call_command
        call_command('flush', '--no-input')

        # Ensure users are only added if they do not already exist
        users = [
            User.objects.get_or_create(username='thundergod', email='thundergod@mhigh.edu', defaults={'password': 'password123'})[0],
            User.objects.get_or_create(username='metalgeek', email='metalgeek@mhigh.edu', defaults={'password': 'password123'})[0],
            User.objects.get_or_create(username='zerocool', email='zerocool@mhigh.edu', defaults={'password': 'password123'})[0],
            User.objects.get_or_create(username='crashoverride', email='crashoverride@mhigh.edu', defaults={'password': 'password123'})[0],
            User.objects.get_or_create(username='sleeptoken', email='sleeptoken@mhigh.edu', defaults={'password': 'password123'})[0],
        ]

        # Save users individually to ensure they are persisted in the database
        for user in users:
            user.save()

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3], users[4])

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=90),
            Leaderboard(user=users[2], score=95),
            Leaderboard(user=users[3], score=85),
            Leaderboard(user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
