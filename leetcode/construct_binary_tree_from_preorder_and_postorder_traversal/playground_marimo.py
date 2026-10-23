import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_construct_from_pre_post, run_construct_from_pre_post
    from solution import Solution

    return (
        Solution,
        assert_construct_from_pre_post,
        run_construct_from_pre_post,
    )


@app.cell
def _():
    # Example test case
    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    expected = [[1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]]
    return expected, postorder, preorder


@app.cell
def _(Solution, postorder, preorder, run_construct_from_pre_post):
    result = run_construct_from_pre_post(Solution, preorder, postorder)
    result
    return (result,)


@app.cell
def _(assert_construct_from_pre_post, expected, result):
    assert_construct_from_pre_post(result, expected)
    return


if __name__ == "__main__":
    app.run()
