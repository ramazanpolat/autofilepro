# autofilepro
Automatically processes files. Simple extract, transform and Do(x) program.

* Watches a directory for new files
* Whenever a new file is detected, processes it

Currently, 2 phases are defined: "validate phase" and "transform phase".
Each phase calls a processor and there are two processes, `validate_file` and `transform_file`in `processor.py` file.

If you put a `.txt` file in `input_dir`, **validate phase** will pick it and validate.
Then **transform phase** gets the validated output and transforms it.   

## Step 1

Edit `config.py` file which is like this:

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

Write your processor functions into `processor.py` file.

## Step 3

Add you processor function to `PROCESSOR` dictionary in `processor.py` file, which is like this:

```python
PROCESSORS = {'validate': validate_file,
              'transform': transform_file}
```

## Step 4
Run your processors:

    python afp.py

## How does it work?

`DirWatch` class watches the directory speified by `input_dir` for new files that matches the `file_filter`.
Both `input_dir` and `file_filter` are specified in `config.py`
Whenever a new file is added to `input_dir`, `DirWatch` gets that file and sends to `processor`.

`processor` is also specified in the `config.py`.

`processor` processes the file (in the example code it renames it). Then the other `processor` gets in and does its job.

You can define any number of phases in `config.py` file. 

## Using Directory Watcher from CLI

You can use `DirWatch` directly from CLI.

In the following example we watch `C:\somediretory` directory and track new files with `.txt` extension. 
If a new file is present then we process new file name with `send` parameter(sending filenames to this paremeter).
So in this example, we only show file names with `echo`. This is also default behavior. The `%s` is replaced with the newe file name hence it is echoed.

```
$ python dirwatch.py --dir=C:\somediretory --filter="*.txt" --send="echo %s" --interval=5

```
### CLI parameters

* `dir`: the directory to start watching. Default = `.` (current directory)
* `filter`: File filter. Only new files that matches this filter will be processed. Default = `*.*`  
* `send`: Command to utilize new files. Default = `echo %s` (shows newly added file names in console)
* `interval`: Directory watching interval. `DirWatch` checks the directory for every interval. Default = `1` second 
 
