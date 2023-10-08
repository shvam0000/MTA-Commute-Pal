document.addEventListener('DOMContentLoaded', function () {
  const apiKey = 'fe1cfbd5a6a0cfb0352dbdcaf6a52e38';
  const temperatureResult = document.getElementById('temperatureResult');
  const fetchTemperatureButton = document.getElementById('fetchTemperature');
  const dateDropdown = document.getElementById('dateDropdown');

  fetchTemperatureButton.addEventListener('click', function () {
    const selectedDate = dateDropdown.value;
    console.log(selectedDate);

    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=Manhattan&dt=${Math.round(
      new Date(selectedDate).getTime() / 1000
    )}&appid=${apiKey}`;

    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        const temperature = data.main.temp;
        const temperatureCelsius = (temperature - 273.15).toFixed(2);

        temperatureResult.innerHTML = `Temperature in New York City on ${selectedDate} is ${temperatureCelsius} °C`;
      })
      .catch((error) => {
        temperatureResult.innerHTML = `Failed to fetch temperature data: ${error.message}`;
      });
  });
});
