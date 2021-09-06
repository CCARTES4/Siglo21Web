$("#formularioReserva").validate({
    rules: {
        rut_cli: {
            required : true,
            minlength : 9,
            maxlength: 10,
        },
        nombre: {
            required: true,
            minlength: 1,
            maxlength: 20
        },
        aPaterno: {
            required: true,
            minlength: 1,
            maxlength: 20
        },
        aMaterno: {
            required: true,
            minlength: 1,
            maxlength: 20
        },
        correo: {
            required: true,
            email: true,
        },
        telefono: {
            required: true,
            maxlength: 9,
            minlength: 9,
            min: 900000000,
            max: 999999999
        },
        Fecha_reserva: {
            required: true
        },
        cant_personas: {
            required: true,
            min: 1
        },
        Hora: {
            required: true
        }
    }
})


$("#FormularioConsulta").validate({
    rules: {
        rut_cli: {
            required: true,
            minlength: 9,
            maxlength: 10
        },
        Fecha_reserva: {
            required: true,
        },
        Hora: {
            required: true
        },
        N_reserva: {
            required: true
        }
    }
})