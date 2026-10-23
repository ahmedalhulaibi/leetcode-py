import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_split_list_to_parts, run_split_list_to_parts
    from solution import Solution

    return Solution, assert_split_list_to_parts, run_split_list_to_parts


@app.cell
def _():
    # Example test case
    head_vals: list[int] = [1, 2, 3]
    k = 5
    expected = [[1], [2], [3], [], []]
    return expected, head_vals, k


@app.cell
def _(Solution, head_vals: list[int], k, run_split_list_to_parts):
    result = run_split_list_to_parts(Solution, head_vals, k)
    result
    return (result,)


@app.cell
def _(assert_split_list_to_parts, expected, result):
    assert_split_list_to_parts(result, expected)
    return


if __name__ == "__main__":
    app.run()
