console.log("slush.js loaded")

function accept_manuscript(id) {
    console.log(id)
    fetch(`/manuscript/${id}`, {
        method: 'PUT',
    });
    document.getElementById(id).style.background = 'green';
    document.getElementById(id).style.color = 'white';

}