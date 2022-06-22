const option = document.getElementById("option"),
result = document.getElementById("result"),
valone = document.getElementById("valone"), 
valtwo = document.getElementById("valtwo"); 
function solve(){
    num1 = parseInt(valone.value);
    num2 = parseInt(valtwo.value);
    if(option.value == "add"){
        soln = num1 + num2;
        result.innerHTML = soln;
    }
    if(option.value == "subtract"){
        soln = num1 - num2;
        result.innerHTML = soln;
    }
    if(option.value == "divide"){
        soln = num1 / num2;
        soln = soln.toFixed(4);
        result.innerHTML = soln;
    }
    if(option.value == "multiply"){
        soln = num1 * num2;
        result.innerHTML = soln;
    }
    
}