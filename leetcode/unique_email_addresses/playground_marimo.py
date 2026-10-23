import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_unique_emails, run_num_unique_emails
    from solution import Solution

    return Solution, assert_num_unique_emails, run_num_unique_emails


@app.cell
def _():
    # Example test case
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    expected = 2
    return emails, expected


@app.cell
def _(Solution, emails, run_num_unique_emails):
    result = run_num_unique_emails(Solution, emails)
    result
    return (result,)


@app.cell
def _(assert_num_unique_emails, expected, result):
    assert_num_unique_emails(result, expected)
    return


if __name__ == "__main__":
    app.run()
