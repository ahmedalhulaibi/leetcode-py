import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_eliminate_maximum, run_eliminate_maximum
    from solution import Solution

    return Solution, assert_eliminate_maximum, run_eliminate_maximum


@app.cell
def _():
    # Example test case
    dist: list[int] = [1, 3, 4]
    speed: list[int] = [1, 1, 1]
    expected: int = 3
    return dist, expected, speed


@app.cell
def _(Solution, dist: list[int], run_eliminate_maximum, speed: list[int]):
    result = run_eliminate_maximum(Solution, dist, speed)
    result
    return (result,)


@app.cell
def _(assert_eliminate_maximum, expected: int, result):
    assert_eliminate_maximum(result, expected)
    return


if __name__ == "__main__":
    app.run()
