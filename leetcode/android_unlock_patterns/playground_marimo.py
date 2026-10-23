import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_patterns, run_number_of_patterns
    from solution import Solution

    return Solution, assert_number_of_patterns, run_number_of_patterns


@app.cell
def _():
    # Example test case
    m = 1
    n = 2
    expected = 65
    return expected, m, n


@app.cell
def _(Solution, m, n, run_number_of_patterns):
    result = run_number_of_patterns(Solution, m, n)
    result
    return (result,)


@app.cell
def _(assert_number_of_patterns, expected, result):
    assert_number_of_patterns(result, expected)
    return


if __name__ == "__main__":
    app.run()
