import * as bootstrap from 'bootstrap';
window.bootstrap = bootstrap;

setTimeout(function () {
            let messages = document.getElementById("msg");
            let alert = new bootstrap.Alert(messages);
            alert.close();
}, 3000);

module.exports = {setTimeout, bootstrap};