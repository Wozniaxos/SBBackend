# Generated by Django 2.0.3 on 2018-04-22 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soundbuddy', '0002_auto_20180422_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistInstrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='bands',
            field=models.ManyToManyField(to='soundbuddy.Band'),
        ),
        migrations.AlterField(
            model_name='band',
            name='artists',
            field=models.ManyToManyField(to='soundbuddy.Artist'),
        ),
        migrations.AlterField(
            model_name='band',
            name='events',
            field=models.ManyToManyField(to='soundbuddy.Event'),
        ),
        migrations.AlterField(
            model_name='band',
            name='music_types',
            field=models.ManyToManyField(to='soundbuddy.MusicType'),
        ),
        migrations.AlterField(
            model_name='band',
            name='photos',
            field=models.ManyToManyField(to='soundbuddy.Photo'),
        ),
        migrations.AlterField(
            model_name='band',
            name='preferred_events',
            field=models.ManyToManyField(to='soundbuddy.EventKind'),
        ),
        migrations.AlterField(
            model_name='band',
            name='tracks',
            field=models.ManyToManyField(to='soundbuddy.Track'),
        ),
        migrations.AlterField(
            model_name='band',
            name='videos',
            field=models.ManyToManyField(to='soundbuddy.Video'),
        ),
        migrations.AddField(
            model_name='artistinstrument',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soundbuddy.Artist'),
        ),
        migrations.AddField(
            model_name='artistinstrument',
            name='instrument',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soundbuddy.Instrument'),
        ),
    ]
