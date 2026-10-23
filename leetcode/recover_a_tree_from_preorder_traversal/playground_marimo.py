import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_recover_from_preorder, run_recover_from_preorder
    from solution import Solution

    return Solution, assert_recover_from_preorder, run_recover_from_preorder


@app.cell
def _():
    # Example test case
    traversal = "1-2--3--4-5--6--7"
    expected_list: list[int | None] = [1, 2, 5, 3, 4, 6, 7]
    return expected_list, traversal


@app.cell
def _(Solution, run_recover_from_preorder, traversal):
    result = run_recover_from_preorder(Solution, traversal)
    result
    return (result,)


@app.cell
def _(assert_recover_from_preorder, expected_list: list[int | None], result):
    assert_recover_from_preorder(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
