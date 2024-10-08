# Generated by Django 5.0.6 on 2024-06-12 03:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menza',
            fields=[
                ('idmnz', models.AutoField(db_column='IdMnz', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', help_text='name', max_length=20, unique=True)),
                ('kapacitet', models.IntegerField(db_column='Kapacitet', help_text='capacity of students that the canteen can accommodate')),
                ('adresa', models.CharField(db_column='Adresa', help_text='address', max_length=500)),
                ('slika', models.TextField(db_column='Slika', help_text='picture')),
                ('radnovremedor', models.CharField(db_column='RadnoVremeDor', help_text='breakfast working hours', max_length=11)),
                ('radnovremeruc', models.CharField(db_column='RadnoVremeRuc', help_text='lunch working hours', max_length=11)),
                ('radnovremevec', models.CharField(db_column='RadnoVremeVec', help_text='dinner working hours', max_length=11)),
                ('link', models.CharField(db_column='Link', help_text='information necessary for map api', max_length=500)),
            ],
            options={
                'db_table': 'menza',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Kategorija',
            fields=[
                ('idkat', models.AutoField(db_column='IdKat', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', help_text='name', max_length=100)),
            ],
            options={
                'db_table': 'kategorija',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('idkor', models.OneToOneField(db_column='IdKor', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profilnaslika', models.ImageField(db_column='ProfilnaSlika', default='pfps/profilna.png', help_text='profile picture', upload_to='pfps/')),
                ('adresa', models.CharField(db_column='Adresa', help_text='address', max_length=500)),
                ('datumrodjenja', models.DateField(blank=True, db_column='DatumRodjenja', help_text='birthdate', null=True)),
                ('brojtel', models.CharField(blank=True, db_column='BrojTel', help_text='phone number', max_length=15, null=True)),
            ],
            options={
                'db_table': 'korisnik',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Meni',
            fields=[
                ('idmen', models.AutoField(db_column='IdMen', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'meni',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Obrok',
            fields=[
                ('idobr', models.AutoField(db_column='IdObr', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', help_text='name', max_length=20, unique=True)),
            ],
            options={
                'db_table': 'obrok',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Verifikacionipin',
            fields=[
                ('pin', models.CharField(db_column='PIN', help_text='PIN', max_length=20, unique=True)),
                ('brojstudkartice', models.CharField(db_column='BrojStudKartice', help_text='student card number', max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'verifikacionipin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Aktivnatabla',
            fields=[
                ('idmnz', models.OneToOneField(db_column='IdMnz', help_text='canteen', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studassist.menza')),
                ('aktivna', models.IntegerField(blank=True, db_column='Aktivna', help_text='is it active', null=True)),
                ('tipobroka', models.CharField(blank=True, db_column='TipObroka', help_text='what type of meals are currently being served in canteen', max_length=1, null=True)),
            ],
            options={
                'db_table': 'aktivnatabla',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='menza',
            name='idmen',
            field=models.ForeignKey(db_column='IdMen', help_text='menu', on_delete=django.db.models.deletion.DO_NOTHING, to='studassist.meni'),
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('idtem', models.AutoField(db_column='IdTem', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', help_text='name', max_length=100)),
                ('opis', models.CharField(db_column='Opis', help_text='description', max_length=200)),
                ('idkat', models.ForeignKey(db_column='IdKat', help_text='category', on_delete=django.db.models.deletion.CASCADE, to='studassist.kategorija')),
            ],
            options={
                'db_table': 'tema',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Odgovor',
            fields=[
                ('idodg', models.AutoField(db_column='IdOdg', primary_key=True, serialize=False)),
                ('naslov', models.CharField(db_column='Naslov', help_text='title', max_length=100)),
                ('datumvreme', models.DateTimeField(db_column='DatumVreme', help_text='datetime')),
                ('komentar', models.CharField(db_column='Komentar', help_text="replie's content", max_length=1000)),
                ('slika', models.ImageField(blank=True, db_column='Slika', help_text='attached picture', null=True, upload_to='replies/')),
                ('idkor', models.ForeignKey(db_column='IdKor', help_text='user', on_delete=django.db.models.deletion.CASCADE, to='studassist.korisnik')),
                ('idtem', models.ForeignKey(db_column='IdTem', help_text='subject', on_delete=django.db.models.deletion.CASCADE, to='studassist.tema')),
            ],
            options={
                'db_table': 'odgovor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('idmod', models.OneToOneField(db_column='IdMod', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studassist.korisnik')),
                ('idmnz', models.ForeignKey(db_column='IdMnz', help_text='canteen assigned to the moderator', on_delete=django.db.models.deletion.DO_NOTHING, to='studassist.menza')),
            ],
            options={
                'db_table': 'moderator',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stanjeracuna', models.DecimalField(db_column='StanjeRacuna', decimal_places=2, help_text='account balance', max_digits=20)),
                ('dorucak', models.IntegerField(db_column='Dorucak', default=0, help_text='number of breakfast coupons student owns')),
                ('rucak', models.IntegerField(db_column='Rucak', default=0, help_text='number of lunch coupons student owns')),
                ('vecera', models.IntegerField(db_column='Vecera', default=0, help_text='number of dinner coupons student owns')),
                ('zeton', models.IntegerField(db_column='Zeton', default=0, help_text='number of chips student owns')),
                ('idstu', models.OneToOneField(db_column='IdStu', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studassist.korisnik')),
                ('brojstudkartice', models.OneToOneField(db_column='BrojStudKartice', help_text='card number', on_delete=django.db.models.deletion.DO_NOTHING, to='studassist.verifikacionipin')),
            ],
            options={
                'db_table': 'student',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Obuhvatanje',
            fields=[
                ('idobu', models.AutoField(db_column='IdObu', primary_key=True, serialize=False)),
                ('danunedelji', models.CharField(db_column='DanUNedelji', help_text='weekday', max_length=3)),
                ('tip', models.CharField(db_column='Tip', help_text='breakfast, lunch or dinner', max_length=1)),
                ('idmen', models.ForeignKey(db_column='IdMen', help_text='menu', on_delete=django.db.models.deletion.CASCADE, to='studassist.meni')),
                ('idobr', models.ForeignKey(db_column='IdObr', help_text='meal', on_delete=django.db.models.deletion.CASCADE, to='studassist.obrok')),
            ],
            options={
                'db_table': 'obuhvatanje',
                'managed': True,
                'unique_together': {('idmen', 'idobr', 'danunedelji', 'tip')},
            },
        ),
        migrations.CreateModel(
            name='Recenzija',
            fields=[
                ('idrec', models.AutoField(db_column='IdRec', primary_key=True, serialize=False)),
                ('opis', models.CharField(db_column='Opis', help_text='student description', max_length=200)),
                ('tekst', models.CharField(blank=True, db_column='Tekst', help_text='review text', max_length=500, null=True)),
                ('datumvreme', models.DateTimeField(db_column='DatumVreme', help_text='datetime')),
                ('ocena', models.IntegerField(db_column='Ocena', help_text='rating')),
                ('idmnz', models.ForeignKey(db_column='IdMnz', help_text='canteen', on_delete=django.db.models.deletion.CASCADE, to='studassist.menza')),
                ('idstu', models.ForeignKey(db_column='IdStu', help_text='student', on_delete=django.db.models.deletion.CASCADE, to='studassist.student')),
            ],
            options={
                'db_table': 'recenzija',
                'managed': True,
                'unique_together': {('idstu', 'idmnz')},
            },
        ),
    ]
