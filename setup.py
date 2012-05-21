from setuptools import setup, find_packages


setup(
    name = 'django-bot-statstic',
    version = '0.1.dev',
    author = 'Anikin Sergey',
    author_email = 'anikin@trilan.ru',
    description = 'Statistics for Django',
    packages = find_packages(),
    include_package_data=True,
    zip_safe = False,
)
