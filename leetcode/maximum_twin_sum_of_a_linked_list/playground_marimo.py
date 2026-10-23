import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pair_sum, run_pair_sum
    from solution import Solution

    return Solution, assert_pair_sum, run_pair_sum


@app.cell
def _():
    # Example test case
    head_list: list[int] = [5, 4, 2, 1]
    expected = 6
    return expected, head_list


@app.cell
def _(Solution, head_list: list[int], run_pair_sum):
    result = run_pair_sum(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_pair_sum, expected, result):
    assert_pair_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
