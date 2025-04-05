document.addEventListener("DOMContentLoaded", () => {
    const proyectosLista = document.getElementById("proyectos-lista");

    const proyectos = [
        { nombre: "Agenda App", descripcion: "Aplicación de gestión de tareas con PyQt6." },
        { nombre: "Página web interactiva", descripcion: "Explorando HTML, CSS y JavaScript." }
    ];

    proyectos.forEach(proyecto => {
        const div = document.createElement("div");
        div.innerHTML = `<h3>${proyecto.nombre}</h3><p>${proyecto.descripcion}</p>`;
        proyectosLista.appendChild(div);
    });
});