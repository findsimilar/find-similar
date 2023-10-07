# FindSimilar Laboratory

## Easy start

- Confirm migrations
```
cd laboratory
make migrate
```
- Run server
```
make server
```

## Use find_similar core function

Instead of:
```python
from find_similar import find_similar  # You will get import error in this case
```

Use:
```python
from django.conf import settings
settings.FIND_SIMILAR('none', ['one', 'two'])
settings.TOKENIZE('some text')
```

Or if you don't like UPPER_CASE:
```python
from django.conf import settings
find_similar = settings.FIND_SIMILAR
tokenize = settings.TOKENIZE

find_similar('none', ['one', 'two'])
tokenize('some text')
```

Looks weird, please make pull request if you find a better way

## Management commands

### Get tokens from one text

Input:
```commandline
python manage.py tokenize_one "some text" "other text"
```

Output:
```commandline
Get tokens for some text...
Done:
{'text', 'some'}
End
Get tokens for other text...
Done:
{'text', 'other'}
End
```