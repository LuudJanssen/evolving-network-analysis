import click


def normal(string):
    click.echo(string)


def important(string):
    click.secho(string, bold=True, fg='blue')


def warning(string):
    click.secho(string, bold=True, fg='yellow')


def success(string):
    click.secho(string, bold=True, fg='green')


def error(string):
    click.secho(string, bold=True, fg='red', err=True)


def dim(string):
    click.secho(string, dim=True)
