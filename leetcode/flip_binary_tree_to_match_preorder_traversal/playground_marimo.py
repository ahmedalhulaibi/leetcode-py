import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flip_match_voyage, run_flip_match_voyage
    from solution import Solution

    return Solution, assert_flip_match_voyage, run_flip_match_voyage


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3]
    voyage = [1, 3, 2]
    expected = [1]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_flip_match_voyage):
    result = run_flip_match_voyage(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_flip_match_voyage, expected, result):
    assert_flip_match_voyage(result, expected)
    return


if __name__ == "__main__":
    app.run()
