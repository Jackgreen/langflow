
def _get_file_type(path: str) -> str:
    """Strips quotes from the url."""
    list2 = path.split(".")
    return list2[len(list2) - 1]
