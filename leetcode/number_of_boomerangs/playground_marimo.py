import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_boomerangs, run_number_of_boomerangs
    from solution import Solution

    return Solution, assert_number_of_boomerangs, run_number_of_boomerangs


@app.cell
def _():
    # Example test case
    points: list[list[int]] = [[0, 0], [1, 0], [2, 0]]
    expected: int = 2
    return expected, points


@app.cell
def _(Solution, points: list[list[int]], run_number_of_boomerangs):
    result = run_number_of_boomerangs(Solution, points)
    print(f"Number of boomerangs: {result}")
    result
    return (result,)


@app.cell
def _(assert_number_of_boomerangs, expected: int, result):
    assert_number_of_boomerangs(result, expected)
    return


if __name__ == "__main__":
    app.run()
