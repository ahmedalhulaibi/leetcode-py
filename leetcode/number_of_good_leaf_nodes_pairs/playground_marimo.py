import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_pairs, run_count_pairs
    from solution import Solution

    return Solution, assert_count_pairs, run_count_pairs


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, None, 4]
    distance = 3
    expected = 1
    return distance, expected, root_list


@app.cell
def _(Solution, distance, root_list: list[int | None], run_count_pairs):
    result = run_count_pairs(Solution, root_list, distance)
    result
    return (result,)


@app.cell
def _(assert_count_pairs, expected, result):
    assert_count_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
