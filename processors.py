from pathlib import Path


def validate_file(file: Path):
    print("\t-->Validate started")

    def validate_line(a_line):
        rows = a_line.split('|')
        if len(rows) == 3:
            return True
        return False

    validate_started_file: Path = file.parent / (file.name + '.validate_started')
    print('validate_started_file:', validate_started_file)
    print('renaming %s to %s' % (file, validate_started_file))
    file.rename(validate_started_file)

    validate_error_file: Path = file.parent / (file.name + '.validate_error')
    print('validate_error_file:', validate_error_file)
    validate_ok_file: Path = file.parent / (file.name + '.validate_ok')
    print('validate_ok_file:', validate_ok_file)

    with validate_started_file.open(mode="r") as validate_started_handle:
        with validate_error_file.open(mode="w") as validate_error_handle:
            with validate_ok_file.open(mode="w") as validate_ok_handle:
                for line in validate_started_handle:
                    # if len(line.strip()) == 0:
                    #     continue
                    if validate_line(line):
                        validate_ok_handle.write(line)
                    else:
                        validate_error_handle.write(line)

    print('renaming %s to %s' % (validate_started_file, validate_ok_file))

    validate_end_file = file.parent / (file.name + '.validate_ended')
    validate_started_file.rename(validate_end_file)


def transform_file(file: Path):
    print("\t-->Transform started")

    def transform_line(a_line: str):
        rows = a_line.split('|')
        new_rows = [row.strip() + 'x_' for row in rows]
        return '|'.join(new_rows) + '\n'

    transform_started_file: Path = file.parent / (file.name + '.transform_started')
    print('transform_started_file:', transform_started_file)
    print('renaming %s to %s' % (file, transform_started_file))
    file.rename(transform_started_file)

    transform_error_file: Path = file.parent / (file.name + '.transform_error')
    print('transform_error_file:', transform_error_file)
    transform_ok_file: Path = file.parent / (file.name + '.transform_ok')
    print('transform_ok_file:', transform_ok_file)

    with transform_started_file.open(mode="r") as transform_started_handle:
        with transform_error_file.open(mode="w") as transform_error_handle:
            with transform_ok_file.open(mode="w") as transform_ok_handle:
                for line in transform_started_handle:
                    try:
                        if len(line.strip()) == 0:
                            continue
                        new_line = transform_line(line)
                        transform_ok_handle.write(new_line)
                    except RuntimeError:
                        transform_error_handle.write(line)

    print('renaming %s to %s' % (transform_started_file, transform_ok_file))

    validate_end_file = file.parent / (file.name + '.transform_ended')
    transform_started_file.rename(validate_end_file)


PROCESSORS = {'validate': validate_file,
              'transform': transform_file}
