# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 157. Read N Characters Given Read4

    **Easy** · Array, Interactive, Simulation

    Given a `file` and assume that you can only read the file using a given method `read4`, implement a method to read `n` characters.

    **Method read4:**

    The API `read4` reads **four consecutive characters** from `file`, then writes those characters into the buffer array `buf4`.

    The return value is the number of actual characters read.

    Note that `read4()` has its own file pointer, much like `FILE *fp` in C.

    **Definition of read4:**

    ```
        Parameter:  char[] buf4
        Returns:    int

    buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
    ```

    Below is a high-level example of how `read4` works:

    ![read4 example](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0157.Read%20N%20Characters%20Given%20Read4/images/157_example.png)

    ```
    File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
    char[] buf4 = new char[4]; // Create buffer with enough space to store characters
    read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
    read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
    read4(buf4); // read4 returns 0. Now buf4 = "\", fp points to end of file
    ```

    **Method read:**

    By using the `read4` method, implement the method `read` that reads `n` characters from `file` and stores them in the buffer array `buf`. Consider that you cannot manipulate `file` directly.

    The return value is the number of actual characters read.

    **Definition of read:**

    ```
        Parameters: char[] buf, int n
        Returns:    int

    buf[] is a destination, not a source. You will need to write the results to buf[].
    ```

    **Note:**

    - Consider that you cannot manipulate the file directly. The file is only accessible for `read4` but not for `read`.
    - The `read` function will only be called once for each test case.
    - You may assume the destination buffer array, `buf`, is guaranteed to have enough space for storing `n` characters.

    ## Examples

    ```
    Input: file = "abc", n = 4
    Output: 3
    Explanation: After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
    Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.
    ```

    ```
    Input: file = "abcde", n = 5
    Output: 5
    Explanation: After calling your read method, buf should contain "abcde". We read a total of 5 characters from the file, so return 5.
    ```

    ```
    Input: file = "abcdABCD1234", n = 12
    Output: 12
    Explanation: After calling your read method, buf should contain "abcdABCD1234". We read a total of 12 characters from the file, so return 12.
    ```

    ## Constraints

    - `1 <= file.length <= 500`
    - `file` consists of English letters and digits.
    - `1 <= n <= 1000`

    **Note:** In this repository the `read4` API is provided as the `read4(buf4)` method of the `File` class in `solution.py`, and `read` receives that `File` instance as its third argument.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class File:

        def __init__(self, content: str) -> None:
            self.content = content
            self.pos = 0

        def read4(self, buf4: list[str]) -> int:
            chunk = self.content[self.pos:self.pos + 4]
            self.pos += len(chunk)
            for i, char in enumerate(chunk):
                buf4[i] = char
            return len(chunk)

    class Solution:

        def read(self, buf: list[str], n: int, file: File) -> int:
            raise NotImplementedError('Implement read')

    practice_exports = {'File': File, 'Solution': Solution}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
