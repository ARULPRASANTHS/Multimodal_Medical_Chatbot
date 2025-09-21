from setuptools import find_packages, setup

setup(
    name='generative_ai_project',
    version='0.0.1',
    author='Arulprasanth S',
    author_email='arulbhigs2004@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # add dependencies here if needed
        # e.g., "numpy", "pandas"
    ],
)
