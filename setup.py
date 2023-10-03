import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="goporting-python",
    version="1.0.3",
    author="Threat Code",
    author_email="connect@w3security.tech",
    description="Python SDK for reverse shell sessions manager - Goporting v1.4.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThraetCode/Goporting-Python",
    packages=["goporting_python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Topic :: System :: Networking",
    ],
    python_requires='>=3.6',
    keywords='goporting, sdk, reverse shell',
    install_requires=["requests"],
)