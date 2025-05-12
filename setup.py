from setuptools import setup, find_packages

setup(
    name='tube_scriptor',
    version='2025.5.120740',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='A package for generating transcripts from YouTube videos in various formats',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/tube_scriptor',
    packages=find_packages(),
    install_requires=[
        'xmltodict',
        'requests',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
