function solve(input){
    switch (input) {
        case "Monday":
            output = 1;
            
            break;

            case "Tuesday":
            output = 2;
            
            break;

            case "Wednesday":
            output = 3;
            
            break;

            case "Thursday":
            output = 4;
            
            break;

            case "Friday":
            output = 5;
            
            break;

            case "Saturday":
            output = 6;
            
            break;

            case "Sunday":
            output = 7;
            
            break;
    
        default:
            output = 'error'
            break;
    }

    console.log(output);
}


// Chaov

const daysMap = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

function solve(day) {
    return daysMap[day] ? daysMap[day] : "error";
}

console.log(solve("Monday"));
console.log(solve("Friday"));
console.log(solve("Invalid"));
