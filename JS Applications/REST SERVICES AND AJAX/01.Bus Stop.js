function getInfo() {

    // Get HTML elements reference

    const inputField = document.querySelector("#stopId");

    const submitBtn = document.querySelector("#submit");

    const stopName = document.querySelector("#stopName");

    const buses = document.querySelector("#buses");

    const stopId = inputField.value;
    
    // Clear previous data

    buses.innerHTML = '';

    // Fetch data from Firebase & Show Info


    const url = `https://judgetests.firebaseio.com/businfo/${stopId}.json`;

    fetch(url)
        .then(data => data.json())
        .then(data => {
            inputField.value = '';
            stopName.textContent = data.name;
            Object.entries(data.buses).forEach(bus => {
                let currentBus = document.createElement('li');

                currentBus.textContent = `Bus ${bus[0]} arrives in ${bus[0]} minutes.`;
                buses.appendChild(currentBus);
            });
        })
        .catch(() => {
            stopName.textContent = "Error";
        });


}
