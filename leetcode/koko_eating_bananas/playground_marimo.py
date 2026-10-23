import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_eating_speed, run_min_eating_speed
    from solution import Solution

    return Solution, assert_min_eating_speed, run_min_eating_speed


@app.cell
def _():
    # Example test case
    piles = [3, 6, 7, 11]
    h = 8
    expected = 4
    return expected, h, piles


@app.cell
def _(Solution, h, piles, run_min_eating_speed):
    result = run_min_eating_speed(Solution, piles, h)
    result
    return (result,)


@app.cell
def _(assert_min_eating_speed, expected, result):
    assert_min_eating_speed(result, expected)
    return


if __name__ == "__main__":
    app.run()
