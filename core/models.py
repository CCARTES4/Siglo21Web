# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apaterno = models.CharField(max_length=20)
    amaterno = models.CharField(max_length=20)
    correo = models.CharField(max_length=40)
    telefono = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class EstadoMesa(models.Model):
    id_est_mesa = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'estado_mesa'


class EstadoOrden(models.Model):
    id_est_orden = models.BigIntegerField(primary_key=True)
    estado_orden = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estado_orden'


class EstadoPago(models.Model):
    id_est_pag = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'estado_pago'


class EstadoSolicitud(models.Model):
    id_est_sol = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'estado_solicitud'


class Mesa(models.Model):
    nro_mesa = models.BigIntegerField(primary_key=True)
    cant_silla = models.BigIntegerField()
    id_est_mesa = models.ForeignKey(EstadoMesa, models.DO_NOTHING, db_column='id_est_mesa')

    class Meta:
        managed = False
        db_table = 'mesa'


class Orden(models.Model):
    orden_id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    total_orden = models.BigIntegerField()
    rut_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cli')
    rut = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='rut')
    id_est_orden = models.ForeignKey(EstadoOrden, models.DO_NOTHING, db_column='id_est_orden')
    idpago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='idpago')
    nro_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='nro_mesa')

    class Meta:
        managed = False
        db_table = 'orden'


class OrdenPlato(models.Model):
    orden_plato_id = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    orden = models.ForeignKey(Orden, models.DO_NOTHING)
    id_plato = models.ForeignKey('Plato', models.DO_NOTHING, db_column='id_plato')

    class Meta:
        managed = False
        db_table = 'orden_plato'


class Pago(models.Model):
    idpago = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    id_est_pag = models.ForeignKey(EstadoPago, models.DO_NOTHING, db_column='id_est_pag')

    class Meta:
        managed = False
        db_table = 'pago'


class Plato(models.Model):
    id_plato = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=35)
    fecha_menu = models.DateField()

    class Meta:
        managed = False
        db_table = 'plato'


class PlatoIngrediente(models.Model):
    plato_ingrediente_id = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    id_plato = models.ForeignKey(Plato, models.DO_NOTHING, db_column='id_plato')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'plato_ingrediente'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=255)
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoSolicitud(models.Model):
    id_prod_sol = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud')

    class Meta:
        managed = False
        db_table = 'producto_solicitud'


class Proveedor(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Reserva(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    fecha_reserva = models.DateField()
    cant_personas = models.BigIntegerField()
    hora = models.CharField(max_length=5)
    fec_cre_res = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    rut_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cli')

    class Meta:
        managed = False
        db_table = 'reserva'


class Solicitud(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    total = models.BigIntegerField()
    id_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='id_proveedor')
    id_est_sol = models.ForeignKey(EstadoSolicitud, models.DO_NOTHING, db_column='id_est_sol')

    class Meta:
        managed = False
        db_table = 'solicitud'


class TipoUsuario(models.Model):
    id_tipo = models.BigIntegerField(primary_key=True)
    descripcion_tipo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Trabajador(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apaterno = models.CharField(max_length=20)
    amaterno = models.CharField(max_length=15)
    passwd = models.CharField(max_length=30)
    id_tipo = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'trabajador'
