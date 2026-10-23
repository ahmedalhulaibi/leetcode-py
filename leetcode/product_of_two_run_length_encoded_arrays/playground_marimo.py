import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_rle_array, run_find_rle_array
    from solution import Solution

    return Solution, assert_find_rle_array, run_find_rle_array


@app.cell
def _():
    # Example test case
    encoded1 = [[1, 3], [2, 3]]
    encoded2 = [[6, 3], [3, 3]]
    expected = [[6, 6]]
    return encoded1, encoded2, expected


@app.cell
def _(Solution, encoded1, encoded2, run_find_rle_array):
    result = run_find_rle_array(Solution, encoded1, encoded2)
    result
    return (result,)


@app.cell
def _(assert_find_rle_array, expected, result):
    assert_find_rle_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
