// Verificar si hay una sesión activa al cargar la página
window.onload = () => {
    const usuarioActual = localStorage.getItem("usuarioActual");
    if (usuarioActual && usuarios[usuarioActual]) {
        alert(`¡Bienvenido de nuevo, ${usuarios[usuarioActual].nombre}!`);
        document.getElementById("usuario-actual").textContent = usuarios[usuarioActual].nombre;
        mostrarPanel(usuarioActual);
    } else {
        mostrarRegistroInicio();
    }
};

// Manejar la transición entre vistas
const mostrarRegistroInicio = () => {
    document.getElementById("registro").style.display = "block";
    document.getElementById("inicio").style.display = "block";
    document.getElementById("panel").style.display = "none";
};

const mostrarPanel = (correo) => {
    document.getElementById("registro").style.display = "none";
    document.getElementById("inicio").style.display = "none";
    document.getElementById("panel").style.display = "block";
    document.getElementById("puntos").textContent = usuarios[correo].puntos;

    // Guardar correo actual en localStorage
    localStorage.setItem("usuarioActual", correo);
};

// Registro de usuarios
document.getElementById("registro-btn").addEventListener("click", () => {
    const nombre = document.getElementById("nombre-usuario").value.trim();
    const correo = document.getElementById("correo-electronico").value.trim();
    const contraseña = document.getElementById("contraseña").value.trim();
    const edad = document.getElementById("edad").value.trim();
    const genero = document.getElementById("genero").value;

    // Validar campos completos
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
    mostrarPanel(correo);
});

// Inicio de sesión
document.getElementById("login-btn").addEventListener("click", () => {
    const correo = document.getElementById("login-correo").value.trim();
    const contraseña = document.getElementById("login-contraseña").value.trim();

    if (usuarios[correo] && usuarios[correo].contraseña === contraseña) {
        alert(`Inicio de sesión exitoso. Bienvenido, ${usuarios[correo].nombre}!`);
        document.getElementById("usuario-actual").textContent = usuarios[correo].nombre;
        mostrarPanel(correo);
    } else {
        alert("Correo o contraseña incorrectos.");
    }
});