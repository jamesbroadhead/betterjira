# TEST

This is currently a skeleton of a repo - code coming soon!

# BetterJira

A python library to improve working with Jira programatically.

This library mostly exists to solve one problem - needing to refer to fields by field-id ("customfield1234") rather than human-readable name.
If you work with Jira installs which have many custom fields, this will help!

## Usage
```python
from Jira import Jira
from betterjira import BetterJira

_jira = JIRA(server, basic_auth=(username, password), max_retries=0)
jira = BetterJira(_jira)

issue = jira.find_single_ticket('PROJECT AND status = Resolved')

# omg, so easy!
value = issue.get_field('MY CUSTOM FIELD')
```

## Development

### Testing
```tox```
