function sum(){

    var salary1 = document.getElementById('salary1').value || 0;
    var salary2 = document.getElementById('salary2').value || 0;
    var salary3 = document.getElementById('salary3').value || 0;
    var salary4 = document.getElementById('salary4').value || 0;

    var result = parseInt(salary1) + parseInt(salary2) + parseInt(salary3) + parseInt(salary4);

        document.getElementById('totalsalary').value = result;
}

function mult(value){

    var x ;

    x = 1000 * value ; 
    
    document.getElementById('expectedsubsidy').value = x;

    if (value > 4) {
        document.getElementById('expectedsubsidy').value = "4000";
    }
}

