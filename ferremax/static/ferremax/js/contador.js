// Establecer la fecha límite (1 día desde ahora)
var deadline = new Date();
deadline.setDate(deadline.getDate() + 1);

// Función para actualizar el temporizador cada segundo
function updateTimer() {
  var currentTime = new Date();
  var difference = deadline - currentTime;

  var days = Math.floor(difference / (1000 * 60 * 60 * 24));
  var hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((difference % (1000 * 60)) / 1000);

  document.getElementById("days").innerText = formatTime(days);
  document.getElementById("hours").innerText = formatTime(hours);
  document.getElementById("minutes").innerText = formatTime(minutes);
  document.getElementById("seconds").innerText = formatTime(seconds);

  // Cuando la cuenta regresiva llega a 0, mostrar un mensaje
  if (difference <= 0) {
    clearInterval(timerInterval);
    document.getElementById("timer").innerHTML = "<h2>¡Tiempo terminado!</h2>";
  }
}

// Función para agregar un cero delante de los números menores que 10
function formatTime(time) {
  return time < 10 ? "0" + time : time;
}

// Actualizar el temporizador cada segundo
var timerInterval = setInterval(updateTimer, 1000);
