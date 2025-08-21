# Containerized Python CLI: `wordcount-tool`

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/triv321/docker-wordcount)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Docker](https://img.shields.io/badge/docker-latest-blue.svg)](https://www.docker.com/)

> A professional, optimized Docker image for the `wordcount-tool`, a command-line utility for word frequency analysis. This project demonstrates best practices in containerization, including multi-stage builds for small and secure final images.

---

## Table of Contents
1.  [Overview](#overview)
2.  [Core Features](#core-features)
3.  [Installation & Setup](#installation--setup)
4.  [Usage](#usage)
5.  [Project Details](#project-details)
6.  [Development](#development)

## Overview

This project addresses a core challenge in modern software engineering: creating portable, reproducible, and optimized application environments. It takes the `wordcount-tool`—a professional Python package—and containerizes it using Docker.

The focus of this exercise was not just to make the application run in a container, but to do so following industry best practices. This involved a deep dive into `Dockerfile` optimization, culminating in a **multi-stage build** that separates the build-time environment from the final runtime environment. The result is a final image that is significantly smaller, faster to deploy, and more secure than a naive, single-stage build.

## Core Features

* **Optimized Image:** Utilizes a multi-stage `Dockerfile` to produce a minimal final image, reducing size and attack surface.
* **Portable:** The containerized application can run on any system (Windows, macOS, Linux) with Docker installed, eliminating the "it works on my machine" problem.
* **Production-Ready:** Follows best practices for containerization, including using lightweight base images and a clean, logical `Dockerfile` structure.
* **Reusable:** The final image is a self-contained, executable tool that can be easily integrated into larger automated workflows.

## Installation & Setup

To build and run this containerized application on a fresh system, you will need the following prerequisites.

### Prerequisites
* **Git:** To clone the project repository.
* **Docker:** The Docker engine must be installed and running.

### Installation Instructions
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/triv321/dockerized_wordCount_Project.git
    cd dockerized_wordCount_Project
    ```

2.  **Build the Docker image:**
    This command reads the `Dockerfile` and builds the final, optimized image, tagging it as `wordcount-image`.
    ```bash
    docker build -t wordcount-image .
    ```

## Usage

Once the image is built, you can use the `docker run` command to execute the `wordcount-tool` inside a container.

### Example
To count the words in a local text file, you must mount the file's directory into the container using a bind mount (`-v`).

1.  **Create a sample file on your host machine:**
    ```bash
    echo "hello docker world hello" > sample.txt
    ```

2.  **Run the container and pass the file as an argument:**
    ```bash
    docker run -v "$(pwd)":/app wordcount-image sample.txt
    ```

### Expected Output
The command will print the formatted word count to your terminal:
--- Word Counts ---hello: 2world: 1
## Project Details

### Design Decisions

#### Multi-Stage Build
The core architectural choice for this project was the use of a **multi-stage `Dockerfile`**. This was done for two primary reasons:
1.  **Size Optimization:** The first stage, named `builder`, uses a full `python:3.9` image to create a virtual environment and install all dependencies, including build-time tools like `setuptools`. The final stage starts from a clean `python:3.9-slim` image and copies *only* the populated virtual environment from the `builder`. This leaves all the source code, tests, and build tools behind, resulting in a significantly smaller final image.
2.  **Security:** The final image has a reduced attack surface. Since it does not contain the source code or build tools, there are fewer potential vulnerabilities for an attacker to exploit.

#### `ENTRYPOINT` vs. `CMD`
The final image uses a combination of `ENTRYPOINT` and `CMD` to create an executable container that behaves like a standard command-line tool.
* **`ENTRYPOINT ["wordcount"]`**: This sets the main, immutable command for the container. The container *is* the `wordcount` tool.
* **`CMD ["--help"]`**: This provides a default argument. If the container is run without any arguments, it will execute `wordcount --help`. If a user provides an argument (like a filename), it will override the `CMD` and be passed to the `ENTRYPOINT`.

## Development

### Testing
The project includes a full suite of unit tests for the underlying Python application. These tests should be run *before* building the Docker image to ensure the application logic is correct.

1.  **Set up the environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -e .
    pip install pytest pytest-cov
    ```

2.  **Run the tests:**
    From the project's root directory, run `pytest` with the coverage flag.
    ```bash
    pytest --cov=wordcount_tool
    ```
