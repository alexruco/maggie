# setup.py

from setuptools import setup, find_packages

setup(
    name="maggie",  # Name of your package
    version="0.1.0",  # Version of your package
    author="Alex Ruco",  # Author name
    author_email="alex@ruco.pt",  # Author email
    description="Maggie, your SEO copilot.",  # Short description of the package
    long_description=open("README.md").read(),  # Long description from the README file
    long_description_content_type="text/markdown",  # Content type for the long description
    url="https://github.com/alexruco/maggie",  # URL for the project (e.g., GitHub repository)
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[  # Classifiers help users find your project by categorizing it
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the Python version compatibility
    install_requires=[  # List of dependencies
        "numpy",
        "requests",
        # Add other dependencies as needed
    ],
    entry_points={  # Entry points for executable scripts
        "console_scripts": [
            "my_module=my_python_module.module:main_function",
        ],
    },
)
