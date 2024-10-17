document.getElementById('hitungBtn').addEventListener('click', function() {
    const jariJari = parseFloat(document.getElementById('jariJari').value);
    const hasilDiv = document.getElementById('hasil');

    if (isNaN(jariJari) || jariJari < 0) {
        hasilDiv.innerHTML = "Harap masukkan jari-jari yang valid.";
        return;
    }

    const luas = Math.PI * (jariJari ** 2);
    const keliling = 2 * Math.PI * jariJari;

    hasilDiv.innerHTML = `Luas Lingkaran: ${luas.toFixed(2)}<br>Keliling Lingkaran: ${keliling.toFixed(2)}`;
});