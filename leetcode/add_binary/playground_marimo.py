import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_binary, run_add_binary
    from solution import Solution

    return Solution, assert_add_binary, run_add_binary


@app.cell
def _():
    # Example test case
    a = "11"
    b = "1"
    expected = "100"
    return a, b, expected


@app.cell
def _(Solution, a, b, run_add_binary):
    result = run_add_binary(Solution, a, b)
    result
    return (result,)


@app.cell
def _(assert_add_binary, expected, result):
    assert_add_binary(result, expected)
    return


if __name__ == "__main__":
    app.run()
