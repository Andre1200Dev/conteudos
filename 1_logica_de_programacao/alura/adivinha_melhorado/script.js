var chute = document.querySelector("input");
var numerosPensados = sorteiaNumeros(3);
var chances = 3;

var chancesHtml = document.getElementById("mostraChances");
var display = document.getElementById("display");
var resultado = document.getElementById("resultado");
display.innerHTML = "Você tem <strong>" + chances + "</strong> tentativas";
console.log(numerosPensados);

chute.focus();

function sorteia() {
  return Math.floor(Math.random() * 10);
}
function sorteiaNumeros(quantidade) {
  var numPensado = [];
  var numero = 1;
  while (numero <= quantidade) {
    var numAleatorio = sorteia();
    var achou = false;

    for (var posiçao = 0; posiçao < numPensado.length; posiçao++) {
      if (numPensado[posiçao] == numAleatorio) {
        achou = true;
        break;
      }
    }
    if (numAleatorio != 0) {
      if (achou == false) {
        numPensado.push(numAleatorio);
        numero++;
      }
    }
  }
  return numPensado;
}
function verifica() {
  var acertou = false;

  if (chances != 0) {
    for (var posiçao = 0; posiçao < numerosPensados.length; posiçao++) {
      if (chute.value == numerosPensados[posiçao]) {
        resultado.innerHTML = "Você acertou um dos numeros pensados é: " + numerosPensados[posiçao];
        display.innerHTML = "A rodada terminou recarregue para jogar novamente!";
        acertou = true;
        chances = 0;
        break;
      }
    }
    if ((acertou == false) & (chances != 0)) {
      resultado.innerHTML = "Você Errou";
      chances--;
      display.innerHTML = "Você tem <strong>" + chances + "</strong> tentativas";
    }
  } else {
    display.innerHTML = "A rodada terminou recarregue para jogar novamente!";
  }
  chute.value = "";
  chute.focus();
}
var botao = document.querySelector("button");
botao.onclick = verifica;