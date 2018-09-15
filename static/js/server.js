function getData() {
    var xhttp = new XMLHttpRequest();
    var endpoint = '/generate-image';    
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           var res = JSON.parse(this.response);
           document.getElementById('query-result').style.backgroundImage = "url(" + res.image_url + ")";
        }
    };
    xhttp.open("POST", endpoint, true);
    var formData = new FormData();
    var description = document.getElementById("input").value;

    formData.append("description", description);
    xhttp.send(formData); 
}