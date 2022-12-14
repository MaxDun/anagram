import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="anagrams_minazuki",
    version="0.1",
    author="minazuki",
    description="This is a test package.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://git.foxminded.com.ua/minazuki/task-1-anagrams",
    packages=['anagrams'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)