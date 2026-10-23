import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_obstacle_course, run_longest_obstacle_course
    from solution import Solution

    return (
        Solution,
        assert_longest_obstacle_course,
        run_longest_obstacle_course,
    )


@app.cell
def _():
    # Example test case
    obstacles: list[int] = [1, 2, 3, 2]
    expected: list[int] = [1, 2, 3, 3]
    return expected, obstacles


@app.cell
def _(Solution, obstacles: list[int], run_longest_obstacle_course):
    result = run_longest_obstacle_course(Solution, obstacles)
    result
    return (result,)


@app.cell
def _(assert_longest_obstacle_course, expected: list[int], result):
    assert_longest_obstacle_course(result, expected)
    return


if __name__ == "__main__":
    app.run()
