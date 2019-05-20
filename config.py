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
