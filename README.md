# betfund-lines

<p align="center">
<a href="https://github.com/betfund/betfund-lines/workflows/betfund-lines/"><img alt="Build Status" src="https://github.com/betfund/betfund-lines/workflows/betfund-lines/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Installation/Usage

From source
```bash
$ git clone https://github.com/betfund/betfund-lines.git
$ cd betfund-lines

$ python3.7 -m venv venv
$ pip install -e .
```

## Environment Variables

+ RUNDOWN_HOST
    + `$ export RUNDOWN_API_HOST=yourHost`
    
    
+ RUNDOWN_KEY
    + `$ export RUNDOWN_API_KEY=yourSecretKey`

## Testing
```bash
# For test dependencies
$ pip install -e ".[testing]"

$ make tests
```