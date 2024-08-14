import setuptools

with open('README.md', mode='r', encoding='utf-8') as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setuptools.setup(
    name='lang-sam',
    version='0.1.1',
    author='Luca Medeiros',
    author_email='lucamedeiros@outlook.com',
    description='Language segment-anything',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/luca-medeiros/lang-segment-anything',
    project_urls={
        'Bug Tracker': 'https://github.com/luca-medeiros/lang-segment-anything/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=requirements)
