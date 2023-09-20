from main import parse_arguments


def test_argument_parser():
    test_arguments = "--locations_list Berlin London Warsaw".split()
    result = parse_arguments(test_arguments)

    assert result == ["Berlin", "London", "Warsaw"]
