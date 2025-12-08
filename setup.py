from setuptools import setup, find_packages

setup(
    name = "github_activity",
    version = "0.1.0",
    description="CLI tool to fetch and display recent GitHub events for a user",
    author = "Average-Chief",
    packages = find_packages(),
    install_requires=[
        "requests",
        "rich"
    ],
    entry_points={
        "console_scripts": ["github-activity=github_events.cli:main"],},
    python_requires='>=3.8',
)