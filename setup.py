from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cosmic-resonance-evaluation",
    version="1.0.0",
    author="Cosmic Researcher",
    author_email="cosmic@resonance.universe",
    description="Cosmic Resonance Evaluation - Universal Consciousness Principles & Mathematical Foundation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cosmic-researcher/cosmic-resonance-evaluation",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "networkx>=2.6.0",
        "sentence-transformers>=2.2.0",
        "torch>=2.0.0",
        "transformers>=4.30.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "cosmic-eval=cosmic_resonance_evaluation.cosmic_evaluator:main",
            "cosmic-workbench=cosmic_resonance_evaluation.cosmic_workbench:main",
        ],
    },
    package_data={
        "cosmic_resonance_evaluation": ["py.typed"],
    },
    include_package_data=True,
    zip_safe=False,
)
