$("#nombre").on('keyup', function (event) {
    var newValue = this.value.replace(/[^a-z/A-Z]+/i, '');
    if (this.value != newValue) {
        this.value = newValue;
    }
});

$("#aPaterno").on('keyup', function (event) {
    var newValue = this.value.replace(/[^a-z/A-Z]+/i, '');
    if (this.value != newValue) {
        this.value = newValue;
    }
});

$("#aMaterno").on('keyup', function (event) {
    var newValue = this.value.replace(/[^a-z/A-Z]+/i, '');
    if (this.value != newValue) {
        this.value = newValue;
    }
});

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1;
var yyyy = today.getFullYear();
 if(dd<10){
        dd='0'+dd
    } 
    if(mm<10){
        mm='0'+mm
    } 

today = yyyy+'-'+mm+'-'+dd;
document.getElementById("Fecha_reserva").setAttribute("min", today);

function validateHhMm(inputField) {
    var isValid = /^([0-1]?[0-9]|2[0-4]):([0-5][0-9])(:[0-5][0-9])?$/.test(inputField.value);

    if (isValid) {
      inputField.style.backgroundColor = '#bfa';
    } else {
      inputField.style.backgroundColor = '#fba';
    }

    return isValid;
  }
