import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_insert, run_insert
    from solution import Solution

    return Solution, assert_insert, run_insert


@app.cell
def _():
    # Example test case
    head_list = [3, 4, 1]
    insert_val = 2
    expected_list = [3, 4, 1, 2]
    return expected_list, head_list, insert_val


@app.cell
def _(Solution, head_list, insert_val, run_insert):
    result = run_insert(Solution, head_list, insert_val)
    result
    return (result,)


@app.cell
def _(assert_insert, expected_list, result):
    assert_insert(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
