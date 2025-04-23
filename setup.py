from setuptools import setup, find_packages

setup(
    name="prompt_engineering",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai==1.75.0",
        "python-dotenv==1.1.0",
        "pydantic>=2.7.0,<3.0.0",
        "pydantic_settings==2.9.1",
        "typing-extensions>=4.8.0",
    ],
) 