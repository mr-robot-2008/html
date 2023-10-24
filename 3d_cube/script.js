const cube = document.getElementById('cube');
let isRotating = true;

// Function to rotate the cube continuously
function rotateCube() {
    if (isRotating) {
        cube.style.animation = 'spin 10s infinite linear';
    }
}

// Start the rotation when the page loads
rotateCube();

cube.addEventListener('mouseenter', () => {
    isRotating = false;
    cube.style.animation = 'none'; // Stop rotation
});

cube.addEventListener('mouseleave', () => {
    isRotating = true;
    rotateCube(); // Resume continuous rotation
});

document.addEventListener('click', () => {
    isRotating = !isRotating; // Toggle continuous rotation on click
    if (isRotating) {
        rotateCube(); // Resume continuous rotation
    } else {
        cube.style.animation = 'none'; // Stop rotation
    }
});

// Function to add an extra rotation animation
function extraRotation() {
    cube.style.animation = 'spin 5s linear'; // Add a 5-second spin animation
}

// Call the extraRotation function when needed, e.g., on button click
// button.addEventListener('click', extraRotation);
