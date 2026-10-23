import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_place_flowers, run_can_place_flowers
    from solution import Solution

    return Solution, assert_can_place_flowers, run_can_place_flowers


@app.cell
def _():
    # Example test case
    flowerbed: list[int] = [1, 0, 0, 0, 1]
    n = 1
    expected = True
    return expected, flowerbed, n


@app.cell
def _(Solution, flowerbed: list[int], n, run_can_place_flowers):
    result = run_can_place_flowers(Solution, flowerbed, n)
    result
    return (result,)


@app.cell
def _(assert_can_place_flowers, expected, result):
    assert_can_place_flowers(result, expected)
    return


if __name__ == "__main__":
    app.run()
