let slideIndex = 1;
class mascotas {
    constructor(nombre,elmento,hp,df){
            this.nombre = nombre;
            this.elemento = elmento;
            this.hp = hp;
            this.df = df;
               
    }
    setNombre(name){
        this.nombre = name;
    }
    setElemento(element){
        this.elemento = element;
    }
    setHp(vida){
        this.hp = vida;
    }
    setDf(defense){
        this.df = defense;
    }

    getNombre(){
        return(this.nombre)
    }
    getHp(){
        return(this.hp);
    }
    
    getDf(){
        return(this.df);
    }
    
    getElemento(){
        return(this.elemento);
    }
    
    
    ataque(){
        let valorAtaque = aleatorio(1,2);
        return(valorAtaque);
    }
    ataqueElemento(){
        let ataqueElemento = aleatorio(2,4);
        return(ataqueElemento);
    }
    sanacion(){
        this.hp += 2;
        if(this.hp >= 10){
            this.hp = 10;
        }
    }
    recibirAtaque(){
        let vida = this.hp;
        let valorAtaque = this.ataque();
        let absorcion = (1/4)*this.df;
        vida = vida -(valorAtaque-absorcion);
        this.setHp(vida);
    }
    recibirAtaqueELemental(ataqueElemental){
    let vida = this.getHp();
    let valorDeAtaque = ataque[1];
    let elementoMensajero = ataque[0];
    let elementoReceptor = this.getElemento();
    let porcentaje = aleatorio(0.1,0.5);
    let resultado = this.tablaDeComparacion(elementoMensajero,elementoReceptor);
    switch(resultado){
        case "igual":
            vida -= valorDeAtaque;
        break;
        case "menor":
            vida -= valorDeAtaque -(porcentaje*valorDeAtaque);
        break;
        case "mayor":
            vida -= valorDeAtaque +(porcentaje*valorDeAtaque);
        break;
    }
    this.setHp(vida);

    }
    tablaDeComparacion(elementoMensajero,elementoReceptor){
        let tabla = ["fuego","agua","aire","tierra"];
        let valor = "esperando";
        switch(elementoMensajero){
            case "fuego":
                tabla = ["igual","mayor","igual","menor"];
            break;
            case "agua":
                tabla = ["menor","normal","mayor","normal"];
            break;
            case "aire":
                tabla = ["igual","menor","normal","mayor"];
            break;
            case "tierra":
                tabla = ["mayor","normal","menor","normal"];
            break;
            
        }
        valor = tabla[elementoReceptor];
        return(valor);

    }
}
function startBattle(){
    let player = new mascotas("","",10,2);
    showSlides(slideIndex);
}
function aleatorio(min,max){
    let difference = max -min;
    let rand = Math.random();
    rand = Math.floor(rand*difference);
    rand = rand + min;
    return rand;
}



// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("petSlide");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}
function createPet(){
    let health = 10;
    let defense = 2;
    let name;
    let elemento;
    switch(n){
        case 0:
            name = "hipodoge";
            elemento = "agua";
            player.setNombre(name);
            player.setElemento(elemento);
            console.log(player);
        break;
        case 1:
            name ="capipepo";
            elemento = "tierra";
            player.setNombre(name);
            player.setElemento(elemento);
            console.log(player);
  
        break;
        case 2:
            name = "ratigueya";
            elemento = "fuego";
            player.setNombre(name);
            player.setElemento(elemento);
            console.log(player);
        break;

    }
    
}
window.addEventListener("load",startBattle)
//la diferencia entre mi codigo y este, es que este pasa directamente la suma del slide por una funcion en el tag directamente, eso es lo que me falto para completar mi slide