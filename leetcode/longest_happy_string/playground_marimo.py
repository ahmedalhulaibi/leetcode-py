import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_happy_string, run_longest_happy_string
    from solution import Solution

    return Solution, assert_longest_happy_string, run_longest_happy_string


@app.cell
def _():
    # Example test case
    a = 1
    b = 1
    c = 7
    return a, b, c


@app.cell
def _(Solution, a, b, c, run_longest_happy_string):
    result = run_longest_happy_string(Solution, a, b, c)
    result
    return (result,)


@app.cell
def _(a, assert_longest_happy_string, b, c, result):
    assert_longest_happy_string(result, a, b, c)
    return


if __name__ == "__main__":
    app.run()
