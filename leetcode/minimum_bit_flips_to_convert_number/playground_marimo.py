import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_bit_flips, run_min_bit_flips
    from solution import Solution

    return Solution, assert_min_bit_flips, run_min_bit_flips


@app.cell
def _():
    # Example test case
    start = 10
    goal = 7
    expected = 3
    return expected, goal, start


@app.cell
def _(Solution, goal, run_min_bit_flips, start):
    result = run_min_bit_flips(Solution, start, goal)
    result
    return (result,)


@app.cell
def _(assert_min_bit_flips, expected, result):
    assert_min_bit_flips(result, expected)
    return


if __name__ == "__main__":
    app.run()
