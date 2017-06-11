# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Expediente(models.Model):
    idPaciente = models.OneToOneField('Paciente', blank=True, null=True, on_delete=models.CASCADE)
    registra = models.CharField(max_length=200)
    fecha_registro = models.DateField()


class Antecedente(models.Model):
    idExpediente = models.OneToOneField('Expediente', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()


class Emergencia(models.Model):
    idPaciente = models.OneToOneField('Paciente', blank=True, null=True, on_delete=models.CASCADE)
    idDoctor = models.OneToOneField('Doctor', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    fecha = models.DateField()


class Calendario(models.Model):
    idCitamedica = models.ForeignKey('Citamedica', blank=True, null=True, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()


class Cirugia(models.Model):
    idDoctor = models.ForeignKey('Doctor', blank=True, null=True, on_delete=models.CASCADE)
    idExpediente = models.OneToOneField('Expediente', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)


class Citamedica(models.Model):
    idPaciente = models.OneToOneField('Paciente', blank=True, null=True, on_delete=models.CASCADE)
    idDoctor = models.OneToOneField('Doctor', blank=True, null=True, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()


# Relacion de muchos a muchos genera tabla
class ConsultaExamenFisico(models.Model):
    idConsultamedica = models.OneToOneField('Consultamedica', blank=True, null=True, on_delete=models.CASCADE)
    idExamenFisico = models.OneToOneField('Examenfisico', blank=True, null=True, on_delete=models.CASCADE)


# Relacion de muchos a muchos genera tabla
class ConsultaExamenMedico(models.Model):
    idConsultamedica = models.OneToOneField('Consultamedica', blank=True, null=True, on_delete=models.CASCADE)
    idExamenMedico = models.OneToOneField('Examenmedico', blank=True, null=True, on_delete=models.CASCADE)


class Consultamedica(models.Model):
    idPaciente = models.OneToOneField('Paciente', blank=True, null=True, on_delete=models.CASCADE)
    idDoctor = models.OneToOneField('Doctor', blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()


class Costo(models.Model):
    idExamenMedico = models.ForeignKey('Examenmedico', blank=True, null=True, on_delete=models.CASCADE)
    idExamenFisico = models.ForeignKey('Examenfisico', blank=True, null=True, on_delete=models.CASCADE)
    idCirugia = models.ForeignKey('Cirugia', blank=True, null=True, on_delete=models.CASCADE)
    idHospitalizacion = models.ForeignKey('Hospitalizacion', blank=True, null=True, on_delete=models.CASCADE)
    idTratamiento = models.ForeignKey('Tratamiento', blank=True, null=True, on_delete=models.CASCADE)
    valor = models.FloatField()


class Departamento(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)


class Diagnostico(models.Model):
    idConsultamedica = models.OneToOneField('Consultamedica', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=700)


class Direccion(models.Model):
    idmunicipio = models.ForeignKey('Municipio', blank=True, null=True)
    numerocasa = models.IntegerField(blank=True, null=True)
    calle = models.CharField(max_length=300, blank=True, null=True)
    pasajepoligono = models.CharField(max_length=300, blank=True, null=True)
    colonia = models.CharField(max_length=300, blank=True, null=True)


class Doctor(models.Model):
    idPersona = models.OneToOneField('Persona', blank=True, null=True, on_delete=models.CASCADE)
    idEspecialidad = models.ForeignKey('Especialidad', blank=True, null=True, on_delete=models.CASCADE)
    codDoctor = models.CharField(max_length=50, blank=True, null=True)


class Enfermera(models.Model):
    idPersona = models.OneToOneField('Persona', blank=True, null=True, on_delete=models.CASCADE)
    codEnfermera = models.CharField(max_length=50, blank=True, null=True)


class Especialidad(models.Model):
    descripcion = models.CharField(max_length=200)


class Examenfisico(models.Model):
    idLaboratorista = models.OneToOneField('Laboratorista', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)


class Examenmedico(models.Model):
    idLaboratorista = models.OneToOneField('Laboratorista', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)


class Familiar(models.Model):
    idPaciente = models.OneToOneField('Paciente', blank=True, null=True, on_delete=models.CASCADE)
    primerNombre = models.CharField(max_length=100)
    segundoNombre = models.CharField(max_length=100)
    primerApellido = models.CharField(max_length=100)
    segundoApellido = models.CharField(max_length=100)
    parentezco = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    telefono = models.CharField(max_length=9)
    dereccion = models.CharField(max_length=200)


class Fichasignosvitales(models.Model):
    idConsultamedica = models.OneToOneField('Consultamedica', blank=True, null=True, on_delete=models.CASCADE)
    peso = models.FloatField()
    temperatura = models.FloatField()
    ritmocardiaco = models.IntegerField()
    presionarterial = models.CharField(max_length=3)
    glucosa = models.FloatField()


class Fichasintomatologia(models.Model):
    idConsultamedica = models.OneToOneField('Consultamedica', blank=True, null=True, on_delete=models.CASCADE)
    detallesintomas = models.CharField(max_length=1000)


class Fisioterapeuta(models.Model):
    idPersona = models.OneToOneField('Persona', blank=True, null=True, on_delete=models.CASCADE)


class Fisioterapia(models.Model):
    idTratamiento = models.ForeignKey('Tratamiento', blank=True, null=True, on_delete=models.CASCADE)
    idfisioterapeuta = models.ForeignKey('Fisioterapeuta', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)


class Historialmedico(models.Model):
    idFamiliar = models.OneToOneField('Familiar', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)


class HospiTramieMed(models.Model):
    idHospitalizacion = models.ForeignKey('Hospitalizacion', blank=True, null=True, on_delete=models.CASCADE)
    idTratamiento = models.ForeignKey('Tratamiento', blank=True, null=True, on_delete=models.CASCADE)


class Hospitalizacion(models.Model):
    idExpediente = models.OneToOneField('Expediente', blank=True, null=True, on_delete=models.CASCADE)
    fechaingreso = models.DateField()
    fechasalida = models.DateField()
    numerocamilla = models.IntegerField()
    sala = models.CharField(max_length=100)


class HospitalizacionExamenFisico(models.Model):
    idExamenFisico = models.ForeignKey('Examenfisico', blank=True, null=True, on_delete=models.CASCADE)
    idHospitalizacion = models.ForeignKey('Hospitalizacion', blank=True, null=True, on_delete=models.CASCADE)


class HospitalizacionExamenMedico(models.Model):
    idExamenMedico = models.ForeignKey('Examenmedico', blank=True, null=True, on_delete=models.CASCADE)
    idHospitalizacion = models.ForeignKey('Hospitalizacion', blank=True, null=True, on_delete=models.CASCADE)


class Laboratorista(models.Model):
    idPersona = models.OneToOneField('Persona', blank=True, null=True, on_delete=models.CASCADE)


class Medicamento(models.Model):
    nombre = models.CharField(max_length=25)
    dosis = models.FloatField()
    freciencia = models.CharField(max_length=25)


class Municipio(models.Model):
    idDepartamento = models.ForeignKey('Departamento', blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True, null=True)


class Paciente(models.Model):
    idPersona = models.OneToOneField('Persona', blank=True, null=True, on_delete=models.CASCADE)
    idResponsable = models.ForeignKey('Responsable', blank=True, null=True, on_delete=models.CASCADE)
    idEnfermera = models.ForeignKey('Enfermera', blank=True, null=True, on_delete=models.CASCADE)


class Persona(models.Model):
    idDireccion = models.OneToOneField('Direccion', blank=True, null=True, on_delete=models.CASCADE)
    primernombre = models.CharField(max_length=100)
    segundonombre = models.CharField(max_length=100)
    primerapellido = models.CharField(max_length=100)
    segundoapellido = models.CharField(max_length=100)
    dui = models.CharField(max_length=9)
    fechanacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)
    ocupacion = models.CharField(max_length=100)
    estadocivil = models.CharField(max_length=20)


class Responsable(models.Model):
    primernombre = models.CharField(max_length=10)
    segundonombre = models.CharField(max_length=10)
    primerapellido = models.CharField(max_length=10)
    segundoapellido = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)


class Terapia(models.Model):
    idTratamiento = models.OneToOneField('Tratamiento', blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, blank=True, null=True)


class TratamientoMedicamento:
    idTratamiento = models.OneToOneField('Tratamiento', blank=True, null=True, on_delete=models.CASCADE)
    idMedicamento = models.OneToOneField('Medicamento', blank=True, null=True, on_delete=models.CASCADE)


class Tratamiento(models.Model):
    idConsultamedica = models.OneToOneField('Consultamedica', blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()
