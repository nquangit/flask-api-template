# commands.py
import click
from flask.cli import with_appcontext
from extensions.ext_database import db


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Initialize the database."""
    db.create_all()
    click.echo("Initialized the database.")


@click.command("migrate-db")
@with_appcontext
def migrate_db_command():
    """Migrate and upgrade database."""
    from flask_migrate import upgrade, migrate

    migrate()
    upgrade()
    click.echo("Database migrated and upgraded!")


# Đăng ký command
def register_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(migrate_db_command)
