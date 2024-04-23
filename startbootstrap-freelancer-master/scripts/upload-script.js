function allowDrop(event) {
    event.preventDefault();
}

function uploadFile(event) {
    event.preventDefault();
    var files = event.dataTransfer.files;
    var formData = new FormData();
    formData.append('file', files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            alert('File uploaded successfully to Google Drive!');
        } else {
            alert('Failed to upload file.');
        }
    })
    .catch(error => console.error('Error:', error));
}
