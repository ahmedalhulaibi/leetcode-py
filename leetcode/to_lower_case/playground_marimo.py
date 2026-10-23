import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_to_lower_case, run_to_lower_case
    from solution import Solution

    return Solution, assert_to_lower_case, run_to_lower_case


@app.cell
def _():
    # Example test case
    s = "Hello"
    expected = "hello"
    return expected, s


@app.cell
def _(Solution, run_to_lower_case, s):
    result = run_to_lower_case(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_to_lower_case, expected, result):
    assert_to_lower_case(result, expected)
    return


if __name__ == "__main__":
    app.run()
