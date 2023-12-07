FReader = new FileReader();
 
// событие, когда файл загрузится
FReader.onload = function(e) {
    document.querySelector("#result").src = e.target.result;
};
 
// выполнение функции при выборки файла
document.querySelector("input").addEventListener("change", loadImageFile);
 
// функция выборки файла
function loadImageFile() {
    var file = document.querySelector("input").files[0];
    FReader.readAsDataURL(file);
}
