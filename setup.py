import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'example_pkg',
    version = '0.0.1',
    author = 'wanghong',
    author_email = 'author@example.com',
    description = 'A small example package',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/pypa/sampleproject',
    packages = setuptools.find_packages(),
    classifiers=[
        'programming language :: python :: 3',
        'license :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)