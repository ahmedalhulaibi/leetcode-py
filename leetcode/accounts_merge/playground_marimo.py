import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_accounts_merge, run_accounts_merge
    from solution import Solution

    return Solution, assert_accounts_merge, run_accounts_merge


@app.cell
def _():
    # Example test case
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    return accounts, expected


@app.cell
def _(Solution, accounts, run_accounts_merge):
    result = run_accounts_merge(Solution, accounts)
    result
    return (result,)


@app.cell
def _(assert_accounts_merge, expected, result):
    assert_accounts_merge(result, expected)
    return


if __name__ == "__main__":
    app.run()
