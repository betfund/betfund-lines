# betfund-lines

## Installation/Usage

From source
```bash
$ git clone https://github.com/betfund/betfund-lines.git
$ cd betfund-lines

$ python3.7 -m venv venv
$ pip install -e .

# For test dependencies
$ pip install -e ".[testing]"
```

## Environment Variables

+ RUNDOWN_API_HOST
    + `$ export RUNDOWN_API_HOST=yourHost`
    
    
+ RUNDOWN_API_KEY
    + `$ export RUNDOWN_API_KEY=yourSecretKey`


## Calling Client
The main runner is via `lines.main`

A caller will need to pass an argument `sport_id`