import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_camera_cover, run_min_camera_cover
    from solution import Solution

    return Solution, assert_min_camera_cover, run_min_camera_cover


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [0, 0, None, 0, 0]
    expected = 1
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_min_camera_cover):
    result = run_min_camera_cover(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_min_camera_cover, expected, result):
    assert_min_camera_cover(result, expected)
    return


if __name__ == "__main__":
    app.run()
