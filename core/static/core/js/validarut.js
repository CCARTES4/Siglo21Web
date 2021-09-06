$("#rut_cli").on('keyup', function (event) {
    var newValue = this.value.replace(/[^k/0-9-]+/i, '');
    if (this.value != newValue) {
        this.value = newValue;
    }
});

