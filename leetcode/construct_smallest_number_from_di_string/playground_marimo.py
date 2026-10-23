import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_number, run_smallest_number
    from solution import Solution

    return Solution, assert_smallest_number, run_smallest_number


@app.cell
def _():
    # Example test case
    pattern = "IIIDIDDD"
    expected = "123549876"
    return expected, pattern


@app.cell
def _(Solution, pattern, run_smallest_number):
    result = run_smallest_number(Solution, pattern)
    result
    return (result,)


@app.cell
def _(assert_smallest_number, expected, result):
    assert_smallest_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
