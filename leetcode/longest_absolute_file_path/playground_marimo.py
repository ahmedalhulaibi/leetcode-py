import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_length_longest_path, run_length_longest_path
    from solution import Solution

    return Solution, assert_length_longest_path, run_length_longest_path


@app.cell
def _():
    # Example test case
    input_str = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    expected = 20
    return expected, input_str


@app.cell
def _(Solution, input_str, run_length_longest_path):
    result = run_length_longest_path(Solution, input_str)
    result
    return (result,)


@app.cell
def _(assert_length_longest_path, expected, result):
    assert_length_longest_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
