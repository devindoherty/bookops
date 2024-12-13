console.log("editor.js loaded")

document.addEventListener('DOMContentLoaded', function() {
    // document.querySelector('#save-manuscript').addEventListener('click', () => save_manuscript());
    document.querySelector('#accepted-manuscripts').addEventListener('click', () => get_manuscripts('accepted'));
    document.querySelector('#my-manuscripts').addEventListener('click', () => get_manuscripts('my'));

    get_manuscripts('accepted')
});

function get_manuscripts(get) {
    console.log(get)
    document.querySelector(`#accepted-view`).innerHTML = ``;
    document.querySelector(`#my-view`).innerHTML = ``;


    document.querySelector('#edit-view').style.display = 'none';
    if (get == "accepted") {
        document.querySelector('#my-view').style.display = 'none';
        document.querySelector('#accepted-view').style.display = 'block';
    } else {
        document.querySelector('#my-view').style.display = 'block';
        document.querySelector('#accepted-view').style.display = 'none';
    }

    fetch(`/manuscripts/${get}`)
        .then(response => response.json())
        .then(manuscripts => {
            console.log(get);
            console.log(manuscripts);
            manuscripts.forEach(element => {
                var manuscript = `<br><div class="manuscript" id="${element["id"]}" onclick = "edit_manuscript(this.id)" style="border: thin solid black;"> ${element["title"]}<br> By: ${element["author"]}<br> Synopsis: ${element["synopsis"]}<br> Time: ${element["timestamp"]} </div><br>`
                if (get == "accepted") {
                    document.querySelector(`#accepted-view`).innerHTML += manuscript;
                } else {
                    document.querySelector(`#my-view`).innerHTML += manuscript;
                }
            });
        });
}

function edit_manuscript(id) {
    console.log("Edit Click")
    console.log(id)
    document.querySelector(`#accepted-view`).innerHTML = ``;
    document.querySelector(`#my-view`).innerHTML = ``;
    document.querySelector('#accepted-view').style.display = 'none';
    document.querySelector('#my-view').style.display = 'none';
    document.querySelector('#edit-view').style.display = 'block';
    
    fetch(`/manuscript/${id}`)
        .then(response => response.json())
        .then(manuscript => {
            console.log(manuscript)
            var author = manuscript["author"];
            var title = manuscript["title"];
            var synopsis = manuscript["synopsis"];
            var body = manuscript["body"];
            var id = manuscript["id"];

            document.querySelector('#edit-author').value = author;
            document.querySelector('#edit-title').value = title;
            document.querySelector('#edit-synopsis').value = synopsis;
            document.querySelector('#edit-body').value = body;
            document.querySelector('#save-button-container').innerHTML = `<button class="btn btn-lg btn-outline-primary" onclick="save_manuscript(${id})">Save</button>`
        });
}

function save_manuscript(id) {
    title = document.querySelector('#edit-title').value;
    synopsis = document.querySelector('#edit-synopsis').value;
    body = document.querySelector('#edit-body').value;

    fetch(`/manuscript/edit/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            title: title,
            synopsis: synopsis,
            body: body,
        })
    });
}