import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_list, run_reverse_list
    from solution import Solution

    return Solution, assert_reverse_list, run_reverse_list


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 3, 4, 5]
    expected_list = [5, 4, 3, 2, 1]
    return expected_list, head_list


@app.cell
def _(Solution, head_list, run_reverse_list):
    result = run_reverse_list(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_reverse_list, expected_list, result):
    assert_reverse_list(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
