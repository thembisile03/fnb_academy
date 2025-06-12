let rootpath = "https://mysite.itvasity.org/api/ContactBook";
let apikey = checkapikey();

function checkapikey() {
    if (!localStorage.getItem("apikey")) {
        window.open("enter-api-key.html", "_self");
    }
    return localStorage.getItem("apikey");
}
