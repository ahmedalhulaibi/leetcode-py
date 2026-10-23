import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_file_system, run_file_system
    from solution import FileSystem

    return FileSystem, assert_file_system, run_file_system


@app.cell
def _():
    # Example test case
    operations = ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
    inputs = [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
    expected = [None, [], None, None, ["a"], "hello"]
    return expected, inputs, operations


@app.cell
def _(FileSystem, inputs, operations, run_file_system):
    result, fs = run_file_system(FileSystem, operations, inputs)
    print(result)
    fs
    return (result,)


@app.cell
def _(assert_file_system, expected, result):
    assert_file_system(result, expected)
    return


if __name__ == "__main__":
    app.run()
