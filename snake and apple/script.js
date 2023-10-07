const snake = document.getElementById('snake');
const apple = document.getElementById('apple');
const gameContainer = document.getElementById('game-container');

let snakeX = 0;
let snakeY = 0;
let appleX = 0;
let appleY = 0;
let direction = 'right';

function randomPosition() {
    return Math.floor(Math.random() * 15) * 20;
}

function updateApplePosition() {
    appleX = randomPosition();
    appleY = randomPosition();
    apple.style.left = appleX + 'px';
    apple.style.top = appleY + 'px';
}

function updateSnakePosition() {
    switch (direction) {
        case 'up':
            snakeY -= 20;
            break;
        case 'down':
            snakeY += 20;
            break;
        case 'left':
            snakeX -= 20;
            break;
        case 'right':
            snakeX += 20;
            break;
    }

    if (snakeX === appleX && snakeY === appleY) {
        updateApplePosition();
    }

    snake.style.left = snakeX + 'px';
    snake.style.top = snakeY + 'px';
}

document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'ArrowUp':
            direction = 'up';
            break;
        case 'ArrowDown':
            direction = 'down';
            break;
        case 'ArrowLeft':
            direction = 'left';
            break;
        case 'ArrowRight':
            direction = 'right';
            break;
    }
});

updateApplePosition();
setInterval(updateSnakePosition, 200);
