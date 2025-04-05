document.getElementById("registro-btn").addEventListener("click", () => {
    const nombre = document.getElementById("nombre-usuario").value.trim();
    const correo = document.getElementById("correo-electronico").value.trim();
    const contraseña = document.getElementById("contraseña").value.trim();
    const edad = document.getElementById("edad").value.trim();
    const genero = document.getElementById("genero").value;

    // Validar que todos los campos estén completos
    if (!nombre || !correo || !contraseña || !edad || !genero) {
        alert("Todos los campos son obligatorios. Por favor, completa el formulario.");
        return;
    }

    // Validar unicidad del correo
    if (usuarios[correo]) {
        alert("El correo ya está registrado. Usa otro.");
        return;
    }

    // Registrar usuario si pasa las validaciones
    usuarios[correo] = { nombre, contraseña, edad, genero, puntos: 100, codigos_generados: [] };
    localStorage.setItem("usuarios", JSON.stringify(usuarios));
    alert("Registro exitoso.");
    mostrarInicioSesion();
});