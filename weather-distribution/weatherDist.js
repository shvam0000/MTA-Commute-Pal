var map;
var heatmap;
var dateDropdown;
var timeDropdown;

function initMap() {
  dateDropdown = document.getElementById('dateDropdown');
  timeDropdown = document.getElementById('timeDropdown');

  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: { lat: 40.79059982299805, lng: -73.94747924804688 },
  });

  // Create an InfoWindow for the popup
  var infoWindow = new google.maps.InfoWindow();

  function update() {
    var selectedDate = dateDropdown.value;
    var selectedTime = timeDropdown.value;
    updateData(selectedDate, selectedTime);
  }

  // Function to update the heatmap
  function updateData(date, time) {
    const timestamp = date + time;
    fetch(
      'https://data.ny.gov/resource/wujg-7c2s.json?transit_timestamp=' +
        timestamp
    )
      .then((response) => response.json())
      .then((data) => {
        // Process and create heatmapData with weights from the 'ridership' field
        var heatmapData = data.map(function (item) {
          var latitude = parseFloat(item.latitude);
          var longitude = parseFloat(item.longitude);
          var ridership = parseFloat(item.ridership);

          return {
            location: new google.maps.LatLng(latitude, longitude),
            weight: ridership, // Use 'ridership' as the weight
          };
        });

        // Create a heatmap layer with weights
        heatmap.setData(heatmapData);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }

  // Create the heatmap layer
  heatmap = new google.maps.visualization.HeatmapLayer({
    data: [], // Initially, no data
    map: map,
  });

  // Set gradient colors (optional)

  // Customize heatmap options (e.g., radius and opacity)
  heatmap.set('radius', 50);
  heatmap.set('opacity', 0.7);

  // Initialize the date and time dropdowns
  dateDropdown.value = '2023-09-24';
  timeDropdown.value = 'T00:00:00.000';

  // Event listeners for date and time dropdowns
  dateDropdown.addEventListener('change', update);
  timeDropdown.addEventListener('change', update);

  // Initial data load
  updateData('2023-09-24', 'T00:00:00.000');
}
