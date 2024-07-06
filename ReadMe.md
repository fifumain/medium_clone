# IMPORTANT UPDATE

It is with great regret that I state that the project has not been rolled out at this time, as there is no way to fund all components of its work. It will definitely come back better, and bigger! te.

# Medium clone by FIFU

Welcome! This project is a clone of the popular medium.com website. At the moment created only the backend component of the site.

## Table of Contents

- [Introduction](#introduction)
- [Roadmap](#roadmap)
- [Documentation](#documentation)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Running tests](#running-tests)
- [Screenshots](#screenshots)
- [Feedback and contributing](#feedback--contributing)
- [Authors](#authors)
- [License](#license)

## Introduction

This project is a website where everyone can view various articles, leave reactions and feedback, and add articles to their bookmarks. Registration is required to use most of the features, and there is a specially designed user-friendly system that includes various security checks such as email verification, etc. This project is currently deployed, with addresses both above and below. The deployment utilized docker, a virtual computer, and a bash script that utilizes archiving the project, and further deploying and running it on a remote server.

## Roadmap

- Upgrade the logging system.

- Add cache system.

- Integrate login via socials.

- Develop the frontend part.

## Documentation

Visit [API Documentation](fifumain.site/redoc/) to see all available API requests.

## Prerequisites

Before using this code, I would like to warn you that this is only a build for local development, the production version is not for distribution.
You need to have Python and Docker installed. Code developen and testet at Python v3.11.5 .

## Installation

- Clone repository:
  `git clone https://github.com/fifumain/medium_clone.git`
- Install required libraries, using the command line:
  `pip install -r local.txt`
- Change variables in envs/local.
- Run: `make build`

## Configuration

- Edit `.envs/local` files in the root directory and configure your environment variables.

## Usage

See Makefile for available usage commands.

## Running Tests {#running-tests}

To run tests, run the following command

```bash
  docker compose -f local.yml run --rm api pytest -p no:warnings  --cov-report html
```

## Screenshots

Here you can see some API [documentation](fifumain.site/redoc/)

![App Screenshot](https://i.imgur.com/s1HEeEY_d.webp?maxwidth=1520&fidelity=grand)

## Feedback and Contributing {#feedback--contributing}

If you have any feedback or contributing ideas, please reach out to me at pustovoitenkofilip@gmail.com

## Authors

- [@fifumain](https://www.github.com/fifumain)

## License

This project is licensed under the Apache License 2.0.
