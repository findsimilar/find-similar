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
Start
Get tokens for some text...
Done:
{'text', 'some'}
End
Start
Get tokens for other text...
Done:
{'text', 'other'}
End
```

### Get cos between two texts

Input:
```commandline
python manage.py compare_two "one" "two"
```

Output:
```commandline
Start
Get cos between "one" and "two"
Start
Get tokens for one...
Done:
{'one'}
End
Start
Get tokens for two...
Done:
{'two'}
End
Done:
0
End
```

With make:
```commandline
make one="one" two="two" compare_two
```

### Example frequency analysis

Input:
```commandline
python manage.py example_frequency_analysis "mock"
```

Output:
```commandline
Start
Analyze "mock"...
Done:
(('mock', 2), ('example', 2), ('for', 2), ('tests', 2), ('this', 1), ('is', 1))
End
```

With make:
```commandline
make example="mock" example_frequency_analysis
```

### Load training data

Input:
```commandline
python manage.py load_training_data 2x2 analysis/tests/data/2x2.xlsx 0
```

Output:
```commandline
Start
Loading data from "analysis/tests/data/2x2.xlsx"...
Done:
TrainingData object (None)
End
```

With make:
```commandline
make load_traning_data name=2x2 filepath=analysis/tests/data/2x2.xlsx sheet_name=0
```
