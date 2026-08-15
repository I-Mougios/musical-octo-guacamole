# packages/kafka-core/kafka_core/cli.py
import sys

try:
    import typer
except ImportError:
    print(
        "Error: The CLI dependencies are missing.\n"
        "Please reinstall this package with the CLI extra using:\n"
        "pip install 'kafka-core[cli]'",
        file=sys.stderr
    )
    sys.exit(1)

app = typer.Typer(help="Kafka Core CLI")

@app.command()
def hello():
    """
    Hello command to verify the CLI is working.
    """
    typer.echo("Kafka Core CLI is working!")


@app.command()
def shutdown():
    """
    Shutdown command to stop Kafka services.
    """
    typer.echo("Shutting down Kafka services...")
