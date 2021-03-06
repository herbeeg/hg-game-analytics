import click
import uuid

from flask import Blueprint

from app.database import db
from app.models.activation import Activation

task = Blueprint('task', __name__)

@task.cli.command('generate-activation-key')
def generate_single_activation_key():
    key = ''.join(str(uuid.uuid4()).split('-'))

    try:
        activation_key = Activation(key)
        db.session.add(activation_key)
        db.session.commit()

        click.echo(key, nl=False)
    except Exception:
        click.echo('Random activation key could not be generated.', nl=False)