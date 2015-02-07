function initialize() {
	var mapOptions = {
		zoom: 8,
		center: new google.maps.LatLng(-.397, 150.644)
	};
	var map = new google.maps.Map(document.getElementById('map'),mapOptions);
	var bounds = new google.maps.LatLngBounds();
	$.ajax({
		url: 'get_gps',
		data: {
			numberOfPoints: 10000
		},
		dataType: 'json',
		success: function(result) {
			var locations = [];
			_.each(result.locations, function(location){
				var marker = new google.maps.Marker({
					position: new google.maps.LatLng(location.latitude, location.longitude),
					map: map,
					title: location.provider
				});
				bounds.extend(marker.position);
			});
			map.fitBounds(bounds);
		}
	});
}

google.maps.event.addDomListener(window, 'load', initialize);