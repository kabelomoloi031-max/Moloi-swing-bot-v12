from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="moloi-swing-bot",
    version="1.0.0",
    author="kabelomoloi031-max",
    description="AI Swing Trading Assistant for MT5 using Google Gemini AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kabelomoloi031-max/Moloi-swing-bot-v12",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "streamlit>=1.36.0",
        "google-generativeai>=0.3.0",
        "Pillow>=10.2.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "moloi-swing-bot=app:main",
        ],
    },
)
