const fileInput = document.getElementById('file-input');
const labelDiv = document.getElementById('label-div');
const hiddenButton = document.getElementById('hidden-btn');
const scannerButton = document.getElementById('scanner-btn');

fileInput.addEventListener('change', function() {
    if (fileInput.files.length > 0) {
        // alert('File selected: ' + fileInput.files[0].name);
        fileInput.disabled = true; // disable the input
        labelDiv.style.display = 'none' // hide the whole div

        hiddenButton.className = 'fa fa-check scanner-btn';
        hiddenButton.style.backgroundColor = 'green'; 
        hiddenButton.style.display = 'block'
        hiddenButton.style.border = 'none' // remove the ugly outline
    } else {
    
        // scannerButton.style.backgroundColor = '#007bff'; // re
    }
});

hiddenButton.addEventListener('click', function() {
    // sends the fileinput to backend 
    const formData = new FormData();
    let responseData = [];
    formData.append('image', fileInput.files[0]);
    fetch('/api/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        return response.json();
    })
    .then(response_data => {
        if (response_data["data"] == "No response! Please refresh the IP/captcha") {
            alert("Please refresh the captcha through GET /api/solve!")
            location.reload()
        } else {
            responseData = response_data["data"]
            if (responseData[1]) {
                window.location.href = '/electronic?electronic=' + responseData[0];
            } else {
                window.location.href = '/404?predicted_item=' + responseData[0];
            }
            console.log(responseData)
            // location.reload()
        }
    })
    .catch(error => {
        alert("There's an error, please call Nok Yin Lim to fix! I'm not present tmr: " + error)
        location.reload()
    });
});