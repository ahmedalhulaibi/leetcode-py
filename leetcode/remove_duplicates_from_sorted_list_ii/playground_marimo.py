import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_delete_duplicates, run_delete_duplicates
    from solution import Solution

    return Solution, assert_delete_duplicates, run_delete_duplicates


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 3, 3, 4, 4, 5]
    expected_list = [1, 2, 5]
    return expected_list, head_list


@app.cell
def _(Solution, head_list, run_delete_duplicates):
    result = run_delete_duplicates(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_delete_duplicates, expected_list, result):
    assert_delete_duplicates(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
