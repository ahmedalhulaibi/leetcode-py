import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_create_binary_tree, run_create_binary_tree
    from solution import Solution

    return Solution, assert_create_binary_tree, run_create_binary_tree


@app.cell
def _():
    # Example test case
    descriptions_list: list[list[int]] = [
        [20, 15, 1],
        [20, 17, 0],
        [50, 20, 1],
        [50, 80, 0],
        [80, 19, 1],
    ]
    expected_list: list[int | None] = [50, 20, 80, 15, 17, 19]
    return descriptions_list, expected_list


@app.cell
def _(Solution, descriptions_list: list[list[int]], run_create_binary_tree):
    result = run_create_binary_tree(Solution, descriptions_list)
    result
    return (result,)


@app.cell
def _(assert_create_binary_tree, expected_list: list[int | None], result):
    assert_create_binary_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
