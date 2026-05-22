"""Migracao inicial gerada com python manage.py makemigrations."""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('bandeira', models.CharField(blank=True, max_length=50)),
                ('endereco', models.CharField(max_length=200)),
                ('avaliacao', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('gasolina', 'Gasolina Comum'), ('aditivada', 'Gasolina Aditivada'), ('etanol', 'Etanol'), ('diesel', 'Diesel S-10')], max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('posto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precos', to='postos.posto')),
            ],
        ),
        migrations.CreateModel(
            name='Comodidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('conveniencia', 'Conveniencia'), ('farmacia', 'Farmacia'), ('restaurante', 'Restaurante'), ('loja', 'Loja')], max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('posto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comodidades', to='postos.posto')),
            ],
        ),
    ]