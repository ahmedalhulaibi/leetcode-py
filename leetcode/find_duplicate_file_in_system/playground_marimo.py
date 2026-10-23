import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_duplicate, run_find_duplicate
    from solution import Solution

    return Solution, assert_find_duplicate, run_find_duplicate


@app.cell
def _():
    # Example test case
    paths = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)",
    ]
    expected = [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]
    return expected, paths


@app.cell
def _(Solution, paths, run_find_duplicate):
    result = run_find_duplicate(Solution, paths)
    result
    return (result,)


@app.cell
def _(assert_find_duplicate, expected, result):
    assert_find_duplicate(result, expected)
    return


if __name__ == "__main__":
    app.run()
