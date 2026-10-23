import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pseudo_palindromic_paths, run_pseudo_palindromic_paths
    from solution import Solution

    return (
        Solution,
        assert_pseudo_palindromic_paths,
        run_pseudo_palindromic_paths,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [2, 3, 1, 3, 1, None, 1]
    expected: int = 2
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_pseudo_palindromic_paths):
    result = run_pseudo_palindromic_paths(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_pseudo_palindromic_paths, expected: int, result):
    assert_pseudo_palindromic_paths(result, expected)
    return


if __name__ == "__main__":
    app.run()
