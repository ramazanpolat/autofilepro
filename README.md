# autofilepro
Automatically processes files

## Step 1

Edit ``config.py`` file which is like this:

```python
phases = [
    {
        "name": "validate",
        "input_dir": "./input",
        "file_filter": "*.txt",
        "processor": "validate",
    },
    {
        "name": "transform",
        "input_dir": "./input",
        "file_filter": "*.validate_ok",
        "processor": "transform",
    }

]
```

## Step 2

Write your processor functions into ``processor.py`` file.

## Step 3

Add you processor function to ``PROCESSOR`` dictionary in ``processor.py`` file, which is like this:

```python
PROCESSORS = {'validate': validate_file,
              'transform': transform_file}
```

## Step 4
Run your processors:

    python afp.py
