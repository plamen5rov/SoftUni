function roadRadar(input) {

    let speed = Number(input[0]);

    let area = input[1];

    switch (area) {
        case 'motorway':

            if (speed > 130) {

                let overspeed = speed - 130;

                if (overspeed <= 20) {

                    console.log('speeding');

                } else if (overspeed <= 40) {
                    console.log('excessive speeding');

                } else {
                    console.log('reckless driving');
                }
            }

            break;

            case 'interstate':

            if (speed > 90) {

                let overspeed = speed - 90;

                if (overspeed <= 20) {

                    console.log('speeding');

                } else if (overspeed <= 40) {
                    console.log('excessive speeding');
                    
                } else {
                    console.log('reckless driving');
                }
            }

            break;

            case 'city':

            if (speed > 50) {

                let overspeed = speed - 50;

                if (overspeed <= 20) {

                    console.log('speeding');

                } else if (overspeed <= 40) {
                    console.log('excessive speeding');
                    
                } else {
                    console.log('reckless driving');
                }
            }

            break;

            case 'residential':

            if (speed > 20) {

                let overspeed = speed - 20;

                if (overspeed <= 20) {

                    console.log('speeding');

                } else if (overspeed <= 40) {
                    console.log('excessive speeding');
                    
                } else {
                    console.log('reckless driving');
                }
            }

            break;

        default:
            break;
    }

}


