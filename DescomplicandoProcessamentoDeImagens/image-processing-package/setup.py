from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="DescomplicandoProcessamentoDeImagens",
    version="0.0.1",
    author="Antonio Bigas",
    author_email="antonio.bigas@gmail.com",
    description="DIO project",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Antoniobigas",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)