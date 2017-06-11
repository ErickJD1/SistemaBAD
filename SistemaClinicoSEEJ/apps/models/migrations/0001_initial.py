# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cirugia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Citamedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ConsultaExamenFisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultaExamenMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Consultamedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Costo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('idCirugia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Cirugia')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=700)),
                ('idConsultamedica', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Consultamedica')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerocasa', models.IntegerField(blank=True, null=True)),
                ('calle', models.CharField(blank=True, max_length=300, null=True)),
                ('pasajepoligono', models.CharField(blank=True, max_length=300, null=True)),
                ('colonia', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codDoctor', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emergencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
                ('idDoctor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codEnfermera', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Examenfisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Examenmedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registra', models.CharField(max_length=200)),
                ('fecha_registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primerNombre', models.CharField(max_length=100)),
                ('segundoNombre', models.CharField(max_length=100)),
                ('primerApellido', models.CharField(max_length=100)),
                ('segundoApellido', models.CharField(max_length=100)),
                ('parentezco', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=9)),
                ('dereccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fichasignosvitales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('temperatura', models.FloatField()),
                ('ritmocardiaco', models.IntegerField()),
                ('presionarterial', models.CharField(max_length=3)),
                ('glucosa', models.FloatField()),
                ('idConsultamedica', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Consultamedica')),
            ],
        ),
        migrations.CreateModel(
            name='Fichasintomatologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detallesintomas', models.CharField(max_length=1000)),
                ('idConsultamedica', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Consultamedica')),
            ],
        ),
        migrations.CreateModel(
            name='Fisioterapeuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Fisioterapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Historialmedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500)),
                ('idFamiliar', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Familiar')),
            ],
        ),
        migrations.CreateModel(
            name='Hospitalizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaingreso', models.DateField()),
                ('fechasalida', models.DateField()),
                ('numerocamilla', models.IntegerField()),
                ('sala', models.CharField(max_length=100)),
                ('idExpediente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Expediente')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalizacionExamenFisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idExamenFisico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Examenfisico')),
                ('idHospitalizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Hospitalizacion')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalizacionExamenMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idExamenMedico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Examenmedico')),
                ('idHospitalizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Hospitalizacion')),
            ],
        ),
        migrations.CreateModel(
            name='HospiTramieMed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idHospitalizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Hospitalizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('dosis', models.FloatField()),
                ('freciencia', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('idDepartamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEnfermera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Enfermera')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primernombre', models.CharField(max_length=100)),
                ('segundonombre', models.CharField(max_length=100)),
                ('primerapellido', models.CharField(max_length=100)),
                ('segundoapellido', models.CharField(max_length=100)),
                ('dui', models.CharField(max_length=9)),
                ('fechanacimiento', models.DateField()),
                ('genero', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=9)),
                ('ocupacion', models.CharField(max_length=100)),
                ('estadocivil', models.CharField(max_length=20)),
                ('idDireccion', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primernombre', models.CharField(max_length=10)),
                ('segundonombre', models.CharField(max_length=10)),
                ('primerapellido', models.CharField(max_length=10)),
                ('segundoapellido', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Terapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('idConsultamedica', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Consultamedica')),
            ],
        ),
        migrations.AddField(
            model_name='terapia',
            name='idTratamiento',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Tratamiento'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='idPersona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Persona'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='idResponsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Responsable'),
        ),
        migrations.AddField(
            model_name='laboratorista',
            name='idPersona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Persona'),
        ),
        migrations.AddField(
            model_name='hospitramiemed',
            name='idTratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Tratamiento'),
        ),
        migrations.AddField(
            model_name='fisioterapia',
            name='idTratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Tratamiento'),
        ),
        migrations.AddField(
            model_name='fisioterapia',
            name='idfisioterapeuta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Fisioterapeuta'),
        ),
        migrations.AddField(
            model_name='fisioterapeuta',
            name='idPersona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Persona'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='idPaciente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Paciente'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='idPaciente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Paciente'),
        ),
        migrations.AddField(
            model_name='examenmedico',
            name='idLaboratorista',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Laboratorista'),
        ),
        migrations.AddField(
            model_name='examenfisico',
            name='idLaboratorista',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Laboratorista'),
        ),
        migrations.AddField(
            model_name='enfermera',
            name='idPersona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Persona'),
        ),
        migrations.AddField(
            model_name='emergencia',
            name='idPaciente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Paciente'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='idEspecialidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Especialidad'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='idPersona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Persona'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='idmunicipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Municipio'),
        ),
        migrations.AddField(
            model_name='costo',
            name='idExamenFisico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Examenfisico'),
        ),
        migrations.AddField(
            model_name='costo',
            name='idExamenMedico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Examenmedico'),
        ),
        migrations.AddField(
            model_name='costo',
            name='idHospitalizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Hospitalizacion'),
        ),
        migrations.AddField(
            model_name='costo',
            name='idTratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Tratamiento'),
        ),
        migrations.AddField(
            model_name='consultamedica',
            name='idDoctor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Doctor'),
        ),
        migrations.AddField(
            model_name='consultamedica',
            name='idPaciente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Paciente'),
        ),
        migrations.AddField(
            model_name='consultaexamenmedico',
            name='idConsultamedica',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Consultamedica'),
        ),
        migrations.AddField(
            model_name='consultaexamenmedico',
            name='idExamenMedico',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Examenmedico'),
        ),
        migrations.AddField(
            model_name='consultaexamenfisico',
            name='idConsultamedica',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Consultamedica'),
        ),
        migrations.AddField(
            model_name='consultaexamenfisico',
            name='idExamenFisico',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Examenfisico'),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='idDoctor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Doctor'),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='idPaciente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Paciente'),
        ),
        migrations.AddField(
            model_name='cirugia',
            name='idDoctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Doctor'),
        ),
        migrations.AddField(
            model_name='cirugia',
            name='idExpediente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Expediente'),
        ),
        migrations.AddField(
            model_name='calendario',
            name='idCitamedica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Citamedica'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='idExpediente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Expediente'),
        ),
    ]
