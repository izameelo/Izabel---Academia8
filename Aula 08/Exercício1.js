let login = "@izameelo";
let senha = "izm2019";

let loginDigitado = prompt ("Digite seu login");
let senhaDigitada = prompt ("Digite sua senha");

if (login == loginDigitado){
    if (senha == senhaDigitada){
        alert ("Acesso liberado");
    } else {
        alert ("Acesso Negado");

    } 
    
} else {
    alert ("Tente outra vez!");
}

while (login =! loginDigitado){
    alert ("Você foi negado")

}
