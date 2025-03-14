let selected_pattern = -1

function select_pattern(id) {

}

document.addEventListener("keydown", e => {
    if (e.key === "Enter") {
        let input = document.getElementById("input");
        let patternsList = document.getElementById("patterns"); // Lista donde se agregan los <li>

        if (input && input.value.trim().length > 0) {  // Verifica que el input no esté vacío
            fetch(`http://127.0.0.1:8000/pattern/contains/${encodeURIComponent(input.value)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Error en la solicitud");
                }
                return response.json(); // Convertir la respuesta en JSON (array de objetos)
            })
            .then(data => {
                patternsList.innerHTML = ""; // Limpiar la lista antes de agregar nuevos elementos
                
                data.forEach(p => {
                    let li = document.createElement("li");
                    li.className = "fs-4 fw-semibold border-bottom border-2 border-black";
                    li.textContent = p.name; // Asigna el nombre dentro del <li>
                    li.onclick = () => select_pattern(p.id); // Asigna la función al evento onclick

                    patternsList.appendChild(li); // Agregar el <li> a la lista
                });

                input.value = ""; // Limpia el input después de procesar
            })
            .catch(error => console.error("Error:", error)); // Capturar errores
        }
    }
});
