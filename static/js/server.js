function getData() {
    var xhttp = new XMLHttpRequest();
    var endpoint = 'https://htn-criminal-generation.azurewebsites.net/generate-image';    
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           console.log(this.response);
           var url = 'https://www.rover.com/blog/wp-content/uploads/2017/08/puppy-header-960x540.jpg';
           document.getElementById('query-result').style.backgroundImage = "url(" + url + ")";
        }
    };
    xhttp.open("POST", endpoint, true);
    var form = document.createElement("form");
    form.setAttribute("description", "little asian girl with yellow hair");
    xhttp.send(form);
}