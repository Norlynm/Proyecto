const notificationSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/notifications/'
);

notificationSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log('Mensaje recibido:', data.message);
    alert(data.message);  // Alerta o notificación al usuario
};
