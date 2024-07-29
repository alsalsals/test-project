def relative_from_root(path: str):
    '''
    Returns the absolute path relative to the project's root directory.
    '''
    import test_project
    from pathlib import Path

    return (
        Path(test_project.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
