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
