import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_between, run_reverse_between
    from solution import Solution

    return Solution, assert_reverse_between, run_reverse_between


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 3, 4, 5]
    left, right = 2, 4
    expected_list = [1, 4, 3, 2, 5]
    return expected_list, head_list, left, right


@app.cell
def _(Solution, head_list, left, right, run_reverse_between):
    result = run_reverse_between(Solution, head_list, left, right)
    result
    return (result,)


@app.cell
def _(assert_reverse_between, expected_list, result):
    assert_reverse_between(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
