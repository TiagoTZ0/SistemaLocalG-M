// Simulación: Mapeo de Rol -> Usuario Específico
const identities = {
    'Admin': { name: 'Bruno', email: 'bruno@mail.com' },
    'Vendedor': { name: 'Carlos', email: 'carlos@mail.com' },
    'Despachador': { name: 'Jhon', email: 'jhon@mail.com' }
};

function handleLogin(event) {
    event.preventDefault();
    
    const roleSelect = document.getElementById('role');
    const selectedRole = roleSelect.value;
    const usernameTyped = document.getElementById('username').value;
    const passwordTyped = document.getElementById('password').value;

    if (!selectedRole) {
        alert("Por favor seleccione un rol.");
        return;
    }
    if (!passwordTyped ) {
        alert("Por favor ingrese la contraseña hdp.");
        return;
    }

    if (!usernameTyped) {
        alert("Por favor ingrese el usuario hdp.");
        return;
    }



    // SIMULACIÓN: Login exitoso forzando la identidad del rol
    const identity = identities[selectedRole];

    const user = { 
        username: identity.name, 
        email: identity.email,
        role: selectedRole 
    };


    localStorage.setItem('user', JSON.stringify(user));
    
    alert("✅ ¡Bienvenido " + user.username + "!\n\nRol: " + user.role);
    
    window.location.reload();

}
