import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_phone_directory, run_phone_directory
    from solution import PhoneDirectory

    return PhoneDirectory, assert_phone_directory, run_phone_directory


@app.cell
def _():
    # Example test case
    operations = ["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
    inputs = [[3], [], [], [2], [], [2], [2], [2]]
    expected = [None, 0, 1, True, 2, False, None, True]
    return expected, inputs, operations


@app.cell
def _(PhoneDirectory, inputs, operations, run_phone_directory):
    result, directory = run_phone_directory(PhoneDirectory, operations, inputs)
    print(result)
    directory
    return (result,)


@app.cell
def _(assert_phone_directory, expected, result):
    assert_phone_directory(result, expected)
    return


if __name__ == "__main__":
    app.run()
