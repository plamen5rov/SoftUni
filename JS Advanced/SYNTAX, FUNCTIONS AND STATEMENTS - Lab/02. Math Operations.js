function solve(num1, num2, operator) {

    var result;

    switch (operator) {
        case '+':

            result = num1 + num2;
            return result;

        case '-':

            result = num1 - num2;
            return result;

            break;

        case '*':

            result = num1 * num2;
            return result;

        case '/':

            result = num1 / num2;
            return result;

        case '%':

            result = num1 % num2;
            return result;

        case '**':

            result = num1 ** num2;
            return result;

        default:
            break;
    }

    console.log(result);

}
