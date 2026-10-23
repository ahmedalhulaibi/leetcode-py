import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_full_bloom_flowers, run_full_bloom_flowers
    from solution import Solution

    return Solution, assert_full_bloom_flowers, run_full_bloom_flowers


@app.cell
def _():
    # Example test case
    flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
    people = [2, 3, 7, 11]
    expected = [1, 2, 2, 2]
    return expected, flowers, people


@app.cell
def _(Solution, flowers, people, run_full_bloom_flowers):
    result = run_full_bloom_flowers(Solution, flowers, people)
    result
    return (result,)


@app.cell
def _(assert_full_bloom_flowers, expected, result):
    assert_full_bloom_flowers(result, expected)
    return


if __name__ == "__main__":
    app.run()
