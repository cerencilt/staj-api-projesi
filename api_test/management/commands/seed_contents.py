# -*- coding: utf-8 -*-
import random
from django.core.management.base import BaseCommand
from api_test.models import Content

LANGUAGES = ['tr', 'en', 'es', 'ar']

TITLES = [
    'Getting Started with Django', 'Python for Beginners', 'Vue.js Fundamentals',
    'React Hooks Guide', 'CSS Grid Layouts', 'What is Docker',
    'PostgreSQL Tips and Tricks', 'Git and GitHub Essentials', 'Linux Commands',
    'Web Security Basics', 'Introduction to Machine Learning', 'What is Deep Learning',
    'Building Apps with FastAPI', 'Node.js Fundamentals', 'TypeScript Guide',
    'What is GraphQL', 'Using Redis', 'MongoDB Basics',
    'Introduction to Kubernetes', 'CI/CD Pipeline Explained',
]

DESCS = [
    'This content covers the fundamental concepts in a comprehensive way.',
    'You can reinforce the topic with step-by-step examples.',
    'Suitable for both beginners and advanced learners.',
    'Supported with real-world scenarios.',
    'A comprehensive guide with practical exercises.',
    'An up-to-date resource prepared with the latest information.',
    'Content ranging from basic concepts to advanced level.',
    'A guide supported with examples and explanations.',
]


class Command(BaseCommand):
    help = 'Create 100 dummy Content and save as fixture'

    def handle(self, *args, **kwargs):
        Content.objects.all().delete()
        self.stdout.write('All existing content has been deleted.')

        contents = []

        for i in range(1, 101):
            lang = LANGUAGES[i % len(LANGUAGES)]

            if i % 10 < 6:
                subtitle = random.choice([l for l in LANGUAGES if l != lang])
            else:
                subtitle = ''

            title = f'{random.choice(TITLES)} {i}'
            desc = random.choice(DESCS)
            draft = i % 100 < 15

            content = Content(
                title=title,
                desc=desc,
                source=f'https://example.com/content/{i}',
                clean_source=f'https://clean.example.com/content/{i}',
                languages=lang,
                subtitles=subtitle,
                draft=draft,
            )
            contents.append(content)

        Content.objects.bulk_create(contents)
        self.stdout.write(f'{Content.objects.count()} contents created.')

        from django.core import management
        with open('api_test/fixtures/contents.json', 'w', encoding='utf-8') as f:
            management.call_command('dumpdata', 'api_test.Content', stdout=f, indent=2)

        self.stdout.write(self.style.SUCCESS(
            '✅ Fixture saved: api_test/fixtures/contents.json'
        ))
