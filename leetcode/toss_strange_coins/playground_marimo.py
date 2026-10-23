import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_probability_of_heads, run_probability_of_heads
    from solution import Solution

    return Solution, assert_probability_of_heads, run_probability_of_heads


@app.cell
def _():
    # Example test case
    prob = [0.4]
    target = 1
    expected = 0.4
    return expected, prob, target


@app.cell
def _(Solution, prob, run_probability_of_heads, target):
    result = run_probability_of_heads(Solution, prob, target)
    result
    return (result,)


@app.cell
def _(assert_probability_of_heads, expected, result):
    assert_probability_of_heads(result, expected)
    return


if __name__ == "__main__":
    app.run()
