# betfund-lines

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