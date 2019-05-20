# autofilepro
Automatically processes files

## Step 1

Edit ``config.py`` file which is like this:

```python
phases = [
    {
        "name": "validate phase",
        "input_dir": "./input",
        "file_filter": "*.txt",
        "processor": "validate",
    },
    {
        "name": "transform phase",
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

## How does it work?

``DirectoryWatcher`` class watches the ``input_dir`` for new files that matches the ``file_filter``.
Both ``input_dir`` and ``file_filter`` are specified in ``config.py``
Whenever a new file is added to ``input_dir``, ``DirectoryWatcher`` gets that file and sends to ``processor``.

``processor`` is also specified in the ``config.py``.

``processor`` processes file and renames it. Then the other ``processor`` gets in and does its job.

You can define unlimited amount of phase in ``config.py`` file. 