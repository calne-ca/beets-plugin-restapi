from setuptools import setup

setup(
    name='beets-rest-api',
    version='0.2.1',
    description='beets plugin that provides a basic REST api',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Joscha Düringer',
    author_email='joscha.dueringer@beardbot.net',
    url='https://github.com/calne-ca/beets-rest-api',
    license='MIT',
    platforms='ALL',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.4.7',
        'mediafile==0.6.0',
        'pillow==8.1.0',
        'flask'
    ],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
