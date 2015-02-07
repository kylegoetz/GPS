function initialize() {
	var mapOptions = {
		zoom: 8
	};
	var map = new google.maps.Map(document.getElementById('map'),mapOptions);
	var bounds = new google.maps.LatLngBounds();
	$.ajax({
		url: 'get_current_location',
		dataType: 'json',
		success: function(result) {
			var marker = new google.maps.Marker({
				position: new google.maps.LatLng(location.latitude, location.longitude),
				map: map,
				title: 'Current Location'
			});
			bounds.extend(marker.position);
			map.fitBounds(bounds);
		}
	});
}

google.maps.event.addDomListener(window, 'load', initialize);