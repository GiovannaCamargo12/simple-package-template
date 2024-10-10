from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_imagem",
    version="0.0.1",
    author="my_name",
    author_email="my_email",
    description="combina as imagens",
    long_description="combina as imagens",
    long_description_content_type="combina as imagens/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
