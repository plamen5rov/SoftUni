function timeToWalk(steps, stepLength, speed) {
    let length = steps * stepLength;
    let totalRestInMinutes = Math.floor(length / 500);
    let totalTime = length / speed / 1000 * 60;

    let totalTimeInSeconds = Math.ceil((totalRestInMinutes + totalTime) * 60);

    let result = new Date(null, null, null, null, null, totalTimeInSeconds);

    return result.toTimeString().split(' ')[0];


}
