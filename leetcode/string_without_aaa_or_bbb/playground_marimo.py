import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_str_without3a3b, run_str_without3a3b
    from solution import Solution

    return Solution, assert_str_without3a3b, run_str_without3a3b


@app.cell
def _():
    # Example test case
    a = 1
    b = 2
    expected = 3
    return a, b, expected


@app.cell
def _(Solution, a, b, run_str_without3a3b):
    result = run_str_without3a3b(Solution, a, b)
    result
    return (result,)


@app.cell
def _(assert_str_without3a3b, expected, result):
    assert_str_without3a3b(result, expected)
    return


if __name__ == "__main__":
    app.run()
