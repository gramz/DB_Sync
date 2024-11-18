from setuptools import setup, find_packages

setup(
    name="db_sync",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pyodbc>=4.0.39',
        'mysql-connector-python>=8.0.33',
        'schedule>=1.2.0',
        'python-dotenv>=1.0.0',
    ],
    author="Guillermo Ramirez",
    author_email="ramirezjose@umes.edu.gt",
    description="Herramienta de sincronización entre SQL Server y MySQL",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
)
