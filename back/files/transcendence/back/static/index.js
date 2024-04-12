function showSection(section) {   
    fetch(`/test/`)
    .then(response => response.text())
    .then(text => {
        console.log(text);
        document.querySelector('#content').innerHTML = text;
    });

}

var btn = document.getElementById("btn-1");
btn.addEventListener("click", function(){
    chargerScript(btn.value);
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            showSection(this.dataset.section)
        }
    })
});

function chargerScript(value) {
    var script = document.createElement('script');
    script.src = "/static/" + value;
    var index_script = document.querySelector('#script_js');
    index_script.parentNode.insertBefore(script, index_script.nextSibling)
}
