from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='python_core_homework_7',
    url='https://github.com/avtarso/python_core_homework_7',
    author='Anton Tarasov',
    author_email='t0676352927@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': [
            'clean_folder = clean_folder.clean:main',
        ],
    }
)