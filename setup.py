import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='just-pkg-kosciej',  # Replace with your own username
    version='0.0.1',
    author='Krystian',
    author_email='a@a.pl',
    description='A small example package',
    install_requires=['tenacity'],
    entry_points={'console_scripts': ['skrypcik = mycode.som:main', 'lepszy = mycode.som:inny']},
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
